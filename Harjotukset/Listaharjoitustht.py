"""items = [1,3,4,5,6,9,10,17,23,24]
result = []

for i in items:
    if i % 2 != 0:
        result.append(i)

print(result)"""

probability = [0.52, 0.49, 0.72, 0.81, 0.12, 0.11]
results = []

for p in probability:
    if p >= 0.5:
        results.append(1)
    else:
        results.append(0)
print(results)