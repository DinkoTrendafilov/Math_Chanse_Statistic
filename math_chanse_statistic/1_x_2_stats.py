from math import factorial, comb

total_games = int(input("Въведете брой мачове: "))
p_win = float(input("Вероятност за победа (в проценти): ")) / 100
p_draw = float(input("Вероятност за равен (в проценти): ")) / 100
p_loss = float(input("Вероятност за загуба (в проценти): ")) / 100

all_probabilities = {}

for k_win in range(total_games + 1):
    for k_draw in range(total_games - k_win + 1):
        k_loss = total_games - k_win - k_draw

        total_factorial = factorial(total_games)
        k_win_factorial = factorial(k_win)
        k_draw_factorial = factorial(k_draw)
        k_loss_factorial = factorial(k_loss)

        probability_result = (
                (total_factorial / (k_win_factorial * k_draw_factorial * k_loss_factorial)) *
                (p_win ** k_win) * (p_draw ** k_draw) * (p_loss ** k_loss)
        )

        all_probabilities[(k_win, k_draw, k_loss)] = probability_result

sorted_all_probabilities = dict(sorted(all_probabilities.items(), key=lambda kvp: (-kvp[1], kvp[0])))

counter = 0
for result, prob in sorted_all_probabilities.items():
    counter += 1
    k_win, k_draw, k_loss = result
    print(f"#{counter} Победи: {k_win}, Равни: {k_draw}, Загуби: {k_loss} -> Вероятност: {(prob * 100):.5f} %")

