"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Brady Korsmo
Lab Time: Thursday @2
"""

def inc_5():
    # Write your code here

    numbone = int(input())
    numbtwo = int(input())

    if (numbtwo < numbone):
        print("Second integer can't be less than the first.")
    else:
        for x in range(numbone, numbtwo +1, 5):
            print(x, end=" ")
    
        
if __name__ == '__main__':
    inc_5()