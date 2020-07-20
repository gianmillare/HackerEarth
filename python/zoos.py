# Zoos
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def main(x):
    list_x = list(x)
    z_count = list_x.count('z' or 'Z')
    o_count = list_x.count('o' or 'O')
    
    if z_count * 2 == o_count:
        print("Yes")
    else:
        print("No")


stdin_str = input()
main(stdin_str)