"""
Description: A practice program for simulating an ATM interface using loops and logic. 
Author: Dongok Yang
Date: 2023.09.27
Usage: Run program and follow prompts.
"""

import random
import os
from time import sleep
#import libraries to get random value and clear screen 


current_balance = float(random.randint(-1000, 10000))
current_balance_str = "${:,.2f}".format(current_balance)
#declare initial balance with random number

while True:
    #make a infinite loop to allow multiple transactions
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
    #lists that are made to print in a desired format

    for line in atm_interface:
        print(line)
    # printing interface

    selection = input("Enter your selection: ").upper()
    #getting user's selection

    if selection not in ['D', 'W','Q']:
        for line in error_message_selection:
            print(line)
    #If user inputs wrong commands, then print error message

    elif selection == 'Q':
        break
    #if user enter Q, exit this program

    else:
        amount = float(input("Enter amount of transaction: "))
        if selection == 'D':
            current_balance += amount
            current_balance_str = "${:,.2f}".format(current_balance)
            updated_balance[1] = f"Your current balance is: {current_balance_str}".center(40)
            for line in updated_balance:
                print(line)
        # if user decides to deposit money, let them deposit money 

        elif selection =='W':
            if amount > current_balance:
                for line in error_message_fund:
                    print(line)
            # if user decides to withdraw money, let them withdraw money 
            else:
                current_balance -= amount
                current_balance_str = "${:,.2f}".format(current_balance)
                updated_balance[1] = f"Your current balance is: {current_balance_str}".center(40)
                for line in updated_balance:
                    print(line)
            # if user decides to withdraw too much money which excess one's deposit, print error message 
                    
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    # clear existing terminal to enhance readability