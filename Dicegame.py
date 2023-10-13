import random


def kasta_tarningen():
    dice = random.randint(1, 6)
    return dice


def spelarens_kast():
    spelarens_poang = 0
    spelarens_kastc = 0
    while True:
        spelarens_kasts = kasta_tarningen()
        spela = input("Vill du kasta eller stanna? ja/nej ")
        if spela == "ja":
            print(f"du kastade {spelarens_kasts}")
            spelarens_poang += spelarens_kasts
            spelarens_kastc += 1
            print(
                f"dina poäng är {spelarens_poang} och du har kastat {spelarens_kastc} gånger")
        elif spelarens_poang > 21:
            print("du förlorade!")
            break
        if spela == "nej":
            print("du stannade")
            break
    return spelarens_poang


def dealerns_kast():
    dealerns_sum = 0
    dealerns_kast = 0
    while dealerns_sum < 17:
        dealerns_kasts = kasta_tarningen()
        print(f"dealern kastade {dealerns_kasts}")
        dealerns_sum += dealerns_kasts
        dealerns_kast += 1
        print(
            f"dealerns poäng {dealerns_sum} och dealern har kastat {dealerns_kast} gånger")
        if dealerns_sum > 21:
            print("dealern förlorade!")
            break
    return dealerns_sum


def avgora_vinnaren(spelarens_poang, dealerns_sum):
    if spelarens_poang > dealerns_sum:
        print(
            f"Grattis du vann och hade {spelarens_poang} poäng och dealern fick {dealerns_sum} poäng")
    elif spelarens_poang < dealerns_sum:
        print(
            f"Dealern vann! Och hade {dealerns_sum} poäng och du fick {spelarens_poang} poäng")
    elif spelarens_poang == dealerns_sum:
        print(
            f"Du fick lika mycket poäng som dealern, Du fick {spelarens_poang} poäng och dealern fick {dealerns_sum} poäng")


def spela_igen():
    while True:
        k = input("Vill du spela igen? ja/nej ")
        if k == "ja":
            main()
        else:
            break


def main():
    spelarens_poang = spelarens_kast()
    dealerns_sum = dealerns_kast()
    avgora_vinnaren(spelarens_poang, dealerns_sum)
    spela_igen()


main()
