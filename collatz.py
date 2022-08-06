# A program to print Collatz Sequence using an integer input.
# Makes use of functions, list and conditional statements.

def collatz(num):  # Function defined for collatz sequence.
    collatz_list=[] # A list to store all the values in the sequence.
    
    while (num != 1) :
        collatz_list.append(num) 
        # Whennumber is Even
        if (num % 2 == 0) :
            num =num // 2
        else:
          # When  number  is Odd
            num = (3 * num)+1
    collatz_list.append(1)  #print 1 in the end   

    print("Length of collatz sequence is",  len(collatz_list))
    print("The sequence is :",end = " ")
    for i in range( len(collatz_list)):
      print(collatz_list[i], end = " ")

num = int(input("Enter the number : "))

collatz(num)
