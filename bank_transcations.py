"""
Description:
Author: Dongok Yang
Date: 2023.09.27
Usage:
"""
import random


transaction_options = ["D", "W", "Q"]
current_balance = float(random.randint(-1000, 10000))
current_balance = "${:,.2f}".format(current_balance)

atm_interface = [
    "***************************************",
    "PIXELL RIVER FINANCIAL".center(40),
    "ATM Simulator".center(40),
    f"Your current balance is: {current_balance}".center(40),
    "",
    "Deposit: D".center(40),
    "Withdraw: W".center(40),
    "To Quit: Q".center(40),
    "***************************************"
]
# Print the centered ATM interface
for line in atm_interface:
    print(line)
