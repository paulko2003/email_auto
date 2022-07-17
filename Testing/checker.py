# this is meant to check tha the data is in the right form
# here the data will be taken in the form of a dict made from the "data_feeder.py" file e.x (afm: "my afm", email: "my email", pdf: "my email")
# here basic checks are made to see if the afm is = 8 and that the pdf file has the correct afm in case anything happens

    
def dict_check(my_dict: dict):
    if len(my_dict["afm"]) < 8:
        print("afm has less than 8 characters")
        return False
    if len(my_dict['afm'])>8:
        print("afm has more than 8 characters")
    #we have no way to check emails
    if my_dict["afm"] in my_dict["pdf"]:
        print("pdf does not match afm")
