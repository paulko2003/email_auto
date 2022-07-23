from mailing.data_get import getter 
from mailing.send_mail import mailer
from make_test_files.make_files import make_files 
from mailing.path_consts import BASIC_Q_PATH, BASIC_XL_PATH, BASIC_S_PATH
from make_test_files.file_deleter import delete_files
from make_logs.logger import wipe

class work:
    def __init__(self,del_log=False, do_files= False, del_files= False, faulty=False, start=1, end=1):
        if do_files:
            make_files(starting=start, ending=end, issues=faulty)
        
        if del_files:
            delete_files()

        if del_log:
            wipe()



    #gets the data needed to run the program
    def get_data(self):
        self.get=getter()
        self.mail=mailer()
   
        ##returns a tuple with 2 pdf direcotries
    def to_pdf_dir(self, name):
        path_q=BASIC_Q_PATH+'/Q'+name+'.pdf'
        path_s=BASIC_S_PATH+'/S'+name+'.pdf'
        return (path_q,path_s)

    #makes it take data and send an email
    def run(self):
        get_data()
        for index,key in enumerate(self.get.sending):
            if self.get.willSend[key]:      #if it can be send it makes the direcotry and feeds it to the mailer
               path_q,path_s=self.to_pdf_dir(key) 
               self.mail.send_one_email(index+1,path_q,path_s)




if __name__ == "__main__":
    work(del_files=True)
