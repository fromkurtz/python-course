# Enviando Email SMTP com Python
import os
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib

from dotenv import load_dotenv

load_dotenv()

# Caminho HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula185.html'

# Dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configuracoes SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    Template = Template(texto_arquivo)
    texto_email = Template.substitute(nome='Joao')

# Tranformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Teste'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)


# Enviando o E-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')
