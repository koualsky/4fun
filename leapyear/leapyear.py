"""
Napisz w Pythonie 3.7, z wykorzystaniem typów funkcję określającą, czy podany 
rok jest rokiem przestępnym zgodnie z kalendarzem Gregoriańskim. Napisz 
podstawowe testy dla takiej funkcji przy użyciu pytest. 
(Podaj link do repozytorium)
"""


def leapyear(year):
    """Return True if year is a leap year"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
