def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value
            else:
                print("Enter a positive number bro.")

        except ValueError:
            print("Enter a valid number bro.")


def get_name(prompt):
    while True:
        name = input(prompt)

        if name and name.replace(" ", "").isalpha():
            return name
        else:
            print("Enter a valid name bro.")