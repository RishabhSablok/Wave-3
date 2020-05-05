def prime():
    if __name__ =="__main__":
        a = False
        number = int(input("Input the number (Greater than 1): "))
        counter = 2
        while counter < number:
            if number % counter == 0:
                return False
                break
            counter += 1
        else:
            return True
# Should i call the function?
# print(prime())