def subscreve():
    from Crypto.Cipher import AES
    msg = bytes("Notebook;3;3000,00;RH", "utf-8")

    senha = bytes("FIAPfiap20232023", "utf-8")
    #implementar a criptografia
    criptografia = AES.new(senha, AES.MODE_EAX)#
    nonce = criptografia.nonce
    cifra, tag = criptografia.encrypt_and_digest(msg)#
    print("\nMensagem Cifrada")
    print(cifra)
    with open("Dados.csv", "wb") as arquivo:
        arquivo.write(cifra)
        
def apende():    
    with open("relatorio.csv", "a") as arquivo:        
        arquivo.write("\nBanana;1;1,00;Pessoal")

def ler():    
    invent = {}    
    with open("Relatorio.csv", "r") as arquivo:        
        dados_linha = arquivo.readlines()        
        for linha in dados_linha:            
            lista = linha.split(";")            
            invent[lista[0]] = [lista[1], lista[2], lista[3]]
subscreve()
ler()