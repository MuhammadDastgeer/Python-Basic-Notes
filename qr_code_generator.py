import qrcode

while True:
    data = input("Enter a number: ")

    if data.isdigit():  
        qr = qrcode.make(data)
        qr.save("qrcode.png")
        print("QR Code Generated Successfully!")
        break  
    else:
        print("Invalid input! Please enter a valid integer.")
