with open("data/app.log") as f:
    lines = f.read().splitlines()
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
invalid = 0
counts = {}
problems = []


for number, line in enumerate(lines, start = 1):
    parts = line.split()
    if not parts:
        continue
    elif len(parts) < 3 or parts[2] not in LEVELS:
        invalid += 1
    else:
        level = parts[2]
        counts[level] = counts.get(level, 0) + 1
        if level in {"ERROR", "CRITICAL"}:
            message = " ".join(parts[3:])
            problems.append(f"line {number}: {message}")
assert counts == {"INFO": 4, "DEBUG": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 1}, f"got {counts}"
assert invalid == 2, f"got {invalid}"
assert len(problems) == 4, f"got {problems}"

for level, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
    print(f"{level}: {count}")  

print(f"Invalid lines: {invalid}")
print(f"Has errors: {any("ERROR" for level in counts)}")
print(f"Problems: {problems.split()}")
