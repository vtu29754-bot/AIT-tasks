# Task 6: Exam Time Table using CSP

def solve_timetable():
    exams = ["CS101", "CS102", "MATH201", "PHY101", "CHEM101"]
    slots = ["Slot 1", "Slot 2", "Slot 3"]
    conflicts = {
        "CS101": ["CS102", "MATH201", "PHY101"],
        "CS102": ["CS101", "PHY101"],
        "MATH201": ["CS101", "PHY101", "CHEM101"],
        "PHY101": ["CS101", "CS102", "MATH201"],
        "CHEM101": ["MATH201"]
    }
    assign = {}
    def backtrack():
        if len(assign) == len(exams): return assign
        var = [e for e in exams if e not in assign][0]
        for s in slots:
            if all(assign.get(c) != s for c in conflicts.get(var, [])):
                assign[var] = s
                if backtrack(): return assign
                del assign[var]
        return None
    return backtrack()

sched = solve_timetable()
for exam, slot in sorted(sched.items()):
    print(f"{exam}: {slot}")

# Output:
# CHEM101: Slot 1
# CS101: Slot 1
# CS102: Slot 2
# MATH201: Slot 2
# PHY101: Slot 3
