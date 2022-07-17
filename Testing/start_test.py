from file_creator import Create_files 
from file_deleter import delete_files



if __name__ == "__main__":
    delete_files() # start by deleting previous files
    Create_files() # makes files needed for the test 
    
    
