"""Test for the name_funtion.py"""

from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Tyson Lanier' work?"""
    formatted_name = get_formatted_name('tyson', 'lanier')
    assert formatted_name == 'Tyson Lanier'
