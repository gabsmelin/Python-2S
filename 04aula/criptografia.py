from Crypto.Cipher import AES

msg = bytes("Olá Mundo", "uft-8")
senha = bytes("FIAPfiap20232023", "uft-8")

#implementando criptografia
criptografia = AES