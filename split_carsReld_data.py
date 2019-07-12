import numpy as np
import csv
import pandas as pd
import os

csv_file_path = "./data_new/2017-IWT4S-CarsReId_LP-dataset/trainVal.csv"

all_path = pd.read_csv(csv_file_path)

all_data_len = len(all_path)
print(all_path.iloc[1,1])

with open('train_data.csv', 'w') as csvfile:

  writer = csv.writer(csvfile)
  writer.writerow(['License_Plate_image', 'lable'])
  for i in range(all_data_len):
      if all_path.iloc[i,3]==1:
          writer.writerow([os.path.join("./data_new/2017-IWT4S-CarsReId_LP-dataset", all_path.iloc[i,1]), all_path.iloc[i,2]])

first = True
with open('test_data.csv', 'w') as csvfile:

  writer = csv.writer(csvfile)
  writer.writerow(['License_Plate_image', 'lable'])
  for i in range(all_data_len):

      if all_path.iloc[i,3]==0:

          if(first):
              tem = all_path.iloc[i, 2]
              writer.writerow([os.path.join("./data_new/2017-IWT4S-CarsReId_LP-dataset", all_path.iloc[i, 1]), all_path.iloc[i, 2]])
              first = False
          else:
              if(all_path.iloc[i, 2]!=tem):
                  writer.writerow([os.path.join("./data_new/2017-IWT4S-CarsReId_LP-dataset", all_path.iloc[i, 1]), all_path.iloc[i, 2]])
                  tem = all_path.iloc[i, 2]

          






