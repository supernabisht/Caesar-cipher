import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar( original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:

            shifted_pos=alphabet.index(letter) + shift_amount
            shifted_pos= shifted_pos%len(alphabet)
            output_text+=alphabet[shifted_pos]
    print(f"Here is the {encode_or_decode} : {output_text}")

should_continue = True
while should_continue:
    text = input("Type the message which you like to encode/decode").lower()
    direction = input("type 'encode' to encode the message and 'decode' to decode the message").lower()
    shift = int(input(" type the value through which message should be shifted"))

    caesar(text, shift, direction)

    restart = input("Do you want to restart it?").lower()

    if restart == "no":
        should_continue = False
        print("GOODBYE!")










