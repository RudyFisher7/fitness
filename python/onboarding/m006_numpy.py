import numpy as np

print(f"NumPy version: {np.__version__}")
# np.show_config()

array_1 = np.array([(3, 5, 6, 7), (4, 0, 0, 0), (3, 4, 5, 6)])
print(array_1)
print(array_1.dtype)

vector_1 = np.zeros(10)
print(vector_1)
print(f"bytes: {vector_1.nbytes}")

# Get documentation/info about the NumPy add function.
# help(np.add)
# np.info(np.add)