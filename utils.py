import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PyPDF2 import PdfWriter
import os

# Delete PDF files in a directory
def delete_pdfs(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            os.remove(os.path.join(directory, filename))

def merge_pdfs(pdf_files):
    # Check if the output PDF file exists.
    if os.path.exists("analise.pdf"):
        # Delete the output PDF file if it exists.
        os.remove("analise.pdf")

    merger = PdfWriter()

    for pdf_file in pdf_files:
        # Check if the input PDF file exists.
        if not os.path.exists(pdf_file):
            raise FileNotFoundError(f"File not found: {pdf_file}")
        
        input1 = open(pdf_file, "rb")
        merger.append(input1)
    
    merger.write('analise.pdf')
    merger.close()
    

def send_email_with_attachment(recipient, page_html):
    # Access the user email and password from the secrets.toml file
    sender = st.secrets["email"]
    password = st.secrets["password"]
    # Create a connection to the SMTP server.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Authenticate the connection.
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)

    # Create a MIME multipart message.
    message = MIMEMultipart()
    message["Subject"] = "Relatório de maturidade de dados"
    message["From"] = sender
    message["To"] = recipient

    print(page_html)
    # Convert the page HTML to a string.
    # html_body = MIMEText(page_html, 'html')
    # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
    message.attach(MIMEText(page_html, "html"))
    # Convert it as a string
    email_string = message.as_string()
    # Add the HTML body to the message.
    # message.attach(html_body)


    # Open the attachment file in read mode.
    #with open(attachment_file_path, "r") as f:
     #   attachment_data = f.read()
        # Create a MIMEText object with the HTML code as the payload and the `subtype='html'` argument.
      #  html_body = MIMEText(attachment_data)
       # message.attach(html_body)

    # Send the email.
    server.sendmail(sender, recipient, email_string)
    server.quit()
    