from math import factorial

total_games = int(input("Въведете брой мачове: "))

p_win_percent = float(input("Вероятност за победа (в проценти): "))
p_draw_percent = float(input("Вероятност за равен (в проценти): "))
p_loss_percent = float(input("Вероятност за загуба (в проценти): "))

p_win = p_win_percent / 100
p_draw = p_draw_percent / 100
p_loss = p_loss_percent / 100

dictionary = {}

for k_win in range(total_games + 1):
    for k_draw in range(total_games - k_win + 1):
        k_loss = total_games - k_win - k_draw

        numerator = factorial(total_games)
        denominator = factorial(k_win) * factorial(k_draw) * factorial(k_loss)
        coefficient = numerator / denominator

        probability = coefficient * (p_win ** k_win) * (p_draw ** k_draw) * (p_loss ** k_loss)
        dictionary[(k_win, k_draw, k_loss)] = probability

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for key, probability in sorted_dictionary.items():
    k_win, k_draw, k_loss = key
    print(f"Победи: {k_win}, Равни: {k_draw}, Загуби: {k_loss} -> Вероятност: {(probability * 100):.6f} %")
