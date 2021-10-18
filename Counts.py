# Importing Libraries
import pandas as pd
import numpy as np

# Loading annotations file
annot = pd.read_csv('via_project_31Aug2021_13h49m_csv.csv')
# To print the annotations
print(annot)

# Reading class attributes column
clas = annot["region_attributes"]
#print(clas)

# Splitting the string and appending in a list
count = []
for i in range(0,5146):
    b = list(clas[i].split('"'))
    count.append(b)

# To check and verify the clas labels
# len(count)

# Making a counting function
def counting(strparam):
    p = []
    for i in count:
        for j in i:
            if j == strparam:
                p.append(j)
    return len(p)


# Loading the Original Class names
names = pd.read_csv('count_engro_sortcount_modified.csv')
names = names['Names']

