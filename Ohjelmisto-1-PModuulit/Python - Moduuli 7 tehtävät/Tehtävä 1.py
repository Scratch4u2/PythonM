vuodenajat = ("talvi","talvi", "kevat","kevat","kevat", "kesa","kesa","kesa", "syksy","syksy","syksy","talvi")
vuodenaika_numero = int(input("Kuukauden numero: \n"))

vuodenaika = vuodenajat[vuodenaika_numero-1]
print(f"{vuodenaika_numero} vuodenaika on {vuodenaika}")