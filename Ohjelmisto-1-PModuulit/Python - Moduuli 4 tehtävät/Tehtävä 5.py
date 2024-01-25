käyttäjätunnus = "python".lower()
salasana = "rules".lower()
yritykset = 0

k_yritys = input("Käyttäjätunnus\n")
s_yritys = input("Salasana\n")

if (k_yritys != käyttäjätunnus) or (s_yritys != salasana):
    while yritykset < 5:
        k_yritys = input("Käyttäjätunnus\n")
        s_yritys = input("Salasana\n")
        yritykset += 1
        if yritykset == 5:
            print("Pääsy evätty")
            break

else:
    print("Tervetuloa!")