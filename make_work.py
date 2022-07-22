from data_get import getter 
from send_mail import mailer



class work:
    def __init__(self):
        self.get=getter()
        self.mail=mailer(Test=False)
    
    ##returns a tuple with 2 pdf direcotries
    def to_pdf_dir(self, name, direcotry= 'Testing/PDF_files/pdf_files_1/'):
        path_q=direcotry+'questions/Q'+name+'.pdf'
        path_s=direcotry+'items/S'+name+'.pdf'
        return (path_q,path_s)

    #makes it take data and send an email
    def run(self):
        for index,key in enumerate(self.get.sending):
            if self.get.willSend[key]:      #if it can be send it makes the direcotry and feeds it to the mailer
               path_q,path_s=self.to_pdf_dir(key) 
               self.mail.send_one_email(index,path_q,path_s)





if __name__ == "__main__":
    work().run()
