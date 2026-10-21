# Task 7: Monkey & Banana Problem using Goal Stack Planning

def goal_stack_planning():
    state = {("AT", "Monkey", "Door"), ("AT", "Box", "Window"), ("AT", "Banana", "Middle"), ("ON", "Monkey", "Floor")}
    stack = [("HAS", "Monkey", "Banana")]
    plan = []
    while stack:
        curr = stack.pop()
        if curr[0] == "OP":
            op, args = curr[1], curr[2]
            plan.append(f"{op}({', '.join(args)})")
        elif curr in state:
            continue
        elif curr == ("HAS", "Monkey", "Banana"):
            stack += [("OP", "GRASP", ("Middle",)), ("ON", "Monkey", "Box"), ("AT", "Box", "Middle")]
        elif curr == ("ON", "Monkey", "Box"):
            stack += [("OP", "CLIMB", ("Middle",)), ("AT", "Monkey", "Middle")]
        elif curr == ("AT", "Box", "Middle"):
            stack += [("OP", "PUSH", ("Window", "Middle")), ("AT", "Monkey", "Window")]
        elif curr == ("AT", "Monkey", "Window"):
            stack += [("OP", "GOTO", ("Door", "Window"))]
    return plan

print("Generated Action Plan:")
for i, step in enumerate(goal_stack_planning(), 1):
    print(f"Step {i}: {step}")

# Output:
# Generated Action Plan:
# Step 1: GOTO(Door, Window)
# Step 2: PUSH(Window, Middle)
# Step 3: CLIMB(Middle)
# Step 4: GRASP(Middle)
