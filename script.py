from password_strength import PasswordPolicy, PasswordStats
import string
import random


def verificar_complexidade_pword(password):
    # Definir a política de senha
    policy = PasswordPolicy.from_names(
        length=12,  # Mínimo de 12 caracteres
        uppercase=3,  # Pelo menos 3 letras maiúsculas
        numbers=3,  # Pelo menos 3 números
        special=3,  # Pelo menos 3 caracteres especiais
    )

    # Verificar se a password atende à política
    resultado = policy.test(password)
    if resultado:
        # Calcular estatísticas da senha
        stats = PasswordStats(password)
        if stats.strength() > 0.5:  # Força da senha deve ser maior que 0.5
            return True, "A password é forte."
        else:
            mensagem = "A password é fraca.\n"
            mensagem += "A password não atende aos critérios de complexidade:\n"
            if len(password) < 12:
                mensagem += "- A password deve ter pelo menos 12 caracteres.\n"
            if sum(1 for c in password if c.isupper()) < 3:
                mensagem += "- A password deve conter pelo menos 3 letras maiúsculas.\n"
            if sum(1 for c in password if c.isdigit()) < 3:
                mensagem += "- A password deve conter pelo menos 3 números.\n"
            if sum(1 for c in password if c in string.punctuation) < 3:
                mensagem += "- A password deve conter pelo menos 3 caracteres especiais.\n"
                # Sugestões baseadas na password inserida
                sugestoes = []
                caracteres = string.ascii_letters + string.digits + string.punctuation
                for _ in range(3):
                    sugestao = ''.join(random.choices(caracteres, k=12))
                    sugestoes.append(sugestao)

                mensagem += "\nSugestões baseadas na sua password:"
                for sugestao in sugestoes:
                    mensagem += "\n- " + sugestao

                return False, mensagem


password = input("Digite a password: ")
valida, mensagem = verificar_complexidade_pword(password)
print(mensagem)
