import re

# Nhập input từ người dùng
input_data = input("Input: ")

# Sử dụng regex để tách các số theo định dạng có chữ 'k'
data = re.findall(r'\d+k', input_data)

# Tính tổng
total = sum(int(item.replace('k', '')) for item in data)

# Hiển thị kết quả
print(f"Tổng các số là: {total}")