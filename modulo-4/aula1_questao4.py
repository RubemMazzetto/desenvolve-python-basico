def find_largest_number_in_sequence():
    try:
        num_count = int(input("Enter the number of values to check: "))

        if num_count <= 0:
            print("No numbers to process.")
            return

        first_number = int(input(f"Enter a number ({num_count} remaining): "))
        largest = first_number
        num_count -= 1

        while num_count > 0:
            x = int(input(f"Enter a number ({num_count} remaining): "))
            
            if x > largest:
                largest = x
            
            num_count -= 1
            
        print(f"The largest number is: {largest}")

    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    find_largest_number_in_sequence()