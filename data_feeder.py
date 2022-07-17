#this script it made as an api between how we get the data and how its being fed to the code
#whenever the end function is called there needs to be returned a dict in the form of (afm: "my afm", email: "my email", pdf: "my email")
#currently we are getting the data by a file containing afm : email, then we search for the pdf with that afm.

import os
import fnmatch as fn


class get_data_test_form:
    #init dict that contains the data in the form i want
    def __init__(self):
        self.my_dict= dict()
    
    #gets the data from each line and saves it to my_dict
    def strip_data(self, line: str): 
        email=''
        afm=''
        passed=False
        line=line.replace(' ','')
        line=line.replace('\n','')
        for i in line:
            if i==':':
                passed=True
            elif not passed:
                afm+=i
            else:
                email+=i
        self.my_dict['afm']=afm
        self.my_dict['emai']=email

        

    #searches and returns file path if exists if not returns empty string ''
    def pdf_file_search(self, folder: str, afm: str):
        path=''
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if fn.fnmatch(file_path,'*'+afm+'*'):
                    path=file_path
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        return path

    def _test(self,file_path= 'Testing/File_test/Test_file_1.txt',file_pdfs='Testing/PDF_files/pdf_files_1'):
        with open(file_path) as file:
            for index,line in enumerate(file):
                self.strip_data(line)
                print(index)
                if not self.pdf_file_search(file_pdfs,self.my_dict["afm"]):
                    print(f"issue in {  line  }")
                

                


if __name__ == '__main__':

    get_data_test_form()._test()
