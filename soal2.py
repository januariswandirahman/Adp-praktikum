while True:
    Hkecil = False
    Hkapital = False
    digit = False
    istimewa = False
    istimewa = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~|"
    password = input("masukan password:=")
    if len(password)>= 8:
        for i in password:
            if 'a'<= i <= 'z':
                Hkecil = True
            elif 'A'<= i <='Z':
                Hkapital = True
            elif '0'<= i <= '9':
                digit = True
            elif i in istimewa:
                istimewa= True
    if Hkecil and Hkapital and digit and istimewa:
        print("password valid ")
        break
    else:
        print("passwor tidak valid, silahkan coba lagi")

            