def on_alkuluku(numero):
    if numero <= 1:
        return False
    elif numero % numero != 0 or numero % 1 != 0:
        return False
    else:
        return True

u_input = int(input("Anna numero: \n"))

if on_alkuluku(u_input):
    print(f"{u_input} on alkuluku")
else:
    print(f"{u_input} ei ole alkuluku")