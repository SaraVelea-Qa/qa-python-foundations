import math

results = [
    ("login", "PASS", 1.2),
    ("search", "FAIL", 3.4),
    ("cart", "PASS", 0.8),
    ("checkout", "SKIP", 0.0),
    ("profile", "FAIL", 2.1),
]

# 1. List of all test names
names = [name for name, _, _ in results]
assert names == ["login", "search", "cart", "checkout", "profile"], f"1: got {names}"

# 2. List of names of FAILED tests
failed = [name for name, status, _ in results if status == "FAIL"]
assert failed == ["search", "profile"], f"2: got {failed}"

# 3. Dict: name -> status
status_by_name = {name: status for name, status, _1 in results}
assert status_by_name == {
    "login": "PASS",
    "search": "FAIL",
    "cart": "PASS",
    "checkout": "SKIP",
    "profile": "FAIL",
}, f"3: got {status_by_name}"

# 4. Set of all distinct statuses
statuses = {status for _, status, _ in results}
assert statuses == {"PASS", "FAIL", "SKIP"}, f"4: got {statuses}"

# 5. Squares of the EVEN numbers from range(10)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
assert even_squares == [0, 4, 16, 36, 64], f"5: got {even_squares}"

# 6. Dict: name -> duration, only for tests slower than 1.0 seconds
slow = {name: duration for name, _, duration in results if duration > 1.0}
assert slow == {"login": 1.2, "search": 3.4, "profile": 2.1}, f"6: got {slow}"

# 7. Names longer than 5 characters, in UPPERCASE
long_upper = [name.upper() for name, status, _ in results if len(name) > 5]
assert long_upper == ["SEARCH", "CHECKOUT", "PROFILE"], f"7: got {long_upper}"

# 8. A label for EVERY test: "OK" if PASS, otherwise "NOT OK"
labels = ["OK" if status == "PASS" else "NOT OK" for _, status, _ in results]
assert labels == ["OK", "NOT OK", "OK", "NOT OK", "NOT OK"], f"8: got {labels}"

# 9. Total duration of PASSED tests (use sum + generator; compare floats correctly)
passed_time = sum(duration for _, status, duration in results if status == "PASS")
assert math.isclose(passed_time, 2.0), f"9: got {passed_time}"

# 10. Number of FAILED tests (without using `failed` from #2)
fail_count = len([status for _, status, _ in results if status == "FAIL"])
assert fail_count == 2, f"10: got {fail_count}"

print("All 10 passed!")
