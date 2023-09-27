"""
Description:
Author: Dongok Yang
Date: 2023.09.27
Usage:
"""
import pprint
import csv

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

filename = "2023-09-27-DY.csv"

with open(filename, mode = "w", newline="") as csv_file:
    headings = ["Account", "Balance"]
    writer = csv.writer(csv_file)
    writer.writerow(headings)

    for account_number, closing_balance in account_data.items():
        writer.writerow([account_number,closing_balance])



print(f"Data has been written to {filename}")
with open(filename, mode="r") as verification_file:
    reader = csv.reader(verification_file)
    for row in reader:
        if not any(row):
            print("The file has a blank row.")
            break
    else:
        print("The file does not have any blank row")