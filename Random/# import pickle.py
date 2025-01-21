# import pickle 
# a = [ 10,20,30]
# file=open('aaa.ts','wb')
# pickle.dump(a,file)
#  *********************************************
import pickle
file=open('aaa.ts','rb')
a=pickle.load(file)
print(a)
          