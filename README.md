# Versão do Python=3.9.13

### É aconselhável a criação de um ambiente virtual:

1. Vá até a pasta que fez pull, abra o terminal e digite `python -m venv venv`
2. Após a criação, digite `./venv/Script/activate` para ativar o abiente virtual
3. Por fim, para instalar todas as bibliotecas necessárias, basta utilizar o comando `pip install -r "requirements.txt"`

# Como funciona

Basta editar a planilha localizada na pasta **arquivos**. Não altere o título das colunas (PARA, ASSUNTO, CORPO) isso ocorrerá em erro do programa.

# Como executar

Crie um arquivo na raiz do projeto com o nome **.env** para evitar de deixar dados sensíveis no projeto, e preencha da seguinte forma:
```
EMAIL_HOST=email_rementente@email.com
PASS_HOST=senha do email
```
Após isso, basta executar o arquivo *main.py*
