# Caesar Cipher Program - SkillCraft Technology

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# --- User Input Section ---
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
text = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))

if choice == "E":
    ciphertext = caesar_encrypt(text, shift)
    print("Encrypted text:", ciphertext)
elif choice == "D":
    plaintext = caesar_decrypt(text, shift)
    print("Decrypted text:", plaintext)
else:
    print("Invalid choice! Please enter E or D.")
