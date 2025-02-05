import numpy as np
from my_matrice import matrix

#(matrix)

def initial_solution(length):
    """
    Creation of a list that contains all the (length) variables (ex: length=10 : 1,2,3,4,5,6,7,8,9,10)
    and it is (lenght) long and there is no repetition (no double 4 or double 7)
    """
    s = np.random.choice(range(length), length, replace = False)
    return s

a = initial_solution(17)
print(a)


# mesasure the quality of the solution s
def objectivefunction(s):
    print(s)
    cost=0
    for i in range(0,len(s)-1):
        start_row = s[i] # we pick the row in the matrix that represents the city were we are coming from
        destination_row = s[i+1] # this is the index of the city that we are going to
        distance = matrix[start_row][destination_row] # in the row of all the distance from our town A we pick a town B that coresponds to the index of second town
        cost += distance
    return cost


b = objectivefunction(a)
print(b)