test_dict={'Codingal':2, 'is':2, 'the':2, 'best':1 }
print("The original dictionary is- ",test_dict)
K=2
res=0
for key in test_dict:
    if test_dict[key]==K:
        res+=1
print("Frequency of K is: ",res)