import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_game = True

def encrypt(original_text, shift_amount):
    encoded_text = ''
    for letter in original_text:
        if letter == " ":
            encoded_text += " "
        elif letter not in alphabet:
            encoded_text += letter
        else:   
            current_index = alphabet.index(letter)
            encode_index = current_index + shift_amount
            encoded_text += alphabet[encode_index]       
    print(f"Here is your encoded result: {encoded_text}")


def decrypt(original_text, shift_amount):
    decoded_text = ''
    for letter in original_text:
        if letter == " ":
            decoded_text += " "
        elif letter not in alphabet:
            decoded_text += letter
        else:   
            current_index = alphabet.index(letter)
            decode_index = current_index - shift_amount
            decoded_text += alphabet[decode_index]       
    print(f"Here is your decoded result: {decoded_text}")
def ceasar(original_text, shift_amount):
    global continue_game
    if direction.lower() == 'encode':
        encrypt(original_text,shift_amount)
    elif direction.lower() == 'decode':
        decrypt(original_text,shift_amount)
    status = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    # Update continue_game based on status
    if status == 'no':
        continue_game = False
        print("Goodbye!")
    elif status != 'yes':  # Handle invalid input
        print("Invalid input. Exiting anyway.")
        continue_game = False
    

print(art.logo)

while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift)


# decrypt(text,shift)


    
       
