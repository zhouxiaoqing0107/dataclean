import pandas as pd
from sklearn import datasets
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

x,y=datasets.load_iris(return_X_y=True, as_frame=True)
df=x
df['target']=y
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
clf=DecisionTreeClassifier(max_depth=1)
clf.fit(x_train,y_train)
clf.score(x_test,y_test)
predicted=clf.predict(x_test)

import matplotlib.pyplot as plt

plt.scatter(x_test.index,y_test)
plt.scatter(x_test.index,predicted)
plt.show()

print(1)
print(2)