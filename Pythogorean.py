def triangle(side1, side2):
    side3 = (side1 ** 2 + side2 ** 2) ** 0.5
    return side3

x = float(input("Input the side 1: "))
y = float(input("Input the side 2: "))
print("The hypotenouse is",triangle(x,y), "units long")