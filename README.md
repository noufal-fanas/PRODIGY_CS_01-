# PRODIGY_CS_01-
Ceasercipher encryption and decryption tool.

A professional Command Line Interface (CLI) tool built in Python for message encryption and decryption using the Caesar Cipher algorithm. This project was developed as part of a cybersecurity internship project to demonstrate foundational cryptographic concepts and file handling. 

🚀 FeaturesEncryption: Shifts alphabetic characters by a user-defined integer value.  Decryption: Reverses the shift from a saved text file to retrieve the original message.  

File Handling: Allows users to save encrypted messages to custom .txt files and read from them later for decryption. 
Character Preservation: Maintains original letter casing (uppercase/lowercase) and keeps punctuation and spaces intact.  
User Interface: Features a clean CLI with custom ASCII art branding and defensive error handling. 

🛠️ How to UseRun the script:  Bashpython caesar_tool.py

Encrypt:  Select Option 1 from the main menu.  Enter the message you wish to secure and a shift key (e.g., 3).  Provide a custom filename (the tool automatically adds the .txt extension). 

Decrypt:  Select Option 2 from the main menu.  Enter the exact filename of the encrypted document.  Enter the correct shift key to reveal the original phrase.  

📝 Technical DetailsUnicode Logic: The tool utilizes Python's built-in ord() and chr() functions to map characters to their numerical counterparts.  Wrap-around Logic: Implements the modulo operator % 26 to ensure that shifts at the end of the alphabet (like 'Z') wrap back to the beginning ('A').  Input Validation: Includes file existence checks using the os module to prevent runtime crashes if a file is missing.  

⚠️ DisclaimerThe Caesar Cipher is a simple substitution cipher and is easily cracked using frequency analysis or brute-force methods. This tool is intended for educational and internship demonstration purposes only and should not be used to protect sensitive production-level data. 
