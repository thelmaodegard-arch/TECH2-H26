# Lecture solution

import numpy as np

def tax(income):
    """
    Return the taxes owned for a given income.
    """
    if income <= 300000:
        taxes = 0
    elif income <= 700000:
        taxes = 0.2 * (income - 300000)
    else:
        taxes = (0.2 * (700000 - 300000)) + (0.35 * (income - 700000))
    
    return taxes

# Create 13 candidate income levels for testing

incomes = np.linspace(0, 1_200_000, 13)

taxes_loop = []

for income in incomes:
    # Compute taxes for current income level
    taxes = tax(income)

    # Append to list
    taxes_loop.append(taxes)

    # Income after tax
    net_income = income - taxes

    print(f"Gross income: {income:10.0f}; "
          f"Taxes: {taxes:10.0f}; "
          f"Net income: {net_income:10.0f}.")