import numpy as np

def reshape_array(rows=3, cols=3):
    try:
        # Taking input and ensuring proper formatting
        arr = np.array(list(map(int, input("Enter space-separated integers: ").split())))

        # Checking if the input contains the correct number of elements
        if arr.size != rows * cols:
            raise ValueError(f"Expected {rows * cols} elements, but got {arr.size}.")

        # Reshaping the array
        reshaped_arr = arr.reshape(rows, cols)
        
        print("\nReshaped NumPy Array:")
        print(reshaped_arr)

    except ValueError as e:
        print(f"Error: {e}")

# Calling the function with a default shape of (3,3)
reshape_array()
