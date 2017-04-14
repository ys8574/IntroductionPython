# from MyModule import animal
# zebra = animal("Samba", 4)
# elephant = animal("Dumbo", 2)
# zebra.description()
# elephant.description()
# import math
# print (math.sqrt(36))
# #same way:
# from math import sqrt
# print(sqrt(36))
# #import all functions from math
# from math import *
# print(acos(1))
# #can be dangerous to call all functions by using "*", you can have defined the same name for something else (as shown below)
# def sqrt (number):
#     print("bla")
# sqrt(36)
from joblib import parallel, delayed
import multiprocessing
import time


# def myfunction(i):
#     print (i)
#     time.sleep(2)
#     return (i)
# if __name__=='__main__':
#     start=time.time()
#     for i in range(10):
#         myfunction(i)
#     print("Serial",time.time()-start)

def myfunction(i):
    print (i)
    time.sleep(2)
    return (i)
if __name__=='__main__':
    start=time.time()
    for i in range(10):
        myresults = myfunction(i)
    print("Serial",time.time()-start)
    num_cores = multiprocessing.cpu_count()
    print("Number of cores used." + str(num_cores))
    results=parallel(n_jobs=num_cores)(delayed(myfunction)(i) for i in range(10))
    print("Parallel",time.time() -start)
    print(results)