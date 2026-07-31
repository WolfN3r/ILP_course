"""S0 -- environment check. Fully written (pure verification, not a learning goal).

Run with: python code/s0_orientation/check_environment.py
"""
import sys


def main() -> None:
    print(f"Python version: {sys.version}")

    try:
        import gurobipy as gp
        from gurobipy import GRB
    except ImportError:
        print("gurobipy is NOT installed in this environment. Run:")
        print("  pip install -r requirements.txt")
        return

    print(f"gurobipy version: {gp.gurobi.version()}")

    try:
        m = gp.Model("license_check")
        m.Params.OutputFlag = 0
        x = m.addVar(name="x")
        m.setObjective(x, GRB.MAXIMIZE)
        m.addConstr(x <= 1)
        m.optimize()
        status_ok = m.Status == GRB.OPTIMAL
        print(f"Trivial solve status: {m.Status} (OPTIMAL == {GRB.OPTIMAL}) -> "
              f"{'OK' if status_ok else 'UNEXPECTED'}")
        print(f"License: {'appears to be working' if status_ok else 'check needed'}")
    except gp.GurobiError as e:
        print(f"Gurobi license/setup problem: {e}")


if __name__ == "__main__":
    main()
