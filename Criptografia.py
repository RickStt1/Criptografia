# Implementação de diferentes tipos de criptografia

# pt 1 Cifre de Cesar
def cifra_de_cesar(texto, chave, modo='criptografar'):
    """Criptografa ou descriptografa um texto usando a Cifra de Cesar."""
    resultado = ''
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra
            deslocamento = chave if modo == 'criptografar' else -chave  # Define o deslocamento, sem IF modo descriptografar, simplifiquei com -chave
            base = ord('A') if char.isupper() else ord('a') # Define a base para letras maiúsculas ou minúsculas
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)  # Aplica o deslocamento e deixa dentro do alfabeto
        else:
            resultado += char  # caracteres não alfabeticos não mudam
    return resultado

# pt 2 Cifra de Vigenère
def cifra_de_vigenere(texto, chave, modo='criptografar'):
    """Criptografa ou descriptografa um texto usando a Cifra de Vigenere."""
    resultado = ''
    chave = chave.lower()  # Converte a chave para minúsculas para padronização
    chave_index = 0 
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra
            deslocamento = ord(chave[chave_index % len(chave)]) - ord('a')  # Define o deslocamento baseado na chave
            if modo == 'descriptografar':
                deslocamento = -deslocamento  # Inverte o deslocamento na descriptografia
            base = ord('A') if char.isupper() else ord('a')  # Define a base para letras maiúsculas ou minúsculas
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)  # Aplica o deslocamento
            chave_index += 1  # Avança o índice da chave
        else:
            resultado += char  # Mantém caracteres não alfabéticos inalterados
    return resultado

# pt 3 XOR
def cifra_xor(texto, chave):
    """Criptografa ou descriptografa um texto usando XOR."""
    return ''.join(chr(ord(char) ^ ord(chave[i % len(chave)])) for i, char in enumerate(texto))
# eu to até agora tentando entender como isso funciona, e ja são 3 da manhã
# essas ultimas 3 linhas de codigo simplesmente não foram eu, pra mim não tem o menor sentido
# eu finalmente entendi (não completamente, mas ja serve)

# escolher criptografia
def escolha_tipo_criptografia():
    """Permite ao usuário escolher o tipo de criptografia."""
    print("\nEscolha o tipo de criptografia:")
    print("1 - Cifra de César")
    print("2 - Cifra de Vigenère")
    print("3 - Cifra XOR")
    print("4 - Sair")
    
    while True:
        opcao = input("Digite a opção desejada: ").strip()
        if opcao in ['1', '2', '3', '4']:
            return int(opcao)
        print("Opção inválida! Tente novamente.")

# pra deixar bonito
if __name__ == "__main__":
    while True:
        print("\n=== Escolha a ação ===")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Sair")
        
        opcao = input("Digite a opção desejada: ").strip()  # Solicita a opção do usuário
        if opcao == '3':  # Sai do programa se o usuário escolher 3
            break
        if opcao not in ['1', '2']:  # se não for o que esta em [] o programa vai te barrar
            print("Opção inválida! Tente novamente.")
            continue
        
        modo = 'criptografar' if opcao == '1' else 'descriptografar'  # Define o modo
        tipo_criptografia = escolha_tipo_criptografia()  # tipo de criptografia
        if tipo_criptografia == 4:  # o programa para
            break
        
        texto = input("Digite o texto: ")  # Solicita o texto ao usuário
        
        if tipo_criptografia == 1:  # Cifra de César
            chave = int(input("Digite a chave (número inteiro): "))
            resultado = cifra_de_cesar(texto, chave, modo)
        elif tipo_criptografia == 2:  # Cifra de Vigenère
            chave = input("Digite a chave (palavra): ")
            resultado = cifra_de_vigenere(texto, chave, modo)
        elif tipo_criptografia == 3:  # Cifra XOR
            chave = input("Digite a chave (palavra): ")
            resultado = cifra_xor(texto, chave)
        
        print(f"Texto {modo}: {resultado}") 
