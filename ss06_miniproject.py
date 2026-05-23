laptop = 0
phone = 0
tablet = 0

while True:
    print('===== MENU =====')
    print('1. Xem báo cáo tồn kho')
    print('2. Nhập kho')
    print('3. Xuất kho')
    print('4. Cảnh báo hàng tồn kho thấp')
    print('5. Thoát chương trình.')
    print('===============================')
    
    choice = int(input('Nhập lựa chọn: '))
    
    if choice == 1:
        print("=== BÁO CÁO TỒN KHO ===")
        print(f"Laptop ({laptop}): ", end="")
        for i in range(laptop):
            print("*", end="")
        print() 
        
        print(f"Phone ({phone}): ", end="")
        for i in range(phone):
            print("*", end="")
        print()
        
        print(f"Tablet ({tablet}): ", end="")
        for i in range(tablet):
            print("*", end="")
        print("\n=======================")
        
    elif choice == 2:
        print("1-Laptop")
        print("2-Phone")
        print("3-Tablet")
        input_product = int(input('Nhập lựa chọn mặt hàng muốn nhập: '))
        
        if input_product == 1:
            while True:
                quantity = int(input("Số lượng muốn nhập: "))
                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                else:
                    laptop += quantity
                    break
        elif input_product == 2:
            while True:
                quantity = int(input("Số lượng muốn nhập: "))
                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                else:
                    phone += quantity
                    break
        elif input_product == 3:
            while True:
                quantity = int(input("Số lượng muốn nhập: "))
                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                else:
                    tablet += quantity
                    break
        else:
            print("Mặt hàng không hợp lệ!")

    elif choice == 3:
        print("1-Laptop")
        print("2-Phone")
        print("3-Tablet")
        input_product = int(input('Nhập lựa chọn mặt hàng muốn xuất: '))
        
        if input_product == 1:
            while True:
                quantity = int(input("Số lượng muốn xuất: "))
                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                elif quantity > laptop:
                    print("Không đủ hàng! Giao dịch bị hủy.")
                    break
                else:
                    laptop -= quantity
                    break
        elif input_product == 2:
            while True:
                quantity = int(input("Số lượng muốn xuất: ")) 
                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                elif quantity > phone:
                    print("Không đủ hàng! Giao dịch bị hủy.")
                    break
                else:
                    phone -= quantity
                    break
        elif input_product == 3:
            while True:
                quantity = int(input("Số lượng muốn xuất: "))
                if quantity < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                elif quantity > tablet:
                    print("Không đủ hàng! Giao dịch bị hủy.")
                    break
                else:
                    tablet -= quantity
                    break
        else:
            print("Mặt hàng không hợp lệ!")
            
    elif choice == 4:
        if laptop < 10:
            print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {laptop} sản phẩm)")
        if phone < 10:
            print(f"[CẢNH BÁO] Mặt hàng Phone sắp hết (Chỉ còn {phone} sản phẩm)")
        if tablet < 10:
            print(f"[CẢNH BÁO] Mặt hàng Tablet sắp hết (Chỉ còn {tablet} sản phẩm)")
            
    elif choice == 5:
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại từ 1 đến 5!")