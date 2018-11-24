#Plot matrix fill of Random numbers

import numpy as np
import matplotlib as plt

width = int(input())
height = int(input())
matrix = np.random.randn(width*height).reshape(width,height)
plt.imshow(matrix,'gray')
plt.show()
