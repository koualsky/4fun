"""
CEL:
Napisz w Pythonie 3.7, z wykorzystaniem typów funkcję określającą, czy podany 
rok jest rokiem przestępnym zgodnie z kalendarzem Gregoriańskim. Napisz 
podstawowe testy dla takiej funkcji przy użyciu pytest. 
(Podaj link do repozytorium)
"""


def lapyear(year):
    """Function return True if year is greater than 5"""

    if year > 5:
        return True
    else:
        return False
