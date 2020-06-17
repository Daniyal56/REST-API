# import dependencies of packages
import os
import pyodbc
from meza import io
import pandas as pd
import csv
import requests

# Joining the path of the directory
fileName = 'HanvonFaceIDManager.mdb'
# os.path.join(path=r'C:\\Users\\Danyal\\Desktop\\KPS\\fileName')
file = r'C:\\Users\\Danyal\\Desktop\\KPS\\' + fileName

# # print(next(file))
# # print(file)

DRV = '{Microsoft Access Driver (*.mdb)}'

connection = pyodbc.connect(f'DRIVER={DRV};DBQ={file}')
cursor = connection.cursor()


SQL = 'SELECT * FROM Attendance;'
rows = cursor.execute(SQL).fetchall()

cursor.close()
# print(cursor.getTypeInfo())
connection.close()

# Converting data into CSV
with open('attendance.csv', 'w') as f:
    csv_writer = csv.writer(f)  # default field-delimiter is ","
    csv_writer.writerow(['AttendanceID', 'MachineID', 'PinNumber', 'AttendanceDateTime', 'Status',
                         'MachineName', 'AttendanceDate', 'AttendanceTime', 'AttendancePhoto', 'PollingDateTime'])
    csv_writer.writerows(rows)


# df = pd.read_csv('attendance.csv')
# print(df.head(5))

# for row in rows:
#     data = dict(row)
#     print(data)
#     break
