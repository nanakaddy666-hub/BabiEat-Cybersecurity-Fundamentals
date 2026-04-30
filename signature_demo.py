from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def sign_delivery_status(status_message):
    print("--- BabiEat Dispatch: Signing Status ---")
    message_bytes = status_message.encode()
    
   
    signature = private_key.sign(
        message_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(f"Status: {status_message}")
    print(f"Signature Created: {signature.hex()[:40]}...")
    return signature

def verify_delivery_status(status_message, signature_to_check):

    try:
        public_key.verify(
            signature_to_check,
            status_message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Verification SUCCESS: The message is authentic and untampered.")
    except Exception:
        print("Verification FAILED: Warning! This message might be fake or modified.")
    print("---------------------------------------")

# Execution
if __name__ == "__main__":
    confirm_msg = "Order #9921: Delivered at 14:30 GMT"
    sig = sign_delivery_status(confirm_msg)
    
   
    verify_delivery_status(confirm_msg, sig)