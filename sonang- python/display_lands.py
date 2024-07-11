def read_lands(filename):
    lands = []
    file = open(filename, "r")
    for line in file:
        lands.append(line.strip().split(", "))
    file.close()
    return lands

# Function to display available lands
def display_available_lands():
    lands = read_lands("land.txt")  # Provide the filename here
    print("Available Lands:")
    for land in lands:
        print(", ".join(land))

if __name__ == "__main__":
    display_available_lands()
