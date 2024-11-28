def caesar_cipher(text, shift, mode):
    shift = (-shift if mode == 'decrypt' else shift) % 26
    return ''.join(
        chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97))
        if c.isalpha() else c for c in text
    )

def main():
    print("Welcome to the Caesar Cipher Program!")
    mode = input("\n1. Encrypt\n2. Decrypt\nChoose (1/2): ").strip()
    if mode not in ['1', '2']:
        return print("Invalid choice! Please restart.")
    text = input("Enter the text: ").strip()
    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        return print("Shift value must be an integer! Restart the program.")
    print("\nResult:", caesar_cipher(text, shift, 'decrypt' if mode == '2' else 'encrypt'))

if __name__ == "__main__":
    main()
