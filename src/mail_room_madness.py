"""."""


from tabulate import tabulate



def create_report(donors):
    """Print a formatted report of all donors, sorted by total amount.
    For each donor in donors:
        add up total donations for total
        calculate average donations amount
    sort donors based on total donation amount
    print the formatted report in order
    main() # to return to original prompt"""
    donors_and_value_list = []
    for name in donors.keys():
        temp = list(donors[name])
        temp.append(temp[0] // temp[1])
        temp.append(name.capitalize())
        donors_and_value_list.append(temp)
    print('')
    print(tabulate(donors_and_value_list, headers=['Total', '# of Donations', 'Avg Donation','Name']))

create_report(donors)
