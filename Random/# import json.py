# import json
# a=['veer','nayan']
# file=open('bbb.ts',"w")
# json.dump(a,file)

# ****************************************
import json
file=open('bbb.ts',"r")
a=json.load(file)
print(a)