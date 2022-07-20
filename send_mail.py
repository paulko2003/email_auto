#this files contains the class that is responsible for how emails will be constracted
#contains function send_one_email that you call everytime you want to send an email
#the class should be instantiated with Test= False if you want to send emails
#__main__ is only used for testing to see for 1 file if something is wrong
#here is used to make the logs for what happened to the emails
import smtplib 
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv, find_dotenv
from emailing_log.logger import logging

class mailer:
    #when object is made gets env variables and establishes an smpt conection/login
    def __init__(self,Test=True):
        load_dotenv()
        logging('\n\n -----new run-----\n\n', True)       #starts a new segment in 
        logging('\n\n -----new run-----\n\n', False)      #both files for new run
        self.Test=Test
        self.my_email= os.environ.get('test_email')
        self.my_password= os.environ.get('test_email_pass')    
        self.my_conection= self._init_conection()

    

    #starts a conection with localhost for test or gmail for real
    #returns None if conection couldnt be established
    def _init_conection(self):
        if self.Test:
            conection= smtplib.SMTP('localhost', 1025) 
        else:
            try:
                conection=smtplib.SMTP_SSL('smtp.gmail.com',465)
                conection.login(self.my_email,self.my_password)
                self.my_password=None
            except Exception as e:
                msg="conection not established"
                print(e)
                print(msg)
                logging(str(e),False)
                logging(msg,False)
                conection=None
        return conection
        

    
    #adds pdfs into the email content or returns None so nothing will be sent
    def _add_atach(self,pdf1_dir: str,pdf2_dir: str, email_content, current_email: int):
        for c_file in [pdf1_dir, pdf2_dir]: #just 2 iterations with c_file being equal to each dir
            try:
                with open(c_file,'rb') as file:
                    file_data=file.read()
                    file_name=c_file.split('/')[-1]   #pdf1_dir variable will be in the form of (curent_dir/next_dir/next_next_dir/pdfname.pdf) so we take the last element after the /        
                email_content.add_attachment(file_data, maintype='application', subtype='octet-stream',filename=file_name)
                msg=f'added file {file_name} to the email'
                logging(msg,True)
                print(msg)
            except Exception as e:
                msg=f"email number {current_email+1}. Had issues, the email was going to be sent to: {email_content['To']}"
                logging(str(e),False)
                logging(msg, False)
                print(e)
                print(msg)#catches error reports it and returns 0
                return None
        return email_content #all went okay and returns email with attachments

    #sets_content for our email (takes relative dirs to our pdf files)
    def _set_content(self,current_mail_number: int,pdf1_dir: str,pdf2_dir: str,Subject: str,Content: str, From,To ):
        email_content=EmailMessage()
        if From== None:
            From=self.my_email
        if To == None:
            To= self.my_email
        email_content['From']=From
        email_content['To']=To
        email_content['Subject']= Subject
        email_content.set_content(Content)
        email_content=self._add_atach(pdf1_dir,pdf2_dir,email_content,current_mail_number) # feeds relative dir for pdfs and adds them to email content 
        return email_content
    
    #basic function used to check if email will be sent or no returns true false(its the last check mainly for failing to locate a dir all other checks are in data_feeder)
    def _can_send(self, email_content ):
        if email_content == None:
            return False
        return True

    #checks if there is an established smpt connection before setting content or doing anything
    def _conected(self):
        if self.my_conection == None:
            return False
        return True

    #is used before sending any email
    def _new_mail_print(self):
        print('')
        print("--------------------------------")
        print('')

    
    #Is called everytime to send an email with the 2 pdfs, returns None incase there was not a conection established
    def send_one_email(self,current_email_number: int ,pdf1_dir: str,pdf2_dir: str,Subject="this email is from digital cate",Content="here are your 2 pdfs", From= None , To = None): 
        if not self._conected():
            msg= 'no connection established to send an email'
            logging(msg,False)
            print(msg)
            return None
        self._new_mail_print()
        my_email=self._set_content(current_email_number,pdf1_dir,pdf2_dir,Subject,Content, From, To)
        if self._can_send(my_email) and self.my_conection!= None:
            try:
                self.my_conection.send_message(my_email)
                msg=f"email number {current_email_number+1} sent to {my_email['To']}"
                logging(msg,True)
                print(msg)
            except Exception as e: 
                print(e)
                msg="issue delivering the email"
                logging(msg, False)
                print(msg)
                logging('\n',False)
                return False
            logging('\n',True)
            return True        #returns true if sent, false if inside exception or outside if(was none
        logging('\n',False)         
        return False 
            


if __name__ == "__main__":
    email=mailer(Test= False)
    for i in range (500):
        dir1='Testing/PDF_files/pdf_files_1/Q00018391.pdf'
        dir2='Testing/PDF_files/pdf_files_1/Q00420534.pdf'
        if i== 342:
            dir1='random dir lol'
        email.send_one_email(i,dir1,dir2)






