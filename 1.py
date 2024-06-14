def main():
    # Yêu cầu người dùng nhập số đầu tiên
    num1 = float(input("Price C5: "))
    
    # Nhân số đầu tiên với 99.1%
    result1 = num1 * 0.991

    # Yêu cầu người dùng nhập số thứ hai
    num2 = float(input("Vn Rate: "))
    
    # Nhân số thứ hai với kết quả của số đầu tiên
    result2 = num2 * result1

    # Làm tròn kết quả đến chữ số thập phân thứ hai
    rounded_result = round(result2, 2)
    
    print(f"Result: {rounded_result}")

if __name__ == "__main__":
    main()

# C:\Users\mthon\Downloads\