
def calculate_discount(price, discount_percent):
    selling_price = price
    if discount_percent > 20:
        selling_price = (price * 20) / 100
    
    return selling_price

if __name__ == "__main__":
    try:
        price = float(input("Enter the price of the item: "))
        discount = float(input("Enter the discount of the item: "))

        if discount < 0 or discount > 100:
            print('Please enter a valid discount between 1 and 100')
        else:
            print(f"The selling price of the item is {calculate_discount(price, discount)}")
    except ValueError:
        print('please enter a valid number for price and discount')
        

    