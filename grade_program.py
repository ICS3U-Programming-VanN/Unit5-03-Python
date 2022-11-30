#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: November 25, 2022
# This program asks the user for their level
# and then displays the middle percentage mark to the user


# This function finds the middle mark percentage of a level and returns it
def calc_mark(level):
    # Declared Variable
    mark = 0

    # Finds the mark value of the inputted level
    match level:
        case "4++":
            mark = 99
        case "4+":
            mark = 96
        case "4":
            mark = 90
        case "4-":
            mark = 84
        case "3+":
            mark = 78
        case "3":
            mark = 74
        case "3-":
            mark = 71
        case "2+":
            mark = 68
        case "2":
            mark = 64
        case "2-":
            mark = 61
        case "1+":
            mark = 58
        case "1":
            mark = 54
        case "-1":
            mark = 51
        case _:
            mark = 0

    # Returns mark value to main()
    return mark


def main():
    # Asks user for their level
    user_level = input("Enter the level you'd like to convert to percentage: ")

    # Calls function to find the mark of the level
    user_mark = calc_mark(user_level)

    # If the user did not enter a valid input
    if user_mark == 0:
        print(f"{user_level} is not valid input!")
    else:
        # Displays their mark
        print(
            f"Your level {user_level} has a middle percentage mark of "
            + str(user_mark)
            + "%."
        )


if __name__ == "__main__":
    main()
