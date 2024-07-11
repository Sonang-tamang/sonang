from datetime import datetime
from display_lands import read_lands

def print_in_box(data):
    box_width = 80
    print("+" + "-" * 80 + "+")
    for line in data.split("\n"):
        print("| " + line.center(box_width - 4) + " |")
    print("+" + "-" * 80 + "+")

def get_ID(content):
    while True:
        try:
            ID = input("Enter the Land ID you want to rent: ")
            for land in content:
                if land[0] == ID:
                    if land[-1] == "Available":
                        return ID
                    else:
                        print("Sorry, this land is not available.")
                        break
            else:
                print("Invalid Land ID! Please enter a valid Land ID.")
        except ValueError:
            print("Invalid Land ID! Please enter a valid Land ID.")

def calculate_monthly_price(land):
    # Assuming the price is fixed and doesn't change
    price_per_month = float(land[4])
    return price_per_month

def renting():
    cart = []
    content = read_lands("land.txt")  # Read lands from the file
    while True:
        ID = get_ID(content)
        for land in content:
            if land[0] == ID:
                if land[-1] == "Not Available":  # Check if the land is available
                    print("Sorry, this land is not available.")
                    break
                cart.append(ID)
                land[-1] = "Not Available"  # Mark the land as not available
                break
        else:
            print("Invalid Land ID! Please enter a valid Land ID.")
            continue

        user_input = input("Would you like to rent another Land too (yes/no): ").lower()
        if user_input == "no":
            break
        elif user_input != "yes":
            print("Invalid input! Please enter yes or no.")

    # Update the text file to reflect the changes
    file = open("land.txt", "w")
    for land in content:
        file.write(", ".join(land) + "\n")
    file.close()

    # Rest of the function remains the same

    
    # Invoice generation
    user_FName = input("Enter your first name: ")
    user_LName = input("Enter your last name: ")
    user_Contact = input("Enter your contact: ")
    rent_date = datetime.now().strftime('%Y-%m-%d')

    # Input to calculate number of months to rent
    num_months = int(input("Enter the number of months to rent: "))

    invoice_file_name = f"{user_FName}_{user_LName}_rent_invoice.txt"
    invoice_file = open(invoice_file_name, "w")
    invoice_file.write("+" + "-" * 101 + "+\n")
    invoice_file.write("|" + "Techno Property Nepal".center(99) + "|\n")
    invoice_file.write("|" + f"Kamalpokhari, Kathmandu | Phone No: +977-9865425360 ".center(99) + "|\n")
    invoice_file.write("+" + "-" * 101 + "+\n")
    invoice_file.write("|" + "Land Details are:".center(99) + "|\n")
    invoice_file.write("+" + "-" * 101 + "+\n")
    invoice_file.write("|" + f"Name of the Customer: {user_FName} {user_LName}".center(99) + "|\n")
    invoice_file.write("|" + f"Contact number: {user_Contact}".center(99) + "|\n")
    invoice_file.write("|" + f"Date and time of purchase: {rent_date}".center(99) + "|\n")
    invoice_file.write("+" + "-" * 101 + "+\n")
    invoice_file.write("|" + "Land Rent Details are:".center(99) + "|\n")
    invoice_file.write("+" + "-" * 101 + "+\n")
    invoice_file.write("|" + "LandID".center(10) + "|" + "City".center(20) + "|" + "Direction".center(20) + "|" + "Price".center(20) + "|" + "Rented Months".center(20) + "|" + "Total Price".center(20) + "|\n")
    invoice_file.write("+" + "-" * 101 + "+\n")

    GrandTotal = 0
    for i, ID in enumerate(cart, start=1):
        for land in content:
            if land[0] == ID:
                price_per_month = calculate_monthly_price(land)
                total_price = price_per_month * num_months
                GrandTotal += total_price
                invoice_file.write(f"|{land[0]:^10}|{land[1]:^20}|{land[2]:^20}|{price_per_month:^20.2f}|{num_months:^20}|NRs{total_price:<19.2f}|\n")
                break
    invoice_file.write("+" + "-" * 101 + "+\n")
    invoice_file.write(f"{'Grand Total:':<91}Nrs {GrandTotal:<18.2f}\n")
    invoice_file.close()

if __name__ == "__main__":
    
    renting()
