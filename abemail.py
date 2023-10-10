"""
Sends email
"""

import smtplib
from loguru import logger
from status import status
from config import EMAIL


def backup_email():
    """
    Sends e-mail
    """
    global status

    # Message parameters
<<<<<<< HEAD
    subject = 'There are errors in ABACKUP at tst.crm-salon.ru!'
=======
    subject = 'There are errors in ABACKUP!'
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300
    text = 'There are errors in methods listed below. For details see logs. \r\n'
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
        % (EMAIL.FROM_ADDRESS.value, EMAIL.TO_ADDRESS.value, subject))
    msg += text + ', '.join(status.keys())

    # Connect to smtp-server
    try:
        server = smtplib.SMTP_SSL(f"{EMAIL.SERVER.value}:{EMAIL.PORT.value}")
    except smtplib.SMTPConnectError:
        logger.error('Could not connect to smtp-server, message is not sent.' + server.noop())
        return None

    logger.success('Connected to smtp-server, response is ' + ','.join(map(str, server.noop())))
<<<<<<< HEAD

=======
    
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300
    # Login to smtp-server
    try:
        server.login(EMAIL.LOGIN.value, EMAIL.PASSWORD.value)
    except smtplib.SMTPAuthenticationError:
        logger.error('Authentication error, message is not sent. ' + ','.join(map(str, server.noop())))
        return None  
    logger.success('Login to smtp-server ' + ','.join(map(str, server.noop())))

    server.set_debuglevel(False)
<<<<<<< HEAD

=======
    
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300
    # Send email
    try:
        server.sendmail(EMAIL.FROM_ADDRESS.value, EMAIL.TO_ADDRESS.value, msg)
    except smtplib.SMTPRecipientsRefused:
        logger.error('Recipients refused, message is not sent. ' + ','.join(map(str, server.noop())))
        return None
    except smtplib.SMTPSenderRefused:
        logger.error(f'From address {EMAIL.FROM_ADDRESS.value} is refused, message is not sent. ' + ','.join(map(str, server.noop())))
<<<<<<< HEAD
        return None
    except Exception as e:
        logger.error(f'SMTP error {e}, message is not sent. ' + ','.join(map(str, server.noop())))
        return None

    # Close connection
    server.quit()
    logger.success('Error message sent to ' + EMAIL.TO_ADDRESS.value)
=======
        return None        
    except Exception as e:
        logger.error(f'SMTP error {e}, message is not sent. ' + ','.join(map(str, server.noop())))
        return None        
    
    # Close connection
    server.quit()
    logger.success('Error message sent to ' + EMAIL.TO_ADDRESS.value)

>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300
