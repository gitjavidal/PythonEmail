import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Intentar cargar configuración desde archivo config.py o variables de entorno
try:
    from config import (
        SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD,
        EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_BODY, ATTACHMENT_FILE
    )
except ImportError:
    # Si no existe config.py, usar variables de entorno
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.example.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', 'your_email@example.com')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'your_password')
    EMAIL_FROM = os.getenv('EMAIL_FROM', SMTP_USERNAME)
    EMAIL_TO = os.getenv('EMAIL_TO', 'recipient@example.com')
    EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT', 'Asunto del correo')
    EMAIL_BODY = os.getenv('EMAIL_BODY', 'Este es el contenido del correo electrónico.')
    ATTACHMENT_FILE = os.getenv('ATTACHMENT_FILE', '')


def send_email(smtp_server, smtp_port, smtp_username, smtp_password,
               email_from, email_to, subject, body, attachment_file=None):
    """
    Envía un correo electrónico con soporte opcional para archivos adjuntos.
    
    Args:
        smtp_server: Servidor SMTP
        smtp_port: Puerto SMTP
        smtp_username: Usuario SMTP
        smtp_password: Contraseña SMTP
        email_from: Remitente
        email_to: Destinatario
        subject: Asunto del correo
        body: Cuerpo del correo
        attachment_file: Ruta al archivo adjunto (opcional)
    
    Returns:
        bool: True si el correo se envió exitosamente, False en caso contrario
    """
    # Crear objeto MIME para el correo electrónico
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject

    # Agregar el cuerpo del correo
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar un archivo si se especifica
    if attachment_file and os.path.exists(attachment_file):
        try:
            with open(attachment_file, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                filename = os.path.basename(attachment_file)
                part.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(part)
            print(f'Archivo adjunto añadido: {attachment_file}')
        except Exception as e:
            print(f'Error al adjuntar archivo: {e}')
            return False
    elif attachment_file:
        print(f'Advertencia: El archivo {attachment_file} no existe. Se enviará el correo sin adjunto.')

    # Establecer la conexión con el servidor SMTP
    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Enviar el correo electrónico
        server.sendmail(email_from, email_to, msg.as_string())
        print('Correo electrónico enviado exitosamente')
        return True

    except smtplib.SMTPAuthenticationError:
        print('Error de autenticación: Verifica tu usuario y contraseña')
        return False
    except smtplib.SMTPException as e:
        print(f'Error SMTP al enviar el correo electrónico: {e}')
        return False
    except Exception as e:
        print(f'Error al enviar el correo electrónico: {e}')
        return False

    finally:
        # Cerrar la conexión con el servidor SMTP
        if server:
            try:
                server.quit()
            except Exception:
                pass


if __name__ == '__main__':
    # Validar que la configuración no sea la predeterminada
    if SMTP_USERNAME == 'your_email@example.com' or SMTP_PASSWORD == 'your_password':
        print('Error: Por favor configura tus credenciales de correo electrónico.')
        print('Puedes hacerlo de dos formas:')
        print('1. Copia config.example.py a config.py y edita los valores')
        print('2. Define las variables de entorno SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_TO')
        exit(1)
    
    # Enviar el correo
    success = send_email(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        smtp_username=SMTP_USERNAME,
        smtp_password=SMTP_PASSWORD,
        email_from=EMAIL_FROM,
        email_to=EMAIL_TO,
        subject=EMAIL_SUBJECT,
        body=EMAIL_BODY,
        attachment_file=ATTACHMENT_FILE if ATTACHMENT_FILE else None
    )
