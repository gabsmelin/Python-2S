
criptografia_dec = AES.new(senha, AES.MODE_EAX, nonce=nonce)
decifra = criptografia_dec.decrypt_and_verify(cifra, tag)
print("\nMensagem Decifrada")
print(decifra.decode("UTF-8"))