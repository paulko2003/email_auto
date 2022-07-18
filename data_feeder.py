
#currently we are getting the data by a file containing afm : email, then we search for the pdf with that afm.
import glob as gl
import os
import fnmatch as fn


class get_data_test_form:
    #init dict that contains the data in the form i want
    def __init__(self):
        self.my_dict= dict()
        self.pdfs_are_ok=dict() #gets every afm as key and pdf path as value 
        self.email_pdf=dict() # gets every email as key and value the pdf
        self.allafms=dict() #gets every afm as key and 0 as value
        self.afm_mail=dict() #gets every afm as key and email as value
    
    def fill_pdfs(self, folder: str):
        for filename in os.listdir(folder):
            self.pdfs_are_ok[filename[1:-4]]=os.path.join(folder,filename)
            self.allafms[str(filename[1:-4])]=0
            
    #gets all data from a txt file
    def strip_data(self, file: str): 
        with open(file,'r') as f:
            for line in f: 
                line=line.replace(' ','')
                line=line.replace('\n','')
                data=line.split(':') 
                self.afm_mail[data[0]]=data[1]
                self.allafms[str(data[0])]+=1

    def email_pdfcon(self):
        for key in self.afm_mail:
            self.email_pdf[self.afm_mail[key]]=self.pdfs_are_ok[key]

    def run(self,file="Testing/File_test/Test_file_1.txt",folder='Testing/PDF_files/pdf_files_1'):
        self.fill_pdfs(folder)
        self.strip_data(file)
        self.email_pdfcon()
        for key in self.allafms:
            if self.allafms[key]!=1:
                print(key,self.allafms[key])




               
                

                


if __name__ == '__main__':
    for i in range(1,11):
        print('file_'+str(i))
        get_data_test_form().run(file="Testing/File_test/Test_file_"+str(i)+".txt",folder='Testing/PDF_files/pdf_files_'+str(i))
