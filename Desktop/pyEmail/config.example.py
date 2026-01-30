# Example configuration file for PythonEmail
# Copy this file to config.py and fill in your actual credentials
# DO NOT commit config.py to version control!

# SMTP server configuration
SMTP_SERVER = 'smtp.example.com'  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587  # 587 for TLS, 465 for SSL

# Email credentials
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'  # Use app password for Gmail

# Email details
EMAIL_FROM = 'your_email@example.com'
EMAIL_TO = 'recipient@example.com'
EMAIL_SUBJECT = 'Asunto del correo'

# Message body
EMAIL_BODY = 'Este es el contenido del correo electrónico.'

# Attachment (optional, leave empty if no attachment)
ATTACHMENT_FILE = ''  # e.g., 'archivo_adjunto.txt'
