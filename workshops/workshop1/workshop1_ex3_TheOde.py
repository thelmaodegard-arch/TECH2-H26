# My solution for exercise 3

import numpy as np

def tax(income):
    """
    Return the taxes owed for a given income.

    Paramteres
    ----------

    Income
        Gross income

    Returns
    -------

    Tax owed

    """
    if income <= 300000:
        return 0

    elif income <= 700000:
        return (income - 300000) * 0.2

    else:
        return (400000 * 0.2) + ((income - 700000) * 0.35)

income = input("What is your income? ")
income = float(income)
tax_owed = tax(income)

print(f"Based on your income, you have to pay NOK {tax_owed} in taxes.")




