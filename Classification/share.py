from sklearn import tree
import matplotlib.pyplot as plt

def share(n):
    if n==2:
        return 'Do Not Buy..'
    return 'Buy'
def classification(n):
    if n<51:
        return 2
    return 1

inputshare=[65,54,40,74,50,88,49,52,39] # [39, 40, 49, 50, 52, 54, 65, 74, 88] 
inputshare.sort()
shares=[[x] for x in inputshare]
print(shares)
result=[2,2,2,1,1,1,1,1,1]
textresult=[share(x) for x in result]

print('textresult',textresult)

classifier=tree.DecisionTreeClassifier()
model=classifier.fit(shares,result)

plt.plot(shares,result,color='red')
plt.scatter(shares,result,color='blue',marker='o')
plt.xlabel('Shares')
plt.ylabel('Result')
plt.legend(['shares','result'])
plt.show()