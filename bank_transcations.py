"""
Description:
Author: Dongok Yang
Date: 2023.09.27
Usage:
"""

import random
import os
from time import sleep
#import libraries to get random value and clear screen 


current_balance = float(random.randint(-1000, 10000))
current_balance_str = "${:,.2f}".format(current_balance)
#declare initial balance with random number

while True:
    #make a infinite loop 
    atm_interface = [
        "***************************************",
        "PIXELL RIVER FINANCIAL".center(40),
        "ATM Simulator".center(40),
        f"Your current balance is: {current_balance_str}".center(40),
        "",
        "Deposit: D".center(40),
        "Withdraw: W".center(40),
        "To Quit: Q".center(40),
        "***************************************"
    ]
    error_message_selection = [
        '***************************************'.center(40),
        'INVALID SELECTION'.center(40),
        '***************************************'.center(40)
    ]
    error_message_fund = [
        '***************************************'.center(40),
        'INSUFFICIENT FUNDS'.center(40),
        '***************************************'.center(40)
    ]
    updated_balance = [
        '***************************************',
        f"Your current balance is: {current_balance_str}".center(40),
        '***************************************'
    ]

    for line in atm_interface:
        print(line)

    selection = input("Enter your selection:").upper()
    if selection not in ['D', 'W','Q']:
        for line in error_message_selection:
            print(line)

    elif selection == 'Q':
        break

    else:
        amount = float(input("Enter amount of transaction:"))
        if selection == 'D':
            current_balance += amount
            current_balance_str = "${:,.2f}".format(current_balance)
            updated_balance[1] = f"Your current balance is: {current_balance_str}".center(40)
            for line in updated_balance:
                print(line)

        elif selection =='W':
            current_balance -= amount
            if amount > current_balance:
                for line in error_message_fund:
                    print(line)
            else:
                current_balance_str = "${:,.2f}".format(current_balance)
                updated_balance[1] = f"Your current balance is: {current_balance_str}".center(40)
                for line in updated_balance:
                    print(line)
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')