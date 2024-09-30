def get_user_input():
    value = float(input("Enter the value to convert: "))
    return value

def select_unit():
    print("Select the conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Kilometers to Miles")
    print("3. Kilograms to Pounds")
    choice = int(input("Enter your choice (1-3): "))
    return choice

def convert(value, choice):
    if choice == 1:
        result = (value * 9/5) + 32
        return f"{value}°C is equal to {result}°F"
    elif choice == 2:
        result = value * 0.621371
        return f"{value} km is equal to {result} miles"
    elif choice == 3:
        result = value * 2.20462
        return f"{value} kg is equal to {result} lbs"
    else:
        return None

def main():
    while True:
        value = get_user_input()
        choice = select_unit()
        
        result = convert(value, choice)
        
        if result:
            print(result)  # Show result
        else:
            print("Error: Invalid conversion choice")  # Display error message
        
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
