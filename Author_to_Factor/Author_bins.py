import pandas as pd
from collections import Counter
#add sub files together, count user appearance totally. 
#And seperate it into 10 bins based on the count. 
#save counts of authors for checkout transaction Archive in past three years. From 2015.7-2018.6.30
def count(name,total):
    df = pd.read_csv('top_author_'+str(name)+'.csv')
    df = df.set_index('Unnamed: 0')
    dic2  = df.to_dict()['0']
    print(dic2)
    total = dict(Counter(total)+Counter(dic2))
    print('csv len:',len(dic2),'Total len:',len(total))
    return total

total = {}
for name in range(0,236):
    total = count(name,total)
print(total)
totaldf = pd.DataFrame.from_dict(total, orient='index')
print(totaldf.head(20))
totaldf = totaldf.sort_values(0,ascending=False)
print(totaldf.head(20))
totaldf.to_csv('author_order.csv')

