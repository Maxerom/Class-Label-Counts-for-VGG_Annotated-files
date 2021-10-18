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

