# Lenora Welborne
# CIS261
# Invoice Line Item Calculator
def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")
def get_quantity():
    while True:
        try: 
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")
def main():
    print("The Invoice Line Item Calculator\n")
    while True:
        price = get_price()
        quantity = get_quantity()
        line_total = price * quantity
        print(f"\nPRICE: ${price:.2f}")
        print(f"QUANTITY:  {quantity}")
        print(f"TOTAL: ${line_total:.2f}")
        more_items = input("Enter another line item? (y/n): ").lower()
        if more_items != 'y':
            print("Bye!")
            break
        print()
if __name__ == "__main__":
    main()
