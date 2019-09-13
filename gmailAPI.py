import smtplib 
import LinkedinListings
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

LinkedinListings.get_results()
   
fromaddr = "XXX@XXX.com"
toaddr = "YYY@YYY.com"
body = "Here's a list of recent job openings that might be of interest to you"
subject = "Job Openings"
filename = "recent_top_results.xlsx"
attachment = open(r'C:/Users/XXX/Desktop/Python/recent_top_results.xlsx', "rb")

def send_mail(toaddr,fromaddr,body,subject,filename,attachment):
   
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr 
      
    # storing the receivers email address  
    msg['To'] = toaddr 
      
    # storing the subject  
    msg['Subject'] = subject
      
    # string to store the body of the mail 

    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
      
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
      
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
      
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    s.login(fromaddr, 'Gmail Password') 
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
      
    # terminating the session 
    s.quit() 

send_mail(toaddr,fromaddr,body,subject,filename,attachment)
