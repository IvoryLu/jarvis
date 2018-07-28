import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('C:\\Users\\Lu\\Documents\\study\\Research\\coxib_drop.csv')
X = dataset.iloc[:,2:28].values
y = dataset.iloc[:,28].values

age = dataset['Age']
# change outlier point symbols
plt.figure()
plt.boxplot(age,0,'gD')

# don't show outlier points
plt.figure()
plt.boxplot(age,0,'')

# horizontal boxes
plt.figure()
plt.boxplot(age,0,'rs',0)

# change whisker length
plt.figure()
plt.boxplot(age, 0, 'rs', 0, 0.75)

'''
# fake up some more data
spread = np.random.rand(50) * 100
center = np.ones(25) * 40
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
d2 = np.concatenate((spread, center, flier_high, flier_low), 0)
age.shape = (-1, 1)
d2.shape = (-1, 1)
# data = concatenate( (data, d2), 1 )
# Making a 2-D array only works if all the columns are the
# same length.  If they are not, then use a list instead.
# This is actually more efficient because boxplot converts
# a 2-D array into a list of vectors internally anyway.
data = [data, d2, d2[::2, 0]]
# multiple box plots on one figure
plt.figure()
plt.boxplot(data)

plt.show()





