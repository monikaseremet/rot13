import string
string.ascii_lowercase
ascii_lowercase = list(string.ascii_lowercase)*2
    
def rot13():
    string_decrypted = ""
    string_encrypted = ""
    
    print("Hello!\nThis program can help you to encrypt or decrypt whatever you want.\nIt's called ROT13 cipher.") 
    
    while True:
        input = input("Please choose what do you want to do: encrypt(en), decrypt(de) or quit(q): ")

        if input.lower() == "en":
            string_to_encrypt = input("Please type in a string to ecrypt: ")
            for char in string_to_encrypt:
                if char == " ":
                    string_decrypted += " "
                    continue
                index = ascii_lowercase.index(char)
                string_decrypted += ascii_lowercase[index+13]
            print(f"Your decrypted string is: {string_decrypted}")

        elif input.lower() == "de":
            string_to_decrypt = input("Please type in a string to decrypt: ")
            for char in string_to_decrypt:
                if char == " ":
                    string_encrypted += " "
                    continue
                index = ascii_lowercase.index(char)
                string_encrypted += ascii_lowercase[index+13]
            print(f"Your encrypted string is: {string_encrypted}")
            
        elif input.lower() == "q":
            break

rot13()
