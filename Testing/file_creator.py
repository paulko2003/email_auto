import random as ra
from name_consts import ALPHABET, MAILS
#Parent class that creates basic test files 
class test_file_creator : 
        
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
    def make_file(self, name, faulty):
        with open("File_test/"+name+'.txt', 'w') as file:
            for i in range(self.numberOfPeople):
                faulty_check=''
                current_afm=self.create_afm()
                current_email=self.create_email()
                if faulty and ra.randint(0,999) == 500: #adds 1/1000 chance to have a faulty afm  
                    letter=current_afm[ra.randint(0,7)]
                    current_afm=current_afm.replace(letter,'')
                    faulty_check="  hehe im faulty mi puta"
                file.write(current_afm+" : "+current_email+ faulty_check + '\n')
    
    #uses the functions to make the files i want to test 
    #takes range of files and if i want a file to have faults or no
    def run(self, start: int , end: int, numberOfPeople: int, faulty=False):
        self.numberOfPeople=numberOfPeople
        self.start= start
        self.end= end
        self.amount= end-start
        self.faulty=False
        names= self.create_names()
        for i in range(self.amount):
            self.make_file(names[i],faulty)    
            


if __name__ == "__main__":
    test_file_creator().run(0,10,4000, faulty=True)



    
