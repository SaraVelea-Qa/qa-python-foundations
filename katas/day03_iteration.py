results = [
    ("login", "PASS", 1.2),
    ("search", "FAIL", 3.4),
    ("cart", "PASS", 0.8),
    ("checkout", "SKIP", 0.0),
    ("profile", "FAIL", 2.1),
]

# 1. Names sorted by duration, fastest first (sorted + key + comprehension)
by_speed = [name for name, _, _ in sorted(results, key=lambda r: r[2])]
assert by_speed == ["checkout", "cart", "login", "profile", "search"], f"1: got {by_speed}"

# 2. Name of the slowest test (max + key, then take the name)
slowest = max(results, key=lambda r: r[2])[0]
assert slowest == "search", f"2: got {slowest}"

# 3. Numbered report lines, starting at 1 (enumerate + f-string + comprehension)
report = [f"{i}. {name}: {status}" for i, (name, status, _) in enumerate(results, start=1)]
assert report == [
    "1. login: PASS",
    "2. search: FAIL",
    "3. cart: PASS",
    "4. checkout: SKIP",
    "5. profile: FAIL",
], f"3: got {report}"

# 4. Names where expected status != actual status (zip with strict=True)
expected = ["PASS", "PASS", "PASS", "SKIP", "PASS"]
mismatches = [
    name
    for (name, actual_status, _), expected_status in zip(results, expected, strict=True)
    if actual_status != expected_status
]
assert mismatches == ["search", "profile"], f"4: got {mismatches}"

# 5. Names sorted by status, then by name (key returns a tuple)
by_status = [name for name, _, _ in sorted(results, key=lambda r: (r[1], r[0]))]
assert by_status == ["profile", "search", "cart", "login", "checkout"], f"5: got {by_status}"

print("All 5 passed!")
