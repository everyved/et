import numpy as np
from scipy.stats import mode
a=np.array([4,5,7,3,6,3,66,34,2,6])

#mean median mode
print(np.mean(a))
print(np.median(a))
print(mode(a))

#standard deviation
print(np.std(a))

#quantile
print(np.quantile(a,.25)) #1st
print(np.quantile(a,.50)) #2nd
print(np.quantile(a,.75)) #3rd

#variance
print(np.var(a))
