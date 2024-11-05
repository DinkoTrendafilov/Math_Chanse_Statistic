from math import comb

total_matches = int(input("Enter total matches: "))
match_possibility = float(input("Enter match possibility %: "))

win_coef = match_possibility / 100
losses_coef = (100 - match_possibility) / 100
total_combinations = 0

print(f"{'-' * 113}")
for match in range(total_matches + 1):
    total_combinations += comb(total_matches, match)
    result = comb(total_matches, match) * (win_coef ** match) * (losses_coef ** (total_matches - match))
    print(f"Matches: {match:_} -- Total matches: {total_matches} "
          f"|| Combinations: {(comb(total_matches, match)):_} ---> Result: {(result * 100):.5f} %")
print(f"Total combinations: {total_combinations:_}")
print(f"{'-' * 113}")
print(total_combinations)
print(len(str(total_combinations)))
