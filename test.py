
# Python program to demonstrate
# main() function
  
  
print("Hello")
  
# Defining main function
def main():
    print("hey there")
    with open('auto.txt', 'w') as f:
    f.write('Create a new text file!')
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
    exit("hey kunal this is data231")
