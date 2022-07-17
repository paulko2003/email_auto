import random as ra
import os
from name_consts import ALPHABET, MAILS
#Parent class that creates basic test files 
class test_file_creator : 
        
    #a function that returns a -list with all the test file names
    def create_names(self, start: int, end: int):
        file_name=list()
        for i in range(start, end+1, 1):
            file_name+=["Test_file_"+str(i)]
        return file_name
    
    #creates and afm everytime its called
    def create_afm(self):
        afm=''
        afm+=str(ra.randint(0,1))
        for i in range(7): afm+= str(ra.randint(0,9))
        return afm
        
    #makes an email everytime its called
    def create_email(self):
        email=''
        name_len=ra.randint(5,15)
        for i in range(name_len):
            email+=ra.choice(ALPHABET)
        email+='@'
        email+=ra.choice(MAILS)
        return email
    
    #takes filename, creates it or appends to it at the end 
    #the txt will be in the form of "afm  :  email"
    def make_txt_file(self, current_afm: str, 
                                    current_email: str, file_name: str, 
                                    faulty: bool):
        
        if os.path.exists("File_test/"+file_name+'.txt'):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w' # make a new file if not

        with open("File_test/"+file_name+'.txt',  append_write) as file:
            if faulty and ra.randint(0,999) == 500: #adds 1/1000 chance to have a faulty afm  
                letter=current_afm[ra.randint(0,7)]
                current_afm=current_afm.replace(letter,'')
            file.write(current_afm+" : "+current_email+ '\n')

    #makes a direcotry that containts all the pdfs corresponding to a file 
    def make_pdf_dir(self, current_index):
        name="PDF_files/"+"pdf_files_"+str(current_index)+'/'
        os.mkdir(name)
        return name

    #makes an empty file with a .pdf extension so we can have something to send
    def make_pdf_file(self, current_afm, current_pdf_dir):
        try:
            current_start='Q'
            if ra.randint(1,3) == 2: 
                current_start='S' #adds a 1/3 chance for a pdf to start with an s instead of q
            open(current_pdf_dir+current_start+current_afm+'.pdf', 'a').close() 
        except Exception as e:
            print(e)


    #uses the functions to make the files i want to test 
    #takes range of files and if i want the files to have faults or no
    def run(self, start: int , end: int, numberOfPeople: int, faulty=False):
        names= self.create_names(start, end)
        for i in range(end - start):       #make (end - start) amount of files
            current_pdf_dir= self.make_pdf_dir(i)
            for j in range(numberOfPeople):#with (numberOfPeople) amount of lines
                current_afm=self.create_afm()
                current_email=self.create_email()
                self.make_txt_file(current_afm ,current_email, names[i], faulty)
                self.make_pdf_file(current_afm, current_pdf_dir)
                
#function that creates the files needed(used for cleaner code)
def Create_files(start= 0, end= 10, people= 4000, faulty= False):
    test_file_creator().run(start,end,people, faulty)

if __name__ == "__main__":
    Create_files()


    
