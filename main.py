
import pandas as pd
import glob
import os

os.chdir("/Users/patri/Desktop/New folder (2)")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


new_list = []
new_list2 = []
new_list3 = []
#loop through all the csv files in the folder, from each file extract take the first value in the 'participant' column and append it to a list
#then create a new dataframe with the list as the 'participant' column
for i in all_filenames:
    df = pd.read_csv(i)
    participant = df['participant'][0]
    ee = df['Explore_Count.routineStartVal'].sum()/600
    optimal = df['Optimal_EE'][3]
    new_list.append(participant)
    new_list2.append(ee)
    new_list3.append(optimal)
    df = pd.DataFrame({'participant': [participant]})
print(new_list)
print(new_list2)
print(new_list3)

group_avg = sum(new_list2)/len(new_list2)
print(group_avg)


