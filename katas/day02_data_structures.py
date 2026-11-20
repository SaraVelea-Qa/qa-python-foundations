import copy

results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL", "PASS"]
names = ["login", "cart", "login", "search", "cart", "logout"]
config = {"base_url": "https://staging.shop.test", "browsers": ["chromium"]}

# 1. Number of results
total = len(results)
assert total == 6

# 2. The first result, using an index
first = results[0]
assert first == "PASS"

# 3. The last result, using a NEGATIVE index
last = results[-1]
assert last == "PASS"

# 4. The first three results, using a slice
first_three = results[0:3]
assert first_three == ["PASS", "FAIL", "PASS"]

# 5. Is there at least one "SKIP"? (True/False, use `in`)
has_skip = "SKIP" in results
assert has_skip is True

# 6. The unique statuses (use a set)
statuses = set(results)
assert statuses == {"PASS", "FAIL", "SKIP"}

# 7. Are there duplicate test names? (compare a len with the len of a set)
has_duplicates = len(names) != len(set(names))
assert has_duplicates is True

# 8. Read "timeout" from config. It's missing, so default to 30.
timeout = config.get("timeout", 30)
assert timeout == 30

# 9. Make an independent copy of config, then add "firefox" to the COPY's browsers.
#    The original config must still have only ["chromium"].
staging_config = copy.deepcopy(config)
staging_config["browsers"].append("firefox")
assert staging_config["browsers"] == ["chromium", "firefox"]
assert config["browsers"] == ["chromium"]

# 10. The results in reverse order
reversed_results = results[::-1]
assert reversed_results == ["PASS", "FAIL", "SKIP", "PASS", "FAIL", "PASS"]

print("All 10 passed!")
