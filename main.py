
mensagem = input("Digite a mensagem! ")
chave = int(input("Digite a chave de deslocamento: "))

mensagem = mensagem.lower()

print("Mensagem: ", mensagem)
print("Chave: ", chave)

mensagemCompleta = ""

for cadaLetra in mensagem:

    if cadaLetra.isalpha():
        formula = (ord(cadaLetra) - ord('a') + chave) %26 + ord('a')
        nova_letra = chr(formula) 
        
        mensagemCompleta = mensagemCompleta + nova_letra
    else:
        mensagemCompleta = mensagemCompleta + cadaLetra

print("Mensagem criptografada: ", mensagemCompleta)
