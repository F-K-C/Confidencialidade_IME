
print("Seja bem-vindo ao programa de criptografia com Cifras de César e Confidencialidade!")
print("1- Criptografar uma mensagem: ")
print("2- Descriptografar uma mensagem: ")

opcao = input("Digite a sua escolha: ")

def cifrar(mensagem, chave):
    mensagem = mensagem.lower()
    mensagemCompleta = ""
    for cadaLetra in mensagem:
        if cadaLetra.isalpha():
            formula = (ord(cadaLetra) - ord('a') + chave) %26 + ord('a')
            nova_letra = chr(formula)
            mensagemCompleta = mensagemCompleta + nova_letra
        else:
            mensagemCompleta = mensagemCompleta + cadaLetra
    return mensagemCompleta

def decifrar(mensagem, chave):
    return cifrar(mensagem, -chave)

if opcao == "1":
    print("Criptografar uma mensagem! Vamos lá! ")
    mensagem = input("Digite a mensagem! ")
    chave = int(input("Digite a chave de deslocamento: "))
    resultado = cifrar(mensagem, chave)
    print("Mensagem criptografada: ", resultado)

elif opcao == "2":
    print("Descriptografar uma mensagem! Vamos lá!")
    mensagem = input("Digite a mensagem! ")
    chave = int(input("Digite a chave de deslocamento: "))
    resultado = decifrar(mensagem, chave)
    print("Mensagem descriptografada: ", resultado)

else:
    print("Opção inválida! Digite novamente 1 ou 2")