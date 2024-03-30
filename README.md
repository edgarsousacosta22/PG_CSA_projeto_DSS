#Verificação de Complexidade de Passwords

https://docs.servicenow.com/pt-BR/bundle/tokyo-platform-security/page/integrate/authentication/concept/password-complexity-requirements.html

Valida no input da password se ela não está na blacklist
Depois Verifica se cumpre os requisitos da politica escolhida no ficheiro config 
Se a password não cumprir os requisitos ele elabora uma sugestão.
Projeto para Verificação da Complexidade da Password

Autor: Edgar Costa
Ambito: Projeto Final de Desenvolvimento Seguro de Software | Pos Graduação em Cibersegurança Aplicada -UL-CUP
Versão: 

Descrição

Usando três ficheiros:
Blacklist.py
Config.py
Script.py

O Script verifica se a password inserida em linha de comandos cumpre com os requisitos de Policy usando duas bibliotecas importadas.
Os requisitos são definidos no script e podem ser alterados.

A linha policy.test(password) é responsável por verificar se a password fornecida atende aos critérios definidos na política de password.

A função test(password) verifica se a password fornecida cumpre todas as regras especificadas na política de password. Retorna True se a password atender a todas as regras e False caso contrário.

A variável policy é uma instância da classe PasswordPolicy que foi definida com base em critérios específicos, como comprimento mínimo, número mínimo de letras maiúsculas, números e caracteres especiais. A função test(password) é então chamada com a password fornecida como argumento para verificar se ela atende a esses critérios.

PasswordPolicy: Esta biblioteca é utilizado para definir uma política de password, especificando os critérios que uma password deve atender para ser considerada segura.

Além disso, também importei as bibliotecas `string` e `random`, que serão utilizados para gerar sugestões de password(não pedido).

PowerPoint incluido para ver a informação.

Edgar Costa a22312163
