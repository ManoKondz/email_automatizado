import smtplib
import email.message
print("Após enviar, espere alguns segundos para confirmação")
assunto_email = input("Digite o assunto do email:\n")
print
print("Para criar um parágrafo utilize:")
def enviar_email():
    corpo_email = input("""
Para criar um parágrafo utilize:
<p>Parágrafo1</p>
<p>Parágrafo2</p>
    """)

    msg = email.message.Message()
    msg['Subject'] = assunto_email
    msg['From'] = 'remetente'
    msg['To'] = 'destinatário'
    password = 'senha'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()