# Lista de passwords inválidas/faceis comuns que são expostas em várias plataformas
INVALID_PASSWORDS = []

# Abrir e ler o arquivo .txt com as senhas inválidas
with open('invalid_passwords.txt', 'r', encoding='utf-8') as file:
    for line in file:
        INVALID_PASSWORDS.append(line.strip())