# part 4
def validation():
    while True:
        n = input("enter name: ")

        if n and n.replace(" ", "").isalpha():
            return n
        else:
            print("Bro, enter a valid name.")
r = validation()
