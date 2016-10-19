'''
Created on Oct 15, 2016

@author: rduvalwa2
class EvalArrayOfIntegers:
    def __init__(self, integers):
        self.integers = integers

    def find_all_eval_strings(self, operators, desired_result):
        """
        Return a list of all strings that meet these criteria:

          - contains each member of `self.integers` exactly once
          - the order of the integers in the string is the same as in `self.integers`
          - any `operators` may be inserted, any number of times,
            before or between any of the integers
          - when evaluated, the string equals `desired_result`

        Args:
            desired_result: the number which each generated string should evaluate to
            operators: a list of strings representing mathematical operations, eg ['+', '-']
        Returns:
            A list of strings each of which evaluates to `desired_result`
        Raises
            TypeError: if `desired_result` is not a number
            TypeError: if `operators` is not a list
        """
        return []
'''

class EvalArrayOfIntegers:
    def __init__(self, integers):
        self.integers = integers
        self.goodIntArrays = []

    def find_all_eval_strings(self, operators, desired_result):
#        goodStrings = []
        print(self.integers)
        int_rawTotal = self.total_int(self.integers)
        
        if int_rawTotal == desired_result:
            self.goodIntArrays.append(self.integers)
        
#        if int_rawTotal < desired_result:
              
        return self.goodIntArrays

# *********************************************        
    def build_arrays(self):
        arrys = [
         [1,99],
        [12,34,56,78,9]
        ,[1,23,45,67,89]
        ,[12,3,4,5,6,7,8,9]
        ,[1,23,4,5,6,7,8,9]
        ,[1,2,34,5,6,7,8,9]
        ,[1,2,3,45,6,7,8,9]
        ,[1,2,3,4,5,67,8,9]
        ,[1,2,3,4,5,6,7,89]
        ,[12,34,5,6,7,8,9]        
        ,[1,2,34,56,7,8,9]
        ,[-1,2,34,56,-7,8,9]        
        ,[1,-2,-3,45,67,8,-9]
        ,[-1,-2,-34,56,-7,89]
        
        ,[123,456,789] 
        ,[-12,-345,67,89]
        ,[123,456,-789]
         
        ,[-123,45,6,7,8,9]
        
                 
        ,[123,45,-67,8,-9]      
        ,[123,-4,-5,-6,-7,8,-9]
        ,[1,23,-4,56,7,8,9]
        ,[1,23,-4,56,7,8,9]
        ,[12,3,-4,5,67,8,9]
        ,[1,2,3,-4,5,6,78,9]
        ,[12,3,4,5,-6,-7,89]
        ]

        return  arrys
        
    def get_possible_combination(self):      
        result_tuple = []
        goodArrays = []
        
        possible = self.build_arrays()
        for arry in possible:
            total = 0
            for i in arry:
                total = total + i
            result_tuple.append((total,arry))

#        for item in result_tuple:
#            print(item)
            
#        '''       
        for item in result_tuple:
            good = True                      
            if item[0] == 100:  
                for i in self.integers:
                    if str(i) not in str(item):
                        good = False
                if good:
                    goodArrays.append(item[1])
            good = True
        return goodArrays
#      '''
        
    def create_array_of_combined_numbers(self):
        comb_array = []
        for i in range(len(self.integers)):
            try:
                com = str(self.integers[i]) + str(self.integers[i+1])
                #print(com)
                comb_array.append(int(com))
            except IndexError as e:
#                print('Index error here', e)
                continue
#get negative numbers                    
        for i in range(len(self.integers)):
            try:
                com = str(self.integers[i]) + str(self.integers[i+1])
                #print(com)
                comb_array.append(int(com) * -1)
            except IndexError as e:
#                print('Index error here', e)
                continue
            
        for i in range(len(self.integers)):
            try:
                com = str(self.integers[i]) + str(self.integers[i+1]) +  str(self.integers[i+2])
                #print(com)
                comb_array.append(int(com))
            except IndexError as e:
#                print('Index error here', e)
                continue
        return comb_array



        
            
if __name__ == '__main__':
    expected = 100
    myeval = EvalArrayOfIntegers(range(1, 10))
#    result = myeval.find_all_eval_strings(['+', '-'], expected)
    '''   
    for ar in result:
        print(ar)
    myeval.create_arrays()   
    print(myeval.create_array_of_combined_numbers())
  '''  
    print(myeval.create_array_of_combined_numbers())
  
    goodA = myeval.get_possible_combination()
    print('array length ',len(goodA) )
    for item in goodA:
        print(item)
