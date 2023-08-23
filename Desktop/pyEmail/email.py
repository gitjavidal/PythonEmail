import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuración del servidor SMTP y credenciales
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'tu_correo@example.com'
smtp_password = 'tu_contraseña'

# Crear objeto MIME para el correo electrónico
msg = MIMEMultipart()
msg['From'] = 'tu_correo@example.com'
msg['To'] = 'destinatario@example.com'
msg['Subject'] = 'Asunto del correo'

# Agregar el cuerpo del correo
body = 'Este es el contenido del correo electrónico.'
msg.attach(MIMEText(body, 'plain'))

# Adjuntar un archivo
filename = 'archivo_adjunto.txt'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename= {filename}')
msg.attach(part)

# Establecer la conexión con el servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Enviar el correo electrónico
    server.sendmail(smtp_username, msg['To'], msg.as_string())
    print('Correo electrónico con adjunto enviado exitosamente')

except Exception as e:
    print('Error al enviar el correo electrónico:', e)

finally:
    # Cerrar la conexión con el servidor SMTP
    server.quit()
