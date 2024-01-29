"""myrange = range(1,100)
list = []
for n in myrange:
    if n % 11 == 0:
        list.append(int(n))
print(list)"""

rangex = []
for i in range(90,0,-5):
    rangex.append(i)
print(rangex)

inrange = range(5,91,5)
print(list(inrange[::-1]))

print(list(range(90,0,-5)))