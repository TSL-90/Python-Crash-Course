"""Test for the name_funtion.py"""

from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Wolfgang Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart')
    assert formatted_name == 'Wolfgang Mozart'


def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
