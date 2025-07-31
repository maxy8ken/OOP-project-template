# Programming Practices in Rostering Tool Project

This document outlines the good programming practices used in the development of the **Rostering Tool Project**, supported by descriptions and code snippets.

---

## 1. Clear and Uncluttered Mainline

**Description:**
The `main.py` file serves as a high-level controller, delegating logic to separate modules and maintaining a clean structure.

**Why:**
Helps improve readability, testing, and modularity.

```python
from scheduler import Scheduler
from data_loader import load_employees
from display import print_schedule

employees = load_employees("data/employees.csv")
scheduler = Scheduler(employees)
schedule = scheduler.create_weekly_roster()
print_schedule(schedule)
```

---

## 2. One Logical Task per Subroutine

**Description:**
Each function performs a single, well-defined task (e.g., availability check or shift assignment).

**Why:**
Improves modularity, reuse, and ease of debugging.

```python
def check_availability(employee, day):
    return day not in employee.unavailable_days

def assign_shift(employee, shift):
    employee.assigned_shifts.append(shift)
```

---

## 3. Use of Stubs

**Description:**
Stub functions were used during early development to simulate yet-to-be-implemented logic.

**Why:**
Allows testing and development of the main structure before full implementation.

```python
def generate_optimised_schedule():
    # TODO: Replace with real scheduling algorithm
    return []
```

---

## 4. Use of Control Structures and Data Structures

**Description:**
Effective use of loops, conditionals, and core data structures like lists, dictionaries, and custom classes.

**Why:**
Allows efficient handling of complex scheduling logic.

```python
for employee in employees:
    for day in week_days:
        if check_availability(employee, day):
            assign_shift(employee, day)

shift_roster = {
    "Monday": [],
    "Tuesday": [],
    # ...
}
```

---

## 5. Ease of Maintenance

**Description:**
The codebase is structured into clear modules with descriptive naming and inline comments.

**Why:**
Makes the system easy to understand, update, or extend in the future.

```python
# data_loader.py
def load_employees(file_path):
    """Reads employee data from CSV and returns list of Employee objects."""
    # ...
```

---

## 6. Version Control

**Description:**
Git was used to track changes and manage feature development.

**Why:**
Enables rollback, collaboration, and progress tracking.

**Example Git Log:**
```
commit 3e9a8d2 - Implement shift assignment logic
commit b41ef21 - Add employee availability checker
commit a81cf01 - Setup project structure and stubs
```

---

## 7. Regular Backups

**Description:**
The project was regularly backed up to GitHub and cloud storage.

**Why:**
Prevents data loss and supports access across devices.

**Example:**
- GitHub repository regularly pushed
- Weekly ZIP backups stored in Google Drive

---

Feel free to replace code snippets or logs with actual screenshots for assessment documentation.
