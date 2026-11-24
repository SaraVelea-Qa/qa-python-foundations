results = [
    ("login", "PASS", 1.2),
    ("search", "FAIL", 3.4),
    ("cart", "PASS", 0.8),
    ("checkout", "SKIP", 0.0),
    ("profile", "FAIL", 2.1),
]

# 1. Is there at least one FAIL?
has_failures = any(status == "FAIL" for _, status, _ in results)
assert has_failures is True, f"1: got {has_failures}"

# 2. Did every test take less than 5.0 seconds?
all_fast = all(duration < 5.0 for _, _, duration in results)
assert all_fast is True, f"2: got {all_fast}"

# 3. Did every test PASS?
all_passed = all(status == "PASS" for _, status, _ in results)
assert all_passed is False, f"3: got {all_passed}"

# 4. Is it true that there are NO skipped tests? (use `not` + any)
no_skips = not any(status == "SKIP" for _, status, _ in results)
assert no_skips is False, f"4: got {no_skips}"

# 5. The empty-list trap: the API returned no responses at all
responses = []
naive_ok = all(code == 200 for code in responses)
assert naive_ok is True, "5: all() on an empty list is True"  # this passes, and that's the problem

# 6. A safe version: must be False when there are no responses.
#    It must be a real bool (True/False), not [] or 0.
safe_ok = len(responses) > 0 and all(code == 200 for code in responses)
assert safe_ok is False, f"6: got {safe_ok!r}"

print("All 6 passed!")
