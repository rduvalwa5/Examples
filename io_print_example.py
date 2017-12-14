'''
    Printing to the Screen
    The simplest way to produce output is using the print statement where you can pass 
    zero or more expressions separated by commas. This function converts the expressions 
    you pass into a string and writes the result to standard output as follows
    @author: rduvalwa2
'''
import glob
import os

class my_print:        
        def __init__(self):
            self.strIn = "No Input"
        
        def pr_print(self, strIn = "NoString"):
            print(strIn)
            
        def print_input(self):
            self.pr_print(self.strIn)
            
        def get_input(self):
            self.strIn = input("Enter your input: ")

        def file_open(self):
            valid_modes = ['w','w+','wb','wb+','r','r+','rb','rb+','a','a+','ab','ab+']
            file_name = input("Enter file name: ")
            file_mode = input("Enter file mode: ")
            if (file_mode not in valid_modes):
                print("Invalid mode", file_mode)
                exit()
            if os.path.isfile(file_name):
                fo = open(file_name,file_mode)
                fo.write("G'day Bruce\nHello sweetheart\nLet my heart go\n")
                fo.close()
                fo = open(file_name,'r')
                content = fo.readlines()
                print(content)
                print ("Name of the file: ", fo.name)
                print ("Closed or not : ", fo.closed)
                print ("Opening mode : ", fo.mode)
                print ("Softspace flag : ", fo.softspace)
            else:
                print('File ' ,file_name, 'does not exist')
                fo = open(file_name, 'w')
                fo.write("G'day Brucie\nHello sweetheart\nLet my heart go\n")
                fo.close()
            fo = open(file_name,'r')
            content = fo.readlines() 
            print(content)
            fo.close()
            print ("Closed or not : ", fo.closed)

if __name__ == '__main__':
    mystring = "New string with punctuation! What do you think? No way."
    
    pr = my_print()
    pr.pr_print(mystring)
    pr.pr_print()
    pr.print_input()
#    pr.get_input()
#    pr.print_input()
    pr.file_open()
        
'''
C1246895-osx:src rduvalwa2$ python print_example.py 
New string with punctuation! What do you think? No way.
NoString
No Input
Enter your input: "Yes in"
Yes in

'''