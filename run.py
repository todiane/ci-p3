
# imports ----------
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import datetime
# --------------

"""
Main code for Corri Construction Company that appears in terminal
"""
print(Fore.GREEN + "This is the Corri Construction Company Contractors Page")
print(Fore.CYAN + "\nUse this portal to input your hours for August and September 2023 only.\n")
print("If your hours are for previous months please contact HR on 01305 483048\n")
print("Please input your first and last name to begin:\n")

"""
instructions to add first and last name
"""
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
print(Fore.YELLOW + "Hello " + first_name + " " + last_name + "\n")

"""
instructions to confirm their profession by
selecting one of the letters provided.

"""
def get_profession_choice():
    """
    Dictionary to map profession codes to profession names
    and rate of pay
    """
    professions = {
        "a": {"name": "Bricklayer", "rate": 28},
        "b": {"name": "Plumber", "rate": 36},
        "c": {"name": "Scaffolder", "rate": 25},
        "d": {"name": "Electrician", "rate": 36},
        "e": {"name": "Carpenter", "rate": 29},
        "f": {"name": "Construction Worker", "rate": 27}
    }

    while True:
        """
        Display available professions to the user
        """
        print(Fore.GREEN + "Select your profession:")
        for key, profession in professions.items():
            print(f"{key}: {profession['name']}")

        """
        Prompt the user to enter the letter corresponding to their choice
        """
        choice = input("\nSelect one of the above options " + Fore.GREEN + "a-f: ").lower()

        """
        Validate the users input and confirm their choice
        Or let them know their input is incorrect and provide the
        list of options again
        """
        if choice in professions:
            confirm = input(f"You chose {professions[choice]['name']}. Is this correct? (y/n): ").lower()
            if confirm == "y":
                return professions[choice]
        else:
            print(Back.RED + "Invalid choice. Please choose a valid option.\n")

"""
if yes print out the details including random user number and hourly pay
"""

if __name__ == "__main__":
    chosen_profession = get_profession_choice()
    import random
    print("Thank you.\n")
    print(Fore.GREEN + first_name + " " + "your contractor number is " + str(random.randint(23203, 63944)))
    print(f"Your profession is: {chosen_profession['name']}")
    print(Fore.GREEN + f"You earn £{chosen_profession['rate']} per hour.")
    print("You pay 20% tax and 13% National Insurance\n")

"""
Get dates from the user for August or September 2023 only. Checks if the dates
are within that range and in sequential order if not error message given.
Code created with support from Travis.media.

"""

# Define the valid date range - this can change each month
start_date = datetime.date(2023, 8, 1)
end_date = datetime.date(2023, 9, 30)

# Function to validate the user input
def validate_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        return False
    # Check if the date is within the valid range
    if start_date <= date <= end_date:
        return date
    else:
        return False

# Function to get the date from user
def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        date = validate_date(date_str)
        if date:
            return date
        else:
            print(Back.RED + "\nInvalid date. Please enter a date between 1 August 2023 and 30 September 2023 in DD-MM-YYYY format.\n")

# Function to get the from and to dates from the user
def get_from_to_dates():
    while True:
        from_date = get_date_input("Enter the from date (DD-MM-YYYY): ")
        to_date = get_date_input("Enter the to date (DD-MM-YYYY): ")
        if from_date <= to_date:
            return from_date, to_date
        else:
            print(Back.RED + "\nInvalid dates. The from date must be before or equal to the to date.\n")

from_date, to_date = get_from_to_dates()
print(Fore.GREEN + f"Thank you, you entered from {from_date.strftime('%d-%m-%Y')} to {to_date.strftime('%d-%m-%Y')} as your dates.\n")

"""
Asks user to input their hours and works out pay
"""
hrs = input("Enter your hours: ")
print("\nThis information will be authorised by your manager:\n")
pay = float(hrs) * chosen_profession['rate'] 
print((Fore.CYAN + f"From {from_date.strftime('%d-%m')}") + " " + (f"to {to_date.strftime('%d-%m')}") + " 2023, your pay before tax" + " " + first_name + " " + "is £" + str(pay) + " for" + " " + str(hrs) + " hours\n")

"""
Calculating payment after tax - 20% tax is 0.2 and 13% NI is 0.13
"""
def final_pay(pay, tax, national_insurance):
  pay_after = pay - (tax * pay) - (national_insurance * pay)
  return pay_after

tax = 0.02
national_insurance = 0.013
pay_after = final_pay(pay, tax, national_insurance)
tax_amount = tax * pay
national_insurance_amount = national_insurance * pay

print(Fore.GREEN + f"Pay minus tax (£{tax_amount:.2f}) & NI (£{national_insurance_amount:.2f}) is £{pay_after:.2f}.")
print(Fore.RED + "\nThe TAX and NATIONAL INSURANCE amounts shown are for your information only\n")
print("Final pay amounts are approximate and depend on your tax status")
print("The actual amount you are paid may change\n")
print("If you have any questions please contact HR on 01305 483048\n")




"""
NEED TO ADD : IF EVERYTHING IS OK ASK IF THEY WANT TO EXIT
IF THEY SAY NO EVERYTHING ISN'T OK - PRINT CONTACT HR ON  01305 483048

DO YOU WANT A PRINT OUT - CAN i FIGURE OUT HOW TO PROVIDE A PRINT-OUT SO THEY CAN DOWNLOAD IT.
OR SHOULD I JUST GET PYTHON TO LET THEM SAVE THE INFORMATION FOR THEM?

do you want to include 40% tax and 13% option as well - it will have to be a random computer selection 
so when people enter their details the computer will randomly give them either 20% or 40% status
OR I can set it up so plumber and electrician selections are 40% and the others are 20%

"""
