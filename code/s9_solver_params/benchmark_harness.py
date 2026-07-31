"""S9 -- plumbing: a reusable benchmark harness for parameter sweeps.

This is infrastructure, not the learning goal (see CLAUDE.md section 2) -- the learning goal
is choosing what to sweep and interpreting the results, which happens in the three task.py
files in this folder.

Usage:
    from benchmark_harness import run_param_sweep, print_report

    def build_model():
        # return a fresh, fully-built (but not yet optimized) gurobipy Model
        ...

    results = run_param_sweep(build_model, [
        {"Threads": 1}, {"Threads": 4}, {"Threads": 8},
    ])
    print_report(results)
"""
import time
from typing import Callable, List, Dict, Any

import gurobipy as gp
from gurobipy import GRB


def run_param_sweep(build_model: Callable[[], gp.Model],
                     param_grid: List[Dict[str, Any]],
                     capture_vars: bool = True) -> List[Dict[str, Any]]:
    """For each dict of {param_name: value} in param_grid: build a fresh model, apply the
    params, solve it, and record timing + solution info.

    Returns a list of result dicts, one per param set, each containing:
      params, runtime_s, status, obj_val, mip_gap, node_count, var_values (optional)
    """
    results = []
    for params in param_grid:
        m = build_model()
        m.Params.OutputFlag = 0
        for name, value in params.items():
            m.setParam(name, value)

        start = time.perf_counter()
        m.optimize()
        runtime = time.perf_counter() - start

        entry = {
            "params": dict(params),
            "runtime_s": runtime,
            "status": m.Status,
            "obj_val": m.ObjVal if m.SolCount > 0 else None,
            "mip_gap": m.MIPGap if m.IsMIP and m.SolCount > 0 else None,
            "node_count": m.NodeCount,
        }
        if capture_vars and m.SolCount > 0:
            entry["var_values"] = {v.VarName: v.X for v in m.getVars()}
        results.append(entry)
        m.dispose()
    return results


def print_report(results: List[Dict[str, Any]]) -> None:
    print(f"{'params':40} {'runtime_s':>10} {'obj_val':>12} {'gap':>8} {'nodes':>8}")
    for r in results:
        gap_str = f"{r['mip_gap']:.4f}" if r["mip_gap"] is not None else "-"
        obj_str = f"{r['obj_val']:.4f}" if r["obj_val"] is not None else "-"
        print(f"{str(r['params']):40} {r['runtime_s']:10.4f} {obj_str:>12} "
              f"{gap_str:>8} {r['node_count']:8.0f}")


def solutions_match(results: List[Dict[str, Any]], tol: float = 1e-6) -> bool:
    """Check whether every result in the list has the same variable values (within tol) as
    the first. Useful for confirming a 'speed-only' claim about a parameter.
    """
    if not results or "var_values" not in results[0]:
        return False
    baseline = results[0]["var_values"]
    for r in results[1:]:
        values = r.get("var_values", {})
        if values.keys() != baseline.keys():
            return False
        if any(abs(values[k] - baseline[k]) > tol for k in baseline):
            return False
    return True
