import random as ra
from name_consts import ALPHABET, MAILS
#Parent class that creates basic test files 
class test_file_create : 

    #takes range of file names
    def __init__(self, start: int , end: int, numberOfPeople: int): 
        self.numberOfPeople=numberOfPeople
        self.start= start
        self.end= end
        self.amount= end-start
        self.run()
        
    #a function that returns a -list with all the test file names
    def create_names(self):
        file_name=list()
        for i in range(self.start, self.end+1, 1):
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
    
    #makes a file which can have errors with numberOfPeople number of lines
    def make_file(self, name, faulty=False):
        with open("File_test/"+name+'.txt', 'w') as file:
            for i in range(self.numberOfPeople):
                current_afm=self.create_afm()
                current_email=self.create_email()
                if not faulty and ra.randint(0,1000) == 500: #adds 1/1001 chance to have a faulty afm or mail 50/50
                    for
                    
                file.write(current_afm+" : "+current_email + '\n')
    
    #makes all the basic files i want to test     
    def run(self):
        names= self.create_names()
        for i in range(self.amount):
            self.make_file(names[i])    
            


if __name__ == "__main__":
    test_file_create(0,10,4000)


    
