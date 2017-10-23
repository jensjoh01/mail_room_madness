"""Module to test mail_room_madness."""


donors = {}
test_dict_1 = {'John': [0, 0]}
test_dict_2 = {'John': [1000, 1]}


def test_create_new_donor():
    """Function to test the create_new_donor function and compare
    to a known dictionary."""
    from mail_room_madness import create_new_donor
    assert create_new_donor('John') == test_dict_1


def test_update_donors():
    """Function to test update_donor function."""
    from mail_room_madness import update_donor
    assert update_donor('John', 1000) == test_dict_2
