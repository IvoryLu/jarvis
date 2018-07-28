le = dataset.iloc[:,4].values
Coxib = dataset.iloc[:,5].values
#n_male = collections.Counter(Male)
n_male = (Male == 1).sum()
n_female = (Male == 0).sum()

n_rofecoxib = (Coxib == 1).sum()
n_celecoxib = (Coxib == 0).sum()

ones = (n_male,n_rofecoxib)
zeros = (n_female,n_celecoxib)

N = 2
ind = np.arange(2)
width = 0.35
print(n_male)

p1 = plt.bar(ind, ones, width)
p2 = plt.bar(ind, zeros, width, bottom = ones)
plt.ylabel('Numbers')
plt.title('Proportion of Male and Coxib')
plt.xticks(ind,('Male', 'Rofecoxib'))
plt.yticks(np.arange(0,45000,9000))
plt.legend((p1[0],p2[0]), ('1','0'))

plt.show()
