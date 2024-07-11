from datetime import datetime

# Function to read lands from file
def read_lands():
    try:
        file = open("land.txt", "r")
        lands = [line.strip().split(", ") for line in file]
        file.close()
    except FileNotFoundError:
        print("File not found.")
        lands = []
    return lands

# Function to write lands to file
def write_lands(lands):
    file = open("land.txt", "w")
    for land in lands:
        file.write(", ".join(land) + "\n")
    file.close()

# Function to calculate the late fee
def calculate_late_fee(total_price, num_months_late):
    if num_months_late <= 0:
        return 0
    late_fee_rate = 0.10  # 10% late fee rate
    late_fee = total_price * late_fee_rate * num_months_late
    return late_fee

# Function to return lands
def return_lands():
    while True:
        lands = read_lands()  # Read lands from the file
        return_ids = input("Enter the IDs of the lands to return separated by space (or 'done' to finish): ").lower()
        
        if return_ids == 'done':
            break

        return_ids = return_ids.split()  # Split the input by spaces
        returned_lands = []
        total_rental_price = 0
        total_late_fee = 0

        user_name = input("Enter your name: ")

        for return_id in return_ids:
            found_land = next((land for land in lands if land[0] == return_id), None)
            if found_land:
                if found_land[5] == "Available":
                    print("Land with ID " + return_id + " is already returned.")
                else:
                    found_land[5] = "Available"  # Update status to "Available" in the text file
                    print("Land with ID " + return_id + " has been returned.")

                    # Check if the user was late in returning the land
                    while True:
                        rented_months = int(input("Enter the number of months the land " + return_id + " was rented: "))
                        if rented_months >= 0:
                            break
                        else:
                            print("Please enter a non-negative value.")

                    while True:
                        returned_months = int(input("Enter the number of months the land " + return_id + " was returned: "))
                        if returned_months >= 0:
                            break
                        else:
                            print("Please enter a non-negative value.")

                    num_months_late = returned_months - rented_months
                    rental_price_per_month = float(found_land[4]) / 12
                    total_rental_price += rental_price_per_month * rented_months
                    late_fee = calculate_late_fee(rental_price_per_month * rented_months, num_months_late)
                    total_late_fee += late_fee
                    if num_months_late > 0:
                        print("You were late by " + str(num_months_late) + " months.")
                        print("Late fee for land " + return_id + ": NRs " + "{:.2f}".format(late_fee))

                    returned_lands.append((found_land, rented_months, returned_months, num_months_late, late_fee))
            else:
                print("Land with ID " + return_id + " not found.")

        # Update the file to reflect the changes (update status to "Available")
        write_lands(lands)

        # Generate bill for returned lands
        if returned_lands:
            return_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            invoice_number = datetime.now().strftime('%Y%m%d%H%M%S%f')  # Unique invoice number

            invoice_file_name = user_name + "_return_invoice_" + invoice_number + ".txt"
            invoice_file = open(invoice_file_name, "w")
            invoice_file.write("+" + "-" * 101 + "+\n")
            invoice_file.write("|" + "Return Bill Details".center(99) + "|\n")
            invoice_file.write("|Date and Time: " + return_date_time + "\n")
            invoice_file.write("+" + "-" * 101 + "+\n")

            for land, rented_months, returned_months, num_months_late, late_fee in returned_lands:
                total_price_with_late_fee = rental_price_per_month * rented_months + late_fee
                invoice_file.write("Kitta No.: " + land[0] + "\n")
                invoice_file.write("Rented Months: " + str(rented_months) + "\n")
                invoice_file.write("Returned Months: " + str(returned_months) + "\n")
                invoice_file.write("Price per Month: Rs. {:.2f}\n".format(rental_price_per_month))
                invoice_file.write("Total Rental Price: Rs. {:.2f}\n".format(rental_price_per_month * rented_months))
                invoice_file.write("Delayed Months: " + str(num_months_late) + "\n")
                invoice_file.write("Fine: Rs. {:.2f}\n".format(late_fee))
                invoice_file.write("Total Amount with Fine: Rs. {:.2f}\n".format(total_price_with_late_fee))
                invoice_file.write("+" + "-" * 101 + "+\n")

            grand_total = total_rental_price + total_late_fee
            invoice_file.write("Total Rental Price: Rs. {:.2f}\n".format(total_rental_price))
            invoice_file.write("Total Late Fee: Rs. {:.2f}\n".format(total_late_fee))
            invoice_file.write("Grand Total: Rs. {:.2f}\n".format(grand_total))
            invoice_file.write("+" + "-" * 101 + "+\n")
            invoice_file.close()

# Only execute return_lands when this script is run directly, not when imported
if __name__ == "__main__":
    return_lands()
