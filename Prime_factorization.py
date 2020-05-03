user_input = int(input("Enter a number greater than 2: "))
factor = 2
print("The factors of", user_input, "are: ")
while factor <= user_input:
    if user_input % factor == 0:
        print(factor)
        user_input //= factor
    else:
        factor += 1
