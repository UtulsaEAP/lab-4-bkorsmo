"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Brady Korsmo
Lab Time: Thursday @2
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())
    first = [a,b,c]

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())
    second = [d,e,f]

    solution = find_integer_solution(first,second)
    if solution:
        print("x =", solution[0], ", y =", solution[1])
    else:
        print("There is no solution")
    

    # YOUR CODE HERE
def find_integer_solution(first, second):
        for x in range(-10, 11):
            for y in range(-10, 11):
                if first[0]*x + first[1]*y == first[2] and second[0]*x + second[1]*y == second[2]:
                    return x, y
        return None






    
    
if __name__ == "__main__":
    brute_eq()