import matplotlib.pyplot as plt
a=[1,2,3,4,5,6]
b=[5,4,2,5,7,4]
c=[4,2,6,3,6,8]

plt.subplot(2,2,1)
plt.plot(a,b,color='red')
plt.title('one')

plt.subplot(2,2,2)
plt.plot(a,c,color='blue')
plt.title('two')

plt.subplot(2,2,3)
plt.plot(a,c,color='blue')
plt.title('two')

plt.subplot(2,2,4)
plt.plot(a,c,color='blue')
plt.title('two')


plt.show()

