"""
Description:
Author: Dongok Yang
Date: 2023.09.27
Usage:
"""
import pprint

account_data = {}

with open("account_balances.txt","r") as file:
    for line in file:
        print(line)
        number_balance = line.strip().split('|')

        account_number, account_balance = number_balance
        account_data[account_number] = float(account_balance)

pp = pprint.PrettyPrinter(width=20)
pp.pprint(account_data)