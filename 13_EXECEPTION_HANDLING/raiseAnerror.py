# string = "hello"

# if not type(string) is int:
#     raise TypeError("type error")
# else:
#     print(string)

# try:
#     obj = None
#     obj.some_method()
# except AttributeError as e:
#     print(f"AttributeError: {e}")


# try:
#     data = input("Enter something: ")
# except EOFError as e:
#     print(f"EOFError: {e}")

# try:
#     import Onfil
# except ImportError as e:
#     print(f"ImportError: {e}")

# try:
#     # Arithmetic operation
#     result = 10 / 0
    
#     # File operation
#     with open('nonexistent_file.txt', 'r') as file:
#         data = file.read()
    
#     # List operation
#     my_list = [1, 2, 3]
#     item = my_list[5]
    
#     # Dictionary operation
#     my_dict = {'a': 1, 'b': 2}
#     value = my_dict['c']
    
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except FileNotFoundError:
#     print("The file does not exist.")
# except IndexError:
#     print("List index out of range.")
# except KeyError:
#     print("Key not found in dictionary.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("Execution completed.")

# x = 10
# y = 0

# # Assert that y is not zero before dividing
# assert y != 0, "y should not be zero to avoid division by zero"
# result = x / y  # This will raise an AssertionError
# print(result)

# try: 
# 	raise NameError("Hi there")
# except NameError:
# 	print ("An exception")
# 	raise

marks = 10000
a = marks / 0
print(a)

