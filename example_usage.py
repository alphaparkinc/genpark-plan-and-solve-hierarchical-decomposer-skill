from client import PlanAndSolveDecomposer

planner = PlanAndSolveDecomposer()
plan = planner.generate_plan("Audit and consolidate Q3 foreign currency hedging risks")
print(f"Generated {len(plan)} subtasks:")
for tid, desc in plan:
    print(f"  - [{tid}] {desc}")

while planner.plan:
    tid, res = planner.execute_next(lambda t_id, desc, comp: f"Done: {desc}")
    print(f"Executed: {tid} -> {res}")
