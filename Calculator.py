import math

def show_menu():
    print("\n" + "="*40)
    print("Advanced Calculator")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Divisors of a number")
    print("6. Sine (input in radians)")
    print("7. Cosine (input in radians)")
    print("0. Exit")
    print("="*40)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Error: Please enter a positive integer.")
        except ValueError:
            print("Error: Input must be an integer.")

def divisors(n):
    n = int(n)
    divs = [i for i in range(1, n+1) if n % i == 0]
    return divs

def main():
    while True:
        show_menu()
        choice = input("Your choice: ")

        if choice == '0':
            print("Exiting program. Goodbye!")
            break

        elif choice == '1':
            a = get_number("First number: ")
            b = get_number("Second number: ")
            print(f"Result: {a} + {b} = {a + b}")

        elif choice == '2':
            a = get_number("First number: ")
            b = get_number("Second number: ")
            print(f"Result: {a} - {b} = {a - b}")

        elif choice == '3':
            a = get_number("First number: ")
            b = get_number("Second number: ")
            print(f"Result: {a} * {b} = {a * b}")

        elif choice == '4':
            a = get_number("Dividend: ")
            b = get_number("Divisor: ")
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {a} / {b} = {a / b}")

        elif choice == '5':
            num = get_positive_int("Enter a positive integer: ")
            divs = divisors(num)
            print(f"Divisors of {num}: {divs}")

        elif choice == '6':
            deg = get_number("Enter angle in degrees : ")
            rad = math.radians(deg)  # Convert degrees to radians
            result = math.sin(rad)
            print(f"sin({deg}) = {result}")

        elif choice == '7':
            deg = get_number("Enter angle in degrees : ")
            rad = math.radians(deg)  # Convert degrees to radians6
            result = math.cos(rad)
            print(f"cos({deg}) = {result}")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()