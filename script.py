from password_strength import PasswordPolicy, PasswordStats
import string
import random


def verificar_complexidade_pword(password):
    # Definir a política de password segura
    policy = PasswordPolicy.from_names(
        length=12,  # Mínimo de 12 caracteres
        uppercase=3,  # Pelo menos 3 letras maiúsculas
        numbers=3,  # Pelo menos 3 números
        special=3,  # Pelo menos 3 caracteres especiais
    )

    # Verificar se a password cumpre à política
    resultado = policy.test(password)
    if resultado:
        # Calcular estatísticas da password
        stats = PasswordStats(password)
        if stats.strength() > 0.5:  # Força da password deve ser maior que 0.5
            return True, "A password é forte."
        else:
            mensagem_user_visual = "A password é fraca.\n"
            mensagem_user_visual += "A password não atende aos critérios de complexidade:\n"
            if len(password) < 12:
                mensagem_user_visual += "- A password deve ter pelo menos 12 caracteres.\n"
            if sum(1 for c in password if c.isupper()) < 3:
                mensagem_user_visual += "- A password deve conter pelo menos 3 letras maiúsculas.\n"
            if sum(1 for c in password if c.isdigit()) < 3:
                mensagem_user_visual += "- A password deve conter pelo menos 3 números.\n"
            if sum(1 for c in password if c in string.punctuation) < 3:
                mensagem_user_visual += "- A password deve conter pelo menos 3 caracteres especiais.\n"
                # Sugestões baseadas na password inserida
                sugestoes = []
                caracteres = string.ascii_letters + string.digits + string.punctuation
                for _ in range(3):
                    sugestao = ''.join(random.choices(caracteres, k=12))
                    sugestoes.append(sugestao)

                mensagem_user_visual += "\nSugestões baseadas na sua password:"
                for sugestao in sugestoes:
                    mensagem_user_visual += "\n- " + sugestao

                return False, mensagem_user_visual


password_recebida = input("Digite a password: ")
valida, mensagem_user = verificar_complexidade_pword(password_recebida)
print(mensagem_user)
