import pandas as pd
from decouple import config

from functions import send_email

df = pd.read_excel('arquivos/emails_para_enviar.xlsx')

# Configurações do servidor de e-mail
smtp_host = 'smtp.gmail.com'  # servidor SMTP, ex: smtp.gmail.com para Gmail
smtp_port = 587  # porta do servidor SMTP, para gmail os padrões são 25, 465 ou 587
email_user = config('EMAIL_HOST')
email_password = config('PASS_HOST')

for index, row in df.iterrows():
    email_dest = row['Para']
    assunto=row['Assunto']
    corpo=row['Corpo']

    novo_email=send_email(email_user, email_password, email_dest,assunto,corpo)