#Python program to show how to use assert keyword  
# defining a function  

def square_root( Number ): 
        try: 
            assert ( Number > 0), "Give a positive integer" 
            return Number**Number

           
        except AssertionError:
           print("Asseriton Error Occured")  
           return "Number is Negative"
        
#Calling function and passing the values  
print( square_root( -3) )  
# print( square_root( 12) ) 