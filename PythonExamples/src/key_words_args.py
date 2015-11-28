'''
Created on Mar 8, 2013
@author: rduvalwa2
Demonstrates capture keyword arguments
first function, keywords(), iterates over the keys of the dict, printing the keys 
(which are the names of the unmatched keyword arguments) and the associated values
 (which are the values following the equals signs). 
 '''
def keywords(**kwargs): #this is an example of dict-parameter
    "Prints the keys and arguments passed through"
    for key in kwargs:
        print("Printing   " "{0}: {1} ".format(key, kwargs[key]))
"""second function, keywords_as_dict(), just prints the keyword arguments, demonstrating that the dict-parameter is in fact a dict."""     
def keywords_as_dict(**kwargs):
    "Prints the keyword arguments as a dict"
    return kwargs
     
if __name__ == "__main__":
    keywords(guido="Founder of Python", python="Used by NASA and Google",Dennis_Ritchie="Founder of C", C="Used to develop Unix")
    print(keywords_as_dict(guido="Founder of Python", python="Used by Nasa and Google",Dennis_Ritchie ="Founder of C", C="Used to develop Unix"))