import os
import base64


def get_fonts(directory="C:/Users/Eva-02/PycharmProjects/petlist.fun/assets/fonts"):
    font_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith(".ttf"):
            name = os.path.splitext(filename)[0]
            font_dict[name] = f"/fonts/{filename}"

    return font_dict


def encrypt_data(user_id):
    # Преобразуем user_id в байтовую строку
    user_id_bytes = str(user_id).encode('utf-8')

    # Шифруем user_id с помощью Base64
    encrypted_user_id_bytes = base64.b64encode(user_id_bytes)

    # Преобразуем зашифрованный user_id обратно в строку
    encrypted_user_id = encrypted_user_id_bytes.decode('utf-8')

    return encrypted_user_id


def decrypt_data(encrypted_user_id):
    # Преобразуем зашифрованный user_id в байтовую строку
    encrypted_user_id_bytes = encrypted_user_id.encode('utf-8')

    # Дешифруем user_id с помощью Base64
    decrypted_user_id_bytes = base64.b64decode(encrypted_user_id_bytes)

    # Преобразуем дешифрованный user_id обратно в строку
    decrypted_user_id = decrypted_user_id_bytes.decode('utf-8')

    return decrypted_user_id

