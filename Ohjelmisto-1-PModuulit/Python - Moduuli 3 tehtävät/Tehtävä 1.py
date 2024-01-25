pituus = float(input("Mikä on kuhan pituus?\n"))

if pituus >= 37:
    print("Kuhan pyyntimitta ok\n")

elif pituus < 37:
    print(f"Kuhan pyyntimitta on {37 - pituus} cm liian lyhyt pyyntimitasta\n")