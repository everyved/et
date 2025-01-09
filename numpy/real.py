import numpy as np
a=np.array([1,4,6,4,9,3+5j])
# print(np.isreal(a))
# b=np.iscomplex(a)
b=np.isreal(a)
c=a[b]
print(c)
