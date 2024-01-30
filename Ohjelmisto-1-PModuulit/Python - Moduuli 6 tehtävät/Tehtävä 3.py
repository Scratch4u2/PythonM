def lasku(m_gallona):
    while m_gallona >= 0:
        litroina = m_gallona * 3.785
        print(f"{litroina} litraa")
        m_gallona = int(input("Montako gallonaa: \n"))

m_gallona = int(input("Montako gallonaa: \n"))
lasku(m_gallona)