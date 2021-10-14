

def my_function(first_argument,
                second_argument,
                third_argument):
    """One line summary of what the function does.

    Short explanation of how the algorithm works. This part corresponds
    to your answer to the third question.

    Args:
        first_argument: A description of first_argument. 
        second_argument: A description of your second argument.
        third_argument: A description of your third argument.

    Returns:
        An explanation of the output. 
    """
    result = True
    #insert code here
    return result



# For example

def add_vectors(vector_01,vector_02):
    """Adds the input vectors.

    Creates a zero vector the same size as the input, then overwrites each
    element with the corresponding sum from the input vectors. 

    Args:
        vector_01: A vector stored as a list.
        vector_02: A vector stored as a list. The same size as vector_01.

    Returns:
        The vector sum of the inputs stored as a list.
    """
    result = [0 for element in vector_01]
    for index in range(len(result)):
        result[index] = vector_01[index] + vector_02[index]
    return result

def scalar_vector_multi(vector_01):
    return vector_01*scalar
# Initializing result as an empty list
vector = []
#instructions for use to put how many elements are in the vector,
elem = int(input("Insert how many elements you want:"))
#for an element i in range from 0 to the given number of elements append an integer to vector from [0,1,2.,n]
#aka telleing the user to put their elements in
    for i in range(0, elem):
        vector.append(int(input("Enter number:")))
#defining scalar for the above function
        scalar = int(input('enter scalar multiplier: '))
#maping the made list "vector" back into our function to get the scalar * the elements in the made list
#then having it listed and put into a new element 'ans'
    ans = list(map(scalar_vector_multi, vector))
#print the answer
print(ans)