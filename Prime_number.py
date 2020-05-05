def prime(number):
    if __name__ =="__main__":
        a = False
        counter = 2
        while counter < number:
            if number % counter == 0:
                return False
                break
            counter += 1
        else:
            return True
a = int(input("Input the number (Greater than 1): "))
if prime(a):
    print("The number is a prime number")

else:
    print("The number is a not a prime number")
