## DISCLAIMER ##
# This is not a clean code, its just for 3d visualization preview sake ty.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

PATH_DATA = 'dataset/'

df = pd.read_csv(r'Python\Hmm\dataset\food_delivery_datasets.csv')

a = df[['resto_id', 'status']]

df['date_time'] = pd.to_datetime(df['date_time']).dt.round('H')
b = df['date_time'].dt.strftime('%A')
c = df['date_time'].dt.strftime('%H:%M')

df = pd.concat([a['resto_id'], b, c, a['status']], axis=1)
df.columns = ['resto_id', 'days', 'time', 'status']

group_status = df.groupby('status')
group_status['status'].size()

df = df[df.status == 'Completed']
df.reset_index(drop=True)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']

fig = plt.figure('scatter dates')

ax = fig.add_subplot(111, projection='3d')

grp_days = df.groupby(['days', 'time'], as_index=False).size()
time = grp_days['time'].unique()
time.sort()

grp_days['time'] = grp_days['time'].replace(time, [i for i in range(len(time))])
grp_days['days'] = grp_days['days'].replace(days, [i for i in range(len(days))])

x = grp_days['days']
y = grp_days['time']
z = grp_days['size']

plot = ax.scatter(x, y, z, c=z)
fig.colorbar(plot)

ax.xaxis.set_ticklabels(days)
ax.set_yticks([i for i in range(0, len(time), 3)])
ax.yaxis.set_ticklabels([time[i] for i in range(0, len(time), 3)])
plt.show()
