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

pp = pprint.PrettyPrinter(20)
pp.pprint(account_data)

for account_number,opening_balance in account_data.items():
    print(opening_balance)
    if opening_balance >= 5000:
        closing_balance = opening_balance +((opening_balance *0.05)/12)
    elif opening_balance >= 1000:
        closing_balance = opening_balance +((opening_balance *0.025)/12)
    elif opening_balance >=0:
        closing_balance = opening_balance +((opening_balance *0.01)/12)
    else:
        closing_balance = opening_balance +((opening_balance *0.10)/12)
    account_data[account_number] = f"{closing_balance:.6f}"

pp.pprint(account_data)

