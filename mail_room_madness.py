"""This is pseudo code for mail room madness assignment, finished product will
be pseudo code functions and a flow chart"""


# Dictionary with donors and amounts they have donated
donors = {donors name: amount donated}


def get_user_input(prompt, validator=None):
    """return the value input by a user prompted by `prompt`

    optionally, validate the input with a function `validator` which must
    take one argument, the input from the user and must return the input if
    valid, and None if not valid
    """
    reply = None
    while reply is None:
        reply = ask_for_input(prompt)
        if there_is_a_validator:
            validate_the_reply
    return reply


def thank_you_function():
    """
    

    """

    prompt for name of donor
    thank_you_prompt()

    if prompt is 'list':
        return list of donor names and reprompt for name of donor


    elif name is not in donor Dictionary  
        add name to Dictionary
        prompt_for_amount()

    else:
        get name from Dictionary and prompt_for_amount()



def prompt_for_amount():
    """."""
    ask for amount of donation
    verify that it is a number
    add value to donor in dictionary
    
    send_email()

def send_email():
    """"."""
    compose and print an email to send to donor


def create_report()
    """."""

    
    # check to see if donor and value is in dict
    # 

def main():
    """
    1. get user prompt
    
    """

    prompt = 'Send a Thank You or Create a Report'
    get_user_input(prompt)

    if get_user_input == 'Thank You':

        thank_you_function()

    elif get_user_input == 'Create Report':

        create_report_function()

    else:
        quit




