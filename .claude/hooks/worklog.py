#!/usr/bin/env python
# .claude/hooks/worklog.py
# Appends one line to the current month's work log. Adapted from the equivalent hook in
# ../ALDA_placementOptimizer/.claude/hooks/worklog.py.
# Usage (set by settings.json): worklog.py prompt   |   worklog.py stop

import sys, json, os, datetime, csv

event = sys.argv[1] if len(sys.argv) > 1 else "event"
data = json.load(sys.stdin)

session_id = data.get("session_id", "unknown")
project = os.environ.get("CLAUDE_PROJECT_DIR", data.get("cwd", "."))
topic = (data.get("prompt", "") or "").strip().replace("\n", " ")[:120]

input_tokens = ""
output_tokens = ""

if event == "stop":
    transcript_path = data.get("transcript_path", "")
    if transcript_path and os.path.exists(transcript_path):
        try:
            with open(transcript_path, encoding="utf-8") as tf:
                lines = tf.readlines()

            # Find the last real user message (not a tool result) -- that's the turn boundary
            last_user_idx = -1
            for i in range(len(lines) - 1, -1, -1):
                try:
                    e = json.loads(lines[i])
                    if e.get("type") == "user" and not e.get("toolUseResult"):
                        last_user_idx = i
                        break
                except Exception:
                    pass

            # Sum tokens across all unique API calls (requestId) after that boundary.
            seen_req = set()
            total_in, total_out = 0, 0
            slice_start = last_user_idx + 1 if last_user_idx >= 0 else 0
            for line in lines[slice_start:]:
                try:
                    e = json.loads(line)
                    if e.get("type") != "assistant":
                        continue
                    req_id = e.get("requestId") or e.get("uuid", "")
                    if req_id in seen_req:
                        continue
                    seen_req.add(req_id)
                    u = e.get("message", {}).get("usage", {})
                    total_in += (
                        u.get("input_tokens", 0)
                        + u.get("cache_read_input_tokens", 0)
                        + u.get("cache_creation_input_tokens", 0)
                    )
                    total_out += u.get("output_tokens", 0)
                except Exception:
                    pass

            if total_in or total_out:
                input_tokens = total_in
                output_tokens = total_out
        except Exception:
            pass

log_dir = os.path.join(project, ".claude", "workProgress")
os.makedirs(log_dir, exist_ok=True)

now = datetime.datetime.now().astimezone()
month_file = os.path.join(log_dir, now.strftime("%Y-%m") + ".csv")
is_new = not os.path.exists(month_file)

with open(month_file, "a", newline="") as f:
    w = csv.writer(f)
    if is_new:
        w.writerow(["timestamp", "session_id", "event", "topic", "input_tokens", "output_tokens"])
    w.writerow([now.isoformat(timespec="seconds"), session_id, event, topic, input_tokens, output_tokens])
