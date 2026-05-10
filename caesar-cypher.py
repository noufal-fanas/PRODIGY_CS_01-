import os

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def display_banner():
    print("-" * 60)
    print("""
  ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ 
 ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
 ██║     ███████║█████╗  ███████╗███████║██████╔╝
 ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
 ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
    """)
    print("           DEVELOPER: NOUFAL N S")
    print("-" * 60)

def get_valid_filename(prompt):
    fname = input(prompt).strip()
    if not fname.endswith(".txt"):
        fname += ".txt"
    return fname

def main():
    while True:
        display_banner()
        print("1. Encrypt Message & Save to Custom File")
        print("2. Decrypt Message from Custom File")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ")

        if choice == '1':
            msg = input("\nEnter the message to encrypt: ")
            shift = int(input("Enter shift value (number): "))
            encrypted_msg = caesar_cipher(msg, shift, 'encrypt')
            
            
            filename = get_valid_filename("Enter the name for your new file: ")
            
            with open(filename, "w") as f:
                f.write(encrypted_msg)
            
            print(f"\n[✔] Success! Message saved to: {filename}")
            print(f"Encrypted Content: {encrypted_msg}")

        elif choice == '2':
            filename = get_valid_filename("Enter the filename to decrypt (e.g., secret_data): ")
            
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    encrypted_content = f.read()
                
                print(f"\nFile Content Found: {encrypted_content}")
                shift = int(input("Enter the shift value used for encryption: "))
                decrypted_msg = caesar_cipher(encrypted_content, shift, 'decrypt')
                
                print(f"\n[✔] Decrypted Message: {decrypted_msg}")
            else:
                print(f"\n[!] Error: The file '{filename}' was not found.")

        elif choice == '3':
            print("\nExiting... Great work today, Noufal!")
            break
        else:
            print("\n[!] Invalid choice. Please try again.")

        input("\nPress Enter to return to menu...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
