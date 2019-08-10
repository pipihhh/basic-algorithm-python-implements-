import numpy as np


ret = (10000000000 * np.log(0.0001)) / (np.log(2) ** 2)
m = np.log(2) * (-ret) / 10000000000
print(m)
