"""
Complete the following python code to reverse the string entered by the user.

Name: Brady Korsmo
Lab Time: Thursday @2
"""

def reverse_string():
    # YOUR CODE HERE
    

    yourstring = str(input())
    finished= ['done', 'd', 'Done']
    while yourstring not in finished:
        print(yourstring[::-1])
        yourstring = str(input())



    





if __name__ == "__main__":
    reverse_string()