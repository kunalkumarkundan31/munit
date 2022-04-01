
# Python program to demonstrate
# main() function
  
  
print("Hello")
  
# Defining main function
def main():
    print("hey there")
    with open('auto.txt', 'w') as f:
      f.write('Auto discovery id is 123')
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
    
