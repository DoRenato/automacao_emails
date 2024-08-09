import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(host_email, host_pass, dest_email, subject, body_email, smtp_host='smtp.gmail.com', smtp_port=587):
    msg = MIMEMultipart()
    msg['From'] = host_email
    msg['To'] = dest_email
    msg['Subject'] = subject
    body = body_email
    msg.attach(MIMEText(body, 'plain'))
    texto = msg.as_string()
    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()  # Configura o servidor para usar TLS
        server.login(host_email, host_pass)  # Tenta autenticar
        server.sendmail(host_email, dest_email, texto)
        print("E-mail enviado com sucesso!")
    except smtplib.SMTPAuthenticationError as e:
        print("Erro de autenticação:", e)
    finally:
        server.quit()  # Fecha a conexão com o servidor