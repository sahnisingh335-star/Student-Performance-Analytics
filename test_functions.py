
from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    calculate_result
)

marks = [80, 70, 90, 60, 100]

assert calculate_total(marks) == 400
assert calculate_average(marks) == 80
assert calculate_grade(93) == "A+"
assert calculate_result(33) == "Fail"
assert calculate_result(40) == "Pass"

print("All tests passed!")
