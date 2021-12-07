import numpy as np
file = open("input.txt")
# file = open("test.txt")
#file = open("test_col.txt")

bombo = file.readline().rstrip().split(",")
file.readline()
carton_list = []
carton = []

for line in file:
    preprocess = ' '.join(line.rstrip().split())
    if(preprocess != ''):
        carton.append(preprocess.split(" "))
    if (len(carton) == 5):
        carton_list.append(carton)
        carton = []
file.close()

def any_winner(list_of_cartons):
    winners = []
    for idx, card in enumerate(list_of_cartons):
        card_np = np.array(card)
        for i in range(len(card)):
            row = card_np[i]
            res = all(ele == '-1' for ele in row)
            if (res):
                winners.append(idx)
            col = card_np[:,i]
            res = all(ele == '-1' for ele in col)
            if (res):
                winners.append(idx)
    return len(winners) != 0, list(set(winners))

def check_new_number(number_to_check, list_of_cards):
    for player in list_of_cards:
        for line in player:
            if number_to_check in line:
                line[line.index(number)] = -1
    return list_of_cards

for number in bombo:
    carton_list = check_new_number(number, carton_list)

    res, winners_list = any_winner(carton_list)
    print(f"Number: {number}")
    print(f"Winners: {winners_list}, Res: {res}")
    print(f"Total players: {len(carton_list)}")
    if(len(carton_list) == 1 and res):
        print("THERE IS A LEAST WINNER")
        print(carton_list, res)
        total = [[int(x) for x in j if x != -1] for j in carton_list[0]]
        flat_list = sum([item for sublist in total for item in sublist])
        print(int(flat_list) * int(number))
        break
    if len(winners_list) != 0:
        for winner in sorted(winners_list, reverse=True):
            print(f"Winner: {winner}")
            carton_list.pop(winner)
# for card in carton_list:
#     print(card)