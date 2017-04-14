import pandas as pd
import numpy as np

col1 = [i for i in range(4)]
col2 = [float(i**2) for i in range(4) ]
col3 = ['cat1', 'cat2', 'cat3', 'cat1']

MyDataframe = pd.DataFrame({'INDEX':col1,
                  'DATE':pd.Timestamp('20130102'),
                  'SQUARED':col2,
                  'THREE':np.array([3]*4, dtype='int32'),
                  'SET':pd.Categorical(["test", "train",
                                        "test", "train"]),
                  'CAT':col3})
# print entire data frame
print(MyDataframe)
# print only first 2 rows
print(MyDataframe.head(2))
# print last 3 rows
print(MyDataframe.tail(3))
# print the datatypes of the columns
print(MyDataframe.dtypes)
# print columnames
print(MyDataframe.columns)
# print the index
print(MyDataframe.index)
# give a summary of the dataframe
print(MyDataframe.describe)

print(MyDataframe[(MyDataframe['SET'] == 'test') &
                  (MyDataframe['SQUARED'] != 0.0)])

MyTestSet = MyDataframe[(MyDataframe['SET'] == 'test') &
                  (MyDataframe['SQUARED'] != 0.0)]
MyTestSet['NEW'] = [i+2 for i in range(2)]
MyTestSet['NEW2'] = MyTestSet['THREE'] + MyTestSet['NEW']
print(MyTestSet)
