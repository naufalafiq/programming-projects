FIRST_CHAR_CODE = ord('A')
LAST_CHAR_CODE = ord('Z')
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_shift(message, shift):        
    # Result placeholder
    result = ""

    # Go through each of the letters in the message
    for char in message.upper():
        if char.isalpha() == True:
            # Convert character to the ASCII code
            char_code = ord(char)
            new_char_code = char_code + shift
            # Checking if shifted character goes beyond Z
            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
            # Checking if shifted character is before A
            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE
            # Converting ASCII back into character and storing in result
            new_char = chr(new_char_code)
            result += new_char
        else:
            # Add the character as is if it's not a letter
            result += char

    print(result)

# Ask the user for message and key and display output
user_message = input('Message to Encrypt: ')
user_shift_key = int(input('Shift Key (integer): '))
caesar_shift(user_message, user_shift_key)