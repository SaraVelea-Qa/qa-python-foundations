with open("data/app.log") as f:
    lines = f.read().splitlines()
   # print(lines)
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
invalid = 0

for line in lines:
    parts = line.split()
    print (f"this line: {parts} has this length {len(parts)}")
    if parts == "":
        continue
    elif len(parts) < 3:
        print(f"the length of the line is: {len(parts)}")
        invalid += 1

print(invalid)
   # elif parts[2] not in LEVELS:
    #    invalid += 1
    




    # for word in line:
    #     if word == " ":
    #         continue
    #     elseif word ==












# assert counts == {"INFO": 4, "DEBUG": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 1}, f"got {counts}"
# assert invalid == 2, f"got {invalid}"
# assert len(problems) == 4, f"got {problems}"