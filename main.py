#for working with dabase
import psycopg2
#environment variables
import os
from dotenv import load_dotenv
load_dotenv('/home/anon_2034/PythonGraph/.env')
#for working with json files
import json
#for working with graph
import matplotlib.pyplot as plt
#for using numbers
import numpy as np

con = psycopg2.connect(
    database = os.getenv('database'),
    user= os.getenv('user'),
    password = os.getenv('password'),
    host=os.getenv('host'),
    port = os.getenv('port')
)
cursor_obj = con.cursor()
cursor_obj.execute("SELECT * FROM weather")
result = cursor_obj.fetchall()


highTemp = []
lowTemp = []

for i in range(len(result)):
    highTemp.append(result[i][2])
    lowTemp.append(result[i][1])

x = np.array(["Germantown", "New York", "Dhaka", "London", "Adelaide"])
y=np.array([lowTemp[0],lowTemp[1],lowTemp[2],lowTemp[3],lowTemp[4]])

plt.bar(x,y)
plt.title("Low Temperatures in Diff Cities Around the world in 31st March 2023")
plt.xlabel("Cities")
plt.ylabel("Temperature")
plt.show()

a = np.array(["Germantown", "New York", "Dhaka", "London", "Adelaide"])
b = np.array([highTemp[0],highTemp[1],highTemp[2],highTemp[3],highTemp[4]])

plt.bar(a,b, color = "orange")
plt.title("High Temperatures in Diff Cities Around the world in 31st March 2023")
plt.xlabel("Cities")
plt.ylabel("Temperature")
plt.show()