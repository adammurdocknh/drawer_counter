def print_program_info():
    print("V1 © Adam Murdock.")
    print("github: https://github.com/adammurdocknh")


# Prints visual divider for CLI
def print_div():
    print("#============#")


def count_drawer():
    # Dictionary of tuples
    # Tup[0] is # of bills
    # Tip[1] is $ of bills mult
    drawer = {
        "bill_count100": [0, 100],
        "bill_count50": [0, 50],
        "bill_count20": [0, 20],
        "bill_count10": [0, 10],
        "bill_count05": [0, 5],
        "bill_count01": [0, 1],
        "coin_count100": [0, 1],
        "coin_count50": [0, .5],
        "coin_count25": [0, .25],
        "coin_count10": [0, .1],
        "coin_count05": [0, .05],
        "coin_count01": [0, .01]
    }
    finished = False
    while finished is False:
        drawer["bill_count100"][0] = bill_loop("$100", True)
        drawer["bill_count50"][0] = bill_loop("$50", True)
        drawer["bill_count20"][0] = bill_loop("$20", True)
        drawer["bill_count10"][0] = bill_loop("$10", True)
        drawer["bill_count05"][0] = bill_loop("$5", True)
        drawer["bill_count01"][0] = bill_loop("$1", True)
        drawer["coin_count100"][0] = bill_loop("$1", False)
        drawer["coin_count50"][0] = bill_loop("$.50", False)
        drawer["coin_count25"][0] = bill_loop("$.25", False)
        drawer["coin_count10"][0] = bill_loop("$.10", False)
        drawer["coin_count05"][0] = bill_loop(".05", False)
        drawer["coin_count01"][0] = bill_loop("$.01", False)
        finished = True

    print_div()
    print("Drawer Breakdown:")
    total: float = 0.0
    i: int = 0
    for key in drawer:
        denom_total = drawer[key][0] * drawer[key][1]
        total = total + denom_total
        print(key)
        print("#", drawer[key][0])
        print("$", denom_total)

    print("Total:", total)


def bill_loop(denom_value: str, is_bill: bool):
    looping = True
    if is_bill:
        print("How many " + denom_value + " bills?")
    else:
        print("How many " + denom_value + " coins?")

    temp: str
    temp = input()
    while looping:

        # Allows the user to quit mid session
        if temp == "q" or temp == "Q":
            print("Thank you for using this script!")
            return quit()
        else:
            try:
                temp = int(temp)
                if temp >= 0:
                    looping = False
                else:
                    print("Please enter a positive integer.")
                    print("Something like 42.")
                    looping = True
            except:
                print("Please enter an integer.")
                print("Something like 42.")
                looping = True

        return int(temp)


def main():
    finished = False
    is_invalid_input = True
    print_program_info()
    print_div()
    print("Welcome to drawer_counter")
    print("Press q to quit early.")
    while not finished:
        count_drawer()
        print("Do you want to continue? Y/N")
        x = input()
        while is_invalid_input:
            if(x == "y" or x == "Y"):
                is_invalid_input = False
                finished = False
            if(x == "n" or x == "N"):
                finished = True
                is_invalid_input = False
                print("Thank you for using this script!")
                quit()

            else:
                print("Please enter Y for yes or N for no")
                finished = False
                is_invalid_input = False


main()
