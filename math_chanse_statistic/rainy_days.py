import random

n = int(input("Enter outside iterations: "))
m = int(input("Enter inside iterations: "))
goal_percent = float(input("Enter possibility %: "))

dictionary = {}

for _ in range(n):
    result = 0
    for _ in range(m):
        randon_number = random.randint(1, 100 * 1000)
        if randon_number in range(1, (int(goal_percent * 1000)) + 1):
            result += 1

    if result not in dictionary:
        dictionary[result] = 1
    else:
        dictionary[result] += 1

sorted_d = dict(sorted(dictionary.items(), key=lambda kvp: (-kvp[1], kvp[0])))

counter = 0
for (key, value) in sorted_d.items():
    counter += 1
    print(f"#{counter:_} Wins: {key:02} || Times: {value:_} | {(value / n * 100):.2f} %")

print(f"{'-' * 113}")
print(f"About possibility [{goal_percent}] % from [{m}] total set: ")
print(f"Max wins: {max(sorted_d.keys())} || Min wins: {min(sorted_d.keys())}")
print(f"{'-' * 113}")
