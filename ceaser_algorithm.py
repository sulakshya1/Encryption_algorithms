N_OF_ALPHABETS = 26
N_OF_DIGITS = 10
def encryption(message, shift):
    encrypted_text = ""
    #shift character
    for char in message:
        if char.isalpha():
            #z comes back to a -> ord changes to ascii code
            ascii_offset = ord('a') if char.islower() else ord('A')
            ascii_char = (ord(char) - ascii_offset + shift) % N_OF_ALPHABETS + ascii_offset
            #changes to ascii code
            cipher = chr(ascii_char)
            encrypted_text += cipher
        elif char.isdigit():
            #changes digits to int and wraps it to 0
            new_digit = (int(char)+shift)% N_OF_DIGITS
            encrypted_text += str(new_digit)
        else:
            encrypted_text += char
    print(encrypted_text)
    pass
def decryption(message, shift):
    shift = shift * -1
    decryption_text = ""
    #shift character
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            ascii_char = (ord(char) - ascii_offset + shift) % N_OF_ALPHABETS + ascii_offset
            cipher = chr(ascii_char)
            decryption_text += cipher
        elif char.isdigit():
            new_digit = (int(char)+shift)% N_OF_DIGITS
            decryption_text += str(new_digit)
        else:
            decryption_text += char
    print(decryption_text)
    pass
def case (user_input):
    if user_input == 1:
        encryption(user_message, user_shift)
        pass
    elif user_input == 2:
        decryption(user_message, user_shift)
        pass
    else:
        print("Invalid input")
        pass
    pass
user_message = input("Message to encrypt: ")
user_shift = int(input("shift key: "))
user_input = int(input("1.for encryption\n2.for decryption\n"))
case(user_input)


#encryption("world_hello 123", 3)
#decryption("zruog_khoor 456",3)