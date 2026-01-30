# PythonEmail

A simple Python script for sending emails with attachments using SMTP.

## Features

- Send emails with custom subject and body
- Attach files to emails
- Support for SMTP authentication
- Configurable SMTP server settings

## Requirements

- Python 3.6+
- No external dependencies (uses standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/gitjavidal/PythonEmail.git
cd PythonEmail
```

2. Configure your email settings (see Configuration section)

## Configuration

Before using the script, you need to configure your email settings. You have two options:

### Option 1: Environment Variables (Recommended)

Set the following environment variables:

```bash
export SMTP_SERVER='smtp.gmail.com'
export SMTP_PORT='587'
export SMTP_USERNAME='your_email@gmail.com'
export SMTP_PASSWORD='your_password'
export EMAIL_TO='recipient@example.com'
```

### Option 2: Configuration File

Copy `config.example.py` to `config.py` and edit it with your settings:

```bash
cp Desktop/pyEmail/config.example.py Desktop/pyEmail/config.py
```

**Important:** Never commit `config.py` with real credentials to version control!

## Usage

```bash
cd Desktop/pyEmail
python send_email.py
```

## Security Notes

- Never commit your credentials to version control
- Use environment variables or a configuration file that is listed in `.gitignore`
- For Gmail, you may need to use an App Password instead of your regular password
- Consider using OAuth2 for production applications

## License

This project is open source and available under the MIT License.
