# Series
import pandas as pd
'''

a=pd.Series()
print(a)
'''

x = [3,4,5,6,7]
var = pd.Series(x)
print(var)


print(type(var))

print(var[2])
y = [3,4,5,6]
var1 = pd.Series(y,index=['a','b','c','d'], dtype="float", name = "python")

print(var1)
print(type(var1))


# passing dictionary
dic = {"name": ['python','c','c++','java'], "por": [1,2,3,4], "rank":[1,4,3,2]}
var3 = pd.Series(dic)
print(var3)

s=pd.Series(12,index=[1,2,3,4,5,6,7])
print(s)


s1=pd.Series(12,index=[1,2,3,4,5,6,7])
s2=pd.Series(12,index=[1,2,3,4])

print(s1+s2)