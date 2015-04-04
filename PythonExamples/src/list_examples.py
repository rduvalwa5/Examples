'''
Created on Apr 2, 2015
http://www.tutorialspoint.com/python/python_lists.htm
@author: rduvalwa2
'''
class listExample:
    
    def createList(self,seq):
        theList = []
        for item in seq:
            theList.append(item)
        return theList
    
    def appendToList(self,aList,obj):
        aList.append(obj)
        return aList
    
    def reverseMylist(self,lst):
        lst.reverse()
        return lst
    
    def removeItem(self,theList,theItem):
        theList.remove(theItem)
        return theList
        
    def insertIntoList(self,theList,position,theItem):
        theList.insert(position,theItem)
        return theList

    def extendList(self,theList,theItem):
        theList.extend(theItem)
        return theList    
    
    
if __name__ == "__main__":
    from array import array
    arSeq = ("a","b","d")
    myArray = array('u',arSeq)

    
    
    myListInstance = listExample()
    aSeq = ("abc",123,myArray,10.0005, 100.56,0.000000000034,b'a',u'a',"z",myListInstance)
    myListResult = myListInstance.createList(aSeq)
    for obj in myListResult:
        print(obj, type(obj))
    
    nextList= ['23','abc',12345,[1,2,3,4],('a','b')]    
    myListInstance.appendToList(myListResult,nextList)
    for obj in myListResult:
        print(obj, type(obj))
        
    forward=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print("forward",forward)
    print("reversed",myListInstance.reverseMylist(forward))
    
    print(myListInstance.removeItem(forward,9))
    try:
        myListInstance.removeItem(forward,9)
    except ValueError:
        print("Got Values Error")
        
    print(myListInstance.insertIntoList(forward,3,9))
    
    print(len(forward))
    
    myListInstance.extendList(forward,("aaaaaa"))
    print(forward)
    print(len(forward))
    myListInstance.extendList(forward,[("aaaaaa"),"b","b","b",("c","c","c")])
    print(forward)
    print(len(forward))