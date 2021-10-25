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
for i in range(0,len(annot)):
    b = list(clas[i].split('"'))
    count.append(b)

# To check and verify the clas labels
# len(count)

# Making a counting function to count from count []
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

# Rearranging the Original class labels file
pro = pd.concat([pd.DataFrame([i], columns = ['Names']) for i in names], ignore_index = True)
#print(pro)

# Counting the labels of class in a new file
con = pd.concat([pd.DataFrame([counting(i)], columns = ['Counts']) for i in names], ignore_index = True)
#print(con)

# Combining the two files for the final results
df = pd.concat([pro,con], axis = 1 )
#print(df)

# Before running this command kindly download tabulate library
#conda install tabulate (As I was using Anaconda for testing purposes)
# To see the output
# print(df.to_markdown())

# Create a new csv file as it is. You can also change the of the file.
df.to_csv('counts(default).csv',index = False)

# Below are the optional commands if you wanna save the file sorted by Alphabets (Remove the comments to use it)
# df = df.sort_values(by = ['Names'])
# df = df.reset_index().drop(columns='index')
# df.to_csv('counts(sorted_by_Name).csv',index = False)

# Below are the optional commands if you wanna save the file sorted by Counts (Remove the comments to use it)
# df = df.sort_values(by = ['Counts'])
# df = df.reset_index().drop(columns='index')
# df.to_csv('counts(sorted_by_Counts).csv',index = False)
