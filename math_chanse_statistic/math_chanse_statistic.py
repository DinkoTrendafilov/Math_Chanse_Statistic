from math import comb

n = int(input("Enter total numbers: "))
m = int(input("Enter needed count of numbers: "))

print(f"{'-' * 113}")
for num in range(m + 1):
    res = comb(m, m - num) * comb(n - m, m - num)
    print(
        f"Chanse to find: {num} from: {m} || {(comb(m, m - num)):_} X {(comb(n - m, m - num)):_} "
        f" =  {res:_} -> [{(comb(n, m)):_}]  =  {(comb(m, m - num) * comb(n - m, m - num) / comb(n, m)) * 100} %")

print(f"{'-' * 113}")
