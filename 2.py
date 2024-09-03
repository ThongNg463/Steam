def main():
    
    num1 = float(input("VND Price: "))

    num2 = float(input("Quantity: "))

    result1 = num1 * num2

    num3 = float(input("Vn rate: "))

    result2 = result1 / num3

    num4 = float(input("% sticker: "))

    result3 = result2 * num4 / 100

    rounded_result = round(result3, 2)

    print(f"Result: {rounded_result}")

if __name__ == "__main__":
    main()
