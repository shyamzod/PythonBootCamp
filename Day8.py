#Caesar Cipher
result = ""
exitfrom = False
while not exitfrom:
    choice = input('Do you want to encrypt or decrypt text').lower()
    result=""
    if choice=="encrypt":
        text = input('Enter the text you want to encrypt').lower()
        shift = int(input('Enter the shift position '))
        for ch in text:
            if ord(ch) + shift>122:
                result+=chr(ord(ch) + shift - 26);
            else:
                result += chr(ord(ch) - shift)
        print(result)
    elif choice=="decrypt":
        text = input('Enter the text you want to encrypt').lower()
        shift = int(input('Enter the shift position '))
        for ch in text:
            if ord(ch) - shift<97:
                result+=chr(ord(ch) - shift + 26);
            else:
                result += chr(ord(ch) - shift)
        print(result)
    exitfromprogram = input('Enter E for Exit and other to continue ')
    if 'E' in exitfromprogram:
        exitfrom=True