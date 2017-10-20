"""."""

import sys
from tabulate import tabulate
donors = {}


def get_user_response(prompt):
    """Display prompt and returns user response lowercased."""
    response = input(prompt)
    return response.lower()


def create_thank_you():
    """Create a thank you letter to specific donor with amount."""
    name = ""
    while name == "":
        name = get_user_response("Enter donor's full name, or list to see all donors ")
        print(name)
        if name == "list":
            for name in donors.keys():
                print(name)
        elif name == "quit":
            main()

    if name not in donors.keys():
        donors[name] = [0, 0]

    amount = 0
    while amount < 1:
        response = input("Enter donation amount in dollars (at least 1) ")
        if response.lower == "quit":
            main()
        else:
            amount = int(response)

    donors[name][0] += amount
    donors[name][1] += 1
    #print("Thank you " + name + " for your very generous donation of $ " + amount)
    print(donors)
    main()



def create_report(donors):
    """Print a formatted report of all donors, sorted by total amount."""
    donors_and_value_list = []
    for name in donors.keys():
        temp = list(donors[name])
        temp.append(temp[0] // temp[1])
        temp.append(name.capitalize())
        donors_and_value_list.append(temp)
    print('')
    print(tabulate(donors_and_value_list, headers=['Total', '# of Donations', 'Avg Donation','Name']))
    main()

def main():
    """Ask the user for desired action and begin that action."""
    choice = get_user_response("Thank you or Print Report? (stop to quit)")

    # reprompt until a valid response is given
    while (choice != "thank you" and choice != "print report" and choice != "quit"):
        choice = get_user_response("Sorry, please type either \"Create thank you\", \"Print report\", or \"quit")

    if choice == "thank you":
        create_thank_you()
    elif choice == "print report":
        create_report(donors)
    elif choice == "quit":
        sys.exit(0)  # quit the program

main()
