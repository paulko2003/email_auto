from make_test_files.file_creator import Create_files 
from make_test_files.file_deleter import delete_files



#class used to make the files i want to make
class make_files:
    def __init__(self, starting=0, ending=1, issues=False,has_pdf=True, has_xls=True):
        delete_files()
        Create_files(start= starting, end= ending, faulty= issues, has_txt=has_xls, has_pdfs=has_pdf)


if __name__ == "__main__":
   make_files() 
    
