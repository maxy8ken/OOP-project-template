# Data Dictionary

This table summarises key variables used across the object oriented roster project. The dictionary notes the intended data type, any expected format or validation and gives example values.

| Variable              | Data Type           | Format / Constraints           | Description                                         | Example                  |
|-----------------------|---------------------|--------------------------------|-----------------------------------------------------|--------------------------|
| `name`                | `str`               | non-empty                      | identifier inherited by most classes                | `"Alice"`                |
| `contact_info`        | `str`               | email or phone string          | how to contact a `Person`/`Employee`                | `"alice@example.com"`    |
| `hours_worked`        | `float` or `int`    | >= 0                           | number of hours an employee has worked              | `38.5`                   |
| `pay_rate`            | `float`             | >= 0                           | hourly rate of pay for an employee                  | `27.50`                  |
| `qualifications`      | `list[str]`         | may be empty                   | skills or certificates an employee holds            | `["First Aid", "RSA"]`   |
| `employees_managed`   | `list[Employee]`    | may be empty                   | employees supervised by a manager                   | `[emp1, emp2]`           |
| `day`                 | `str`               | week day (e.g. "Mon")          | day of a shift                                      | `"Mon"`                  |
| `start_time`          | `str`               | HH:MM                          | beginning of a shift                                | `"09:00"`                |
| `end_time`            | `str`               | HH:MM                          | end of a shift                                      | `"17:00"`                |
| `required_qualifications` | `list[str]`     | may be empty                   | qualifications required to take the shift           | `["First Aid"]`          |
| `assigned_employee`   | `Employee` or `None`| optional                       | employee currently assigned to the shift            | `None`                   |
| `shifts`              | `list[Shift]`       | may be empty                   | list of shifts on a roster                          | `[shift1, shift2]`       |
| `employees`           | `list[Employee]`    | may be empty                   | employees available in a roster                     | `[emp1, emp2]`           |
