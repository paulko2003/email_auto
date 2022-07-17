#deletes files existing in the File_test folder so we dont get the previous files
import os, shutil

def deleter(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def delete_files():
    deleter("PDF_files")
    deleter("File_test")

if __name__ == "__main__":
    delete_files()
