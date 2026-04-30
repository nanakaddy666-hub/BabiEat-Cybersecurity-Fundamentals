from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def secure_send_to_babieat(message_text):
    print("--- BabiEat Secure Incoming Channel ---")
    
    secret_message = message_text.encode()
    ciphertext = public_key.encrypt(
        secret_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Encrypted for BabiEat: {ciphertext.hex()[:50]}...") # Show only first 50 chars
    return ciphertext

def babieat_private_read(encrypted_data):
    # 3. Decrypting with the PRIVATE key
    decrypted_message = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"BabiEat Decrypted Message: {decrypted_message.decode()}")
    print("---------------------------------------")

# Execution
if __name__ == "__main__":
    msg = "Restaurant Bank Info: Bank of Beirut - ACC# 12345678"
    blob = secure_send_to_babieat(msg)
    babieat_private_read(blob)