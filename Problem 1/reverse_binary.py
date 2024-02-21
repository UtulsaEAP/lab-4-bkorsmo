"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Brady Korsmo
Lab Time: Thursday @2

"""


def reverse_binary():
    user_num = int(input())
    output = ""
    # YOUR CODE HERE

    while user_num>0:
        new = user_num%2
        user_num = int(user_num/2)
        output += str(new)
    print(str(output))


if __name__ == "__main__":
    reverse_binary()