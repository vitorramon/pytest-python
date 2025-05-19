def calculate_total(price, discount_rate, tax_rate):
    """
    Calculate the total price after applying a discount and adding tax.

    :param price: Original price
    :param discount_rate: Discount rate (as a decimal)
    :param tax_rate: Tax rate (as a decimal)
    :return: Total price after discount and tax
    """
    discount = price * discount_rate
    tax = (price - discount) * tax_rate
    total = price - discount + tax
    return round(total, 2)

if __name__ == "__main__":
    # Example usage
    price = 100.0
    discount_rate = 0.1  # 10% discount
    tax_rate = 0.2      # 20% tax

    total_price = calculate_total(price, discount_rate, tax_rate)
    print(f"The total price after discount and tax is: {total_price}")