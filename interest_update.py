"""
Description: A practice program for making a file using existing file. 
Author: Dongok Yang
Date: 2023.09.27
Usage: Run the file and you can see the new file has created 
"""
import pprint
import csv
#import libraries to use functions in pprint and csv

account_data = {}
# make a dictionary to store data 

with open("account_balances.txt","r") as file:
    for line in file:
        number_balance = line.strip().split('|')
        account_number, account_balance = number_balance
        account_data[account_number] = float(account_balance)
# open account_balance file and transfer data to accound_data

pprint.PrettyPrinter().pprint(account_data)
# use pretty print to display the contents of dictionary

for account_number,opening_balance in account_data.items():
    if opening_balance >= 5000:
        closing_balance = opening_balance +((opening_balance *0.05)/12)
    elif opening_balance >= 1000:
        closing_balance = opening_balance +((opening_balance *0.025)/12)
    elif opening_balance >=0:
        closing_balance = opening_balance +((opening_balance *0.01)/12)
    else:
        closing_balance = opening_balance +((opening_balance *0.10)/12)
    account_data[account_number] = f"{closing_balance:.6f}"
# applied interest rate and changed value in account_data

pprint.PrettyPrinter().pprint(account_data)
# use pretty print to display the contents of dictionary

filename = "2023-09-27-DY.csv"
# make filename of new csv file 
with open(filename, mode = "w", newline="") as csv_file:
    headings = ["Account", "Balance"]
    writer = csv.writer(csv_file)
    writer.writerow(headings)

    for account_number, closing_balance in account_data.items():
        writer.writerow([account_number,closing_balance])
# make new csv file and transfer contents from account_dta

with open(filename, mode="r") as verification_file:
    reader = csv.reader(verification_file)
    for row in reader:
        if not any(row):
            print("The file has a blank row.")
            break
    else:
        print("The file does not have any blank row.")
# make sure csv file has no blank row

with open(filename, mode="r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
# display upadted data 