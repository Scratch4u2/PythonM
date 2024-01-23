import random

#rand_i = random.randint(1,2)
#print(f"Arvottu numero {rand_i}")


import random

player_count = 6 #int(input("Montako pelaajaa: \n"))
dicecount = 1 #int(input("Montako noppaa: \n"))

current_player = 1

best_player = None
best_score = 0

while current_player <= player_count:
    result = 0
    throw_count = 1
    remaining_dice = dicecount

    while remaining_dice > 0:
        die_result = random.randint(1, 6)
        print(f"Pelaajan {current_player}, {throw_count}. heiton tulos: {die_result}")
        result += die_result
        throw_count += 1
        remaining_dice -= 1
    if result > best_score:
        best_score = result
        best_player = f"{current_player}"
    elif result == best_score:
        best_player = best_player + f" ja pelaaja {current_player}"
    print(f"Pelaajan {current_player} tulos on: {result}")
    current_player += 1

print(f"Paras pelaaja on {best_player} tulos oli: {best_score}")


#break-komento: heittää ulos aktiivisesta silmukasta
counter = 0
while True
    print(f"Laskuri 1:{counter}")
    counter += 1
    if counter == 5:
        break
    print(f"Laskuri 2:{counter}")