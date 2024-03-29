import string
import random
from password_config import policy
from password_blacklist import INVALID_PASSWORDS


def verificar_complexidade_pword(password):
    if password in INVALID_PASSWORDS:
        return False, "A password inserida é muito comum ou fácil de adivinhar. Por favor, insira outra."

    # Verificar se a password cumpre à política
    resultado = policy.test(password)
    if resultado:
        return True, "A password é forte."
    else:
        mensagem_user_visual = "A password é fraca. A password não atende aos critérios de complexidade: "
        if len(password) < 12:
            mensagem_user_visual += "A password deve ter pelo menos 12 caracteres. "
        if sum(1 for c in password if c.isupper()) < 3:
            mensagem_user_visual += "A password deve conter pelo menos 3 letras maiúsculas. "
        if sum(1 for c in password if c.isdigit()) < 3:
            mensagem_user_visual += "A password deve conter pelo menos 3 números. "
        if sum(1 for c in password if c in string.punctuation) < 3:
            mensagem_user_visual += "A password deve conter pelo menos 3 caracteres especiais. "

        # Sugestão
        caracteres = string.ascii_letters + string.digits + string.punctuation
        sugestao = ''.join(random.choices(caracteres, k=14))  # Sugestão com 14 caracteres

        mensagem_user_visual += "\nSugestão de password: " + sugestao
        return False, mensagem_user_visual


password_recebida = input("Digite a password: ")
verificacao, mensagem_user = verificar_complexidade_pword(password_recebida)
print(mensagem_user)
