def encrypt_text(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += chr((ord(char) - 97 + 3) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_text_list(text_list):
    encrypted_text_list = []
    for text in text_list:
        encrypted_text_list.append(encrypt_text(text))
    return encrypted_text_list

# test
text_list = ["hello", "world", "encrypt_this"]
print(encrypt_text_list(text_list))
