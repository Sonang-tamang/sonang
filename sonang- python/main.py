from display_lands import display_available_lands
from operations import renting
from return_lands import return_lands  # Import the function without calling it

# Main function
def main():
    while True:
        print("\nLand Renting System")
        print("1. Display available lands")
        print("2. Rent a land")
        print("3. Return a land")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
           display_available_lands()
        elif choice == '2':
            renting()
        elif choice == '3':
            return_lands()  # Call return_lands when the user chooses option 3
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
