from math import comb

n = int(input("Enter total numbers: "))
goal_possibility = float(input("Enter possibility %: "))

win_coef = goal_possibility / 100
losses_coef = (100 - goal_possibility) / 100

print(f"{'-' * 113}")
for num in range(n + 1):
    result = comb(n, num) * (win_coef ** num) * (losses_coef ** (n - num))
    print(f"Goal matches: {num} | Combinations: {comb(n, num)} | Result: {(result * 100):.2f} %")
print(f"{'-' * 113}")
