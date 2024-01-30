user_input = input("Anna numero: \n")
inputs = []

while user_input != "":
    inputs.append(user_input)
    user_input = input("Anna numero: \n")

inputs.sort(reverse=True)
print(inputs)