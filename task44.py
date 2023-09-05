import random
import pandas as pd
lst= ['robot']*10
lst+=['human']*10
random.shuffle(lst)
data=pd.DataFrame({'whoAmI':lst})
data.head()
robot=list()
human=list()
for i in range(len(lst)):
    if(lst[i]=='robot'):
        robot.append(1)
        human.append(0)
    else:
        robot.append(0)
        human.append(1)
data['robot']=robot
data['human']=human
print (data)