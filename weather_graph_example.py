import requests
import json
import matplotlib.pyplot as plt

headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
}

response = requests.get("https://api.weather.gov/gridpoints/BMX/110,46/forecast/hourly", headers=headers)

data_json = response.json()

weather = str(data_json['properties']['periods'][0]['temperature'])

weatherForecastInformation = data_json['properties']['periods']

temperatureList = []
for information in weatherForecastInformation:
    temperatureList.append(information['temperature'])

print(temperatureList)

xValues = []
for i in range(1, 157):
    xValues.append(i)

print(xValues)

plt.plot(xValues, temperatureList)
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.show()