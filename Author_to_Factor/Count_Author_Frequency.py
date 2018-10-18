import pandas as pd
from pandas import DataFrame
# count the time that the author appears in past three years in this file. 
# each file is small part of total 3 year checkout data, all data is too large, so I seperate 
#into small ones and them combine it. 
def countauthor(name,file):
    n = 0
    totalauthor = []
    for line in file.readlines():
        line = line.strip('\n')
        line = line.split('|')
        author = line[1].split(';')
        totalauthor = totalauthor + author
        n = n + 1
        if n % 1000 == 0:
            print(n,'is finished')
    result = DataFrame(pd.value_counts(totalauthor))
    result.to_csv('top_author_'+str(name)+'.csv')
    print('authorid',name, 'is finished=========')

for name in range(0,236):
    file = open('/Users/mia/Desktop/RAAsxi360/authorid/authorid_'+str(name)+'.txt')
    countauthor(name,file)

