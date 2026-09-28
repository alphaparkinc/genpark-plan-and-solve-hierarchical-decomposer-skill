import sys
import json
from client import PlanAndSolveDecomposer

planner = PlanAndSolveDecomposer()

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "plan_and_solve_decompose",
                        "description": "Decompose complex multi-step prompt into structured sequential execution subtasks",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "query": {"type": "string"}
                            },
                            "required": ["query"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "plan_and_solve_decompose":
            p = planner.generate_plan(args["query"])
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"query": args["query"], "plan": p})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
