import numpy as np
import pandas as pd
​
# load a data file
data_file = pd.read_csv('data_with_headers.csv')

print(data_file[0:3])

time = data_file['time']
print(time[0:3])

sensors = data_file.loc[:,'s1':'s4']
print(sensors[0:6])


time = time - time[0]
print(time[0:3])

avg_row = np.mean(sensors,1)
avg_col = np.mean(sensors,0)
print(avg_col)

my_data = [time, sensors, avg_row]
result = pd.concat(my_data,axis=1)
print(result[0:3])

result.to_csv('result.csv')
result.to_excel('result.xlsx')
result.to_html('result.htm')
result.to_clipboard('')

%matplotlib inline
import matplotlib.pyplot as plt

plt.figure(1)
plt.plot(time,sensors['s1'],'r-')
plt.plot(time,avg_row,'b.')
plt.legend(['Sensor 1','Average'])
plt.xlabel('Time (sec)')
plt.ylabel('Sensor Values')
plt.savefig('myPlot.png')