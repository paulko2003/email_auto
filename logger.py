from logging_path import ISSUES, SENT_WELL

#if true goes to the good ones if false goes to the issues
def logging(addition: str,is_ok: bool):
    addition+='\n'
    if is_ok:
        with open(SENT_WELL,'a') as file:
            file.write(addition)
    else:
        with open(ISSUES,'a') as file:
            file.write(addition)

        
