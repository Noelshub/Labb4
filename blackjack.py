import random

def cards():
    list = ["jack", "queen", "king"]
    randomw = random.randint(2, 13)
    randomw_value = 0

    if randomw == 11:
        randomw_value = 10
        randomw = list[0]
    elif randomw == 12:
        randomw_value = 10
        randomw = list[1]
    elif randomw == 13:
        randomw_value = 10
        randomw = list[2]
    else:
        randomw_value += randomw 
    return randomw_value, randomw


def spelaren():
    spelarens_sum = 0
    while True:
        kort, kortc = cards()
        spela = input("Vill du dra eller stanna?(dra/stanna)")
        if spela == "dra":
            spelarens_sum += kort
            if spelarens_sum > 21:
                print(f"du gick över 21 och hade {spelarens_sum} poäng och förlorade!")
                exit()
            print(f"du fick {kortc} och har {spelarens_sum} poäng")
            
        elif spela == "stanna":
            print(f"du stannade med {spelarens_sum} poäng")
            break

spelaren()
