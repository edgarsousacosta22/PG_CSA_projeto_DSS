from password_strength import PasswordPolicy

# Definir a política de password segura
policy = PasswordPolicy.from_names(
    length=12,  # Mínimo de 12 caracteres
    uppercase=3,  # Pelo menos 3 letras maiúsculas
    numbers=3,  # Pelo menos 3 números
    special=3,  # Pelo menos 3 caracteres especiais
)