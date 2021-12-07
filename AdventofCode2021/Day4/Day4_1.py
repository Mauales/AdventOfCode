import numpy as np
file = open("input.txt")
#file = open("test.txt")
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
    for idx, card in enumerate(list_of_cartons):
        res = False
        card_np = np.array(card)
        for i in range(len(card)):
            row = card_np[i]
            res = all(ele == '-1' for ele in row)
            if (res):
                return res, idx
            col = card_np[:,i]
            res = all(ele == '-1' for ele in col)
            if (res):
                return res, idx
    return res, -1

for number in bombo:
    for player in carton_list:
        for line in player:
            if number in line:
                line[line.index(number)] = -1

    end, winner = any_winner(carton_list)

    if(end):
        print("THERE IS A WINNER")
        print(carton_list[winner])
        total = [[int(x) for x in j if x != -1] for j in carton_list[winner]]
        flat_list = sum([item for sublist in total for item in sublist])
        print(int(flat_list) * int(number))
        break

# for card in carton_list:
#     print(card)