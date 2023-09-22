# Segundo Semestre

Aula 03 | Bibliotecas

- pip -v
|-> Gestor de pacotes do python
|-> Para intalarmos "extensões" em forma de txt, usamos "pip install -r req.txt"

----->Pesquisar ação AES<-----


Biblioteca AES, DES E DES3
|-> Algoritimos de criptografia
|-->DES:  
|-->DES3: Dados incriptado com DES e mais três vezes.
|-->AES:
|-->RSA: Padrões de criptografia de calculo inareverciveis.

|-->Hash MD5(não volta pro código original,senha) = Algoritimo quabrado(de forma alguma devemos usá-los)
|-->HOJE EM DIA USAMOS SHA3_512


1º Passo = variável para criptografar tem que estar em bytes, não em texto direto porque o computadorsó trabalha com 0 e 1.
2º Passo = o bytes tem dois parâmetros(1: mensagem, 2: tipo, geralmente "utf-8")
3º Passo = criamos o AES(aes.new) e dentro dele passamos dois parametros(1: a senha e depois modo que a criptografia ira instancia-lá, geralmente usamos AES.MODE.EAX)/VALIDAÇÃO DA CRIPTO
4º Passo = depois criamos uma variável nonce e depois fazer um criptografia.nonce(para temperar, deixar mais dificil de descriptografar/ser lida)
5º Passo = meio que "criptografamos mais uma vez", pegamos a senha e a mensagem "batemos no liquidificador" e devolvemos em duas váriaveis, uma mensagem criptografada e a outra a própria mensagem

Para reverter
1º Passo = usamos a mesma coisa mas com o parametro de nonce(que já é do AES)
2º Passo = agora desmastigamos com o decrypt_and_verify e passamos os dois paramêtros da mensagem.


