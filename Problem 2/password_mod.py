"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Brady Korsmo
Lab Time: Thrusday @2
"""

def password_mod():
    word = (input())
    password = ''
    # Type your code here.

    for char in word:
        if char == "i":
            password += "1"
        elif char== "a":
            password +="@"
        elif char == "m":
            password +="M"
        elif char == "B":
            password += "8"
        elif char == "s":
            password += "$"
        else:
            password +=char
    password += "!"
    print(password)

if __name__ == "__main__":
    password_mod()