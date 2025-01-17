# -*- coding: utf-8 -*-
"""LVADSUSR121-SNEHA-IA2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19zHtblgo2bygOLEVSMDTSISFifBFXIi8
"""

#1
import numpy as np
rgd_image = np.array([[[255,0,0],[0,255,0],[0,0,255]],
 [[255,255,0],[255,0,255],[0,255,255]],
  [[127,127,127],[200,200,200],[50,50,50]]])
arr = np.array(rgd_image)
arr1 = []
for i in arr :
  for j in i :
    a1 = 0.2989*j
    for k in j :
      a2 = 0.5870*k
      for l in k :
        a3 = 0.1140*l
  arr1[9] = a1+a2+a3

print(arr1)

#2
import numpy as np
arr = np.arange(12).reshape((3,4,1))
print(arr)
print(np.mean(arr))
print(np.std(arr))

#3
import numpy as np
arr = np.arange(12).reshape((2,6))
arr2 = arr.reshape(2,3,2)
print(arr)
print(arr2)
for i in arr2 :
  print(arr2.flatten())

#4
import numpy as np
arr = [[2,4,5,6,8],[6,8,9,4,5]]
arr1 = np.array(arr)

#5
import numpy as np
arr = [89,78,54,67,90]
arr1 = np.array(arr)
arr_avg = np.mean(arr1)
print(arr_avg)

#6
import numpy as np
arr = [23,5,6,7,8,89]

#7
import pandas as pd
emp_data = {
    'Name' : ['Alice','Bob','Charlie','David','Eve','Frank','Grace'],
     'Age' : [25,30,35,40,45,50,55],
    'City' : ['New York','Los Angeles','Chicago','Houston','Phoenix','Miami','Boston'],
    'Department': ['HR','IT','Finance','Marketing','Sales','IT','HR']
}
df = pd.DataFrame(emp_data)
df1 = df[(df['Age']<45) & (df['Department'] != 'HR')]
df2 = df1[['Name','City']]
print(df2)

#8
import pandas as pd
sup_data = {
    'product' : ['Apples','Bananas','Cherries','Dates','Elderberries','Flour','Grapes'],
    'Category' : ['Fruit','Fruit','Fruit','Fruit','Fruit','Bakery','Fruit'],
    'Price' : [1.20,0.50,3.00,2.50,4.00,1.50,2.00],
    'Promotion' : [True, False, True, True, False, True, False]
}
df = pd.DataFrame(sup_data)
df1 = df[df['Category'] == 'Fruit']
AVGPRICE = df1['Price'].mean()

df2 = df1[(df1['Price'] > AVGPRICE) & (df1['Promotion']==False)]
print(df2)

#9
import pandas as pd
data = {

    'Employee' : ['Alice','Bob','Charlie','David'],
    'Department' : ['HR','IT','Finance','IT'],
    'Manager' : ['John','Rachel','Emily','Rachel']
}

data1 = {
    'Employee' : ['Alice','Charlie','Eve'],
    'Project' : ['P1','P2','P3']

}
mer = pd.merge(data,data1, on=data['Manager']==data1['Employee'])
df = pd.DataFrame(mer)
print(df)

#10
import pandas as pd
data = {
    'Department' :['Electronics','Electronics','Clothing','Clothing','Home Goods'],
    'Salesperson' : ['Alice','Bob','Charlie','David','Eve'],
    'Sales' : [70000,50000,30000,40000,60000]
}
df = pd.DataFrame(data)
df1 = df.groupby(['Salesperson','Department']).agg({'Sales' : 'mean'})
print(df1)