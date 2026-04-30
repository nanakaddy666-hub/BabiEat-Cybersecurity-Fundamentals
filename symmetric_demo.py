from cryptography.fernet import Fernet


secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

def protect_order_data(address_text):
    print("--- BabiEat Security System ---")
    print(f"Original Address: {address_text}")
    
    # 2. Encryption (Locking the Data)
    incoming_data = address_text.encode() 
    encrypted_address = cipher_suite.encrypt(incoming_data)
    print(f"Encrypted (Ciphertext): {encrypted_address.decode()}")
    
    return encrypted_address

def reveal_order_data(secure_data):
   
    decrypted_data = cipher_suite.decrypt(secure_data)
    final_address = decrypted_data.decode()
    print(f"Decrypted Result: {final_address}")
    print("-------------------------------")

# Execution
if __name__ == "__main__":
    
    order_info = "Apartment 4B, Rue Hamra, Beirut"
    encrypted_blob = protect_order_data(order_info)
    reveal_order_data(encrypted_blob)