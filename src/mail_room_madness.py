"""Module for creating a dictionary of donors and print a list of donors."""

import sys
from tabulate import tabulate
donors = {}


def get_user_response(prompt):  # pragma: no cover
    """Display prompt and return user response lowercased."""
    response = input(prompt)
    return response.lower()


def create_new_donor(name):
    """Function to add new donor into dictionary."""
    donors[name] = [0, 0]
    return donors


def update_donor(name, amount):
    """Function to update the amount donated and increment number of donations."""
    donors[name][0] += amount
    donors[name][1] += 1
    return donors


def create_thank_you():  # pragma: no cover
    """Create a thank you letter to specific donor with amount."""
    name = ""
    while name == "":
        name = get_user_response("Enter donor's full name, or 'list' to see all donors. 'q' to quit: ")
        if name == "list":
            for name in donors.keys():
                print(name)
            name = ""
        elif name == "q":
            main()

    if name not in donors.keys():
        create_new_donor(name)

    amount = 0
    while amount < 1:
        response = input("Enter donation amount in dollars (at least 1): ")
        if response.lower == "quit":
            main()
        else:
            amount = float(response)

    update_donor(name, amount)
    print("Thank you {name} for your very generous donation of ${amount:.2f}!".format(name=name.capitalize(), amount=amount))
    main()


def create_report_list():  # pragma: no cover
    """Function to create the list of donors and the amount donated."""
    donors_and_value_list = []
    for name in donors.keys():
        temp = list(donors[name])
        temp.append(float(temp[0]) / temp[1])
        temp.append(name.capitalize())
        donors_and_value_list.append(temp)
    return donors_and_value_list


def create_report():  # pragma: no cover
    """Print a formatted report of all donors, sorted by total amount."""
    donors_and_value_list = create_report_list()
    print('')
    print(tabulate(donors_and_value_list, headers=['Total', '# of Donations', 'Avg Donation', 'Name']))
    main()


def main():  # pragma: no cover
    """Ask the user for desired action and begin that action."""
    choice = get_user_response("Enter '1' to write a thank you letter, '2' to print a report, 'q' to stop ")

    # reprompt until a valid response is given
    while (choice != "1" and choice != "2" and choice != "q"):
        choice = get_user_response("Sorry, please enter either '1' for thank you, '2' for a report, or 'q' to stop ")
    if choice == "1":
        create_thank_you()
    elif choice == "2":
        create_report()
    elif choice == "q":
        sys.exit(0)  # quit the program


if __name__ == '__main__':  # pragma: no cover
    try:
        main()
    except KeyboardInterrupt:
        print('\nThank You')
        sys.exit()
