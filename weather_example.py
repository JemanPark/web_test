from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

# time, shortforecast, temperature, humidity, rain, windspeed
class weatherInformation:
    def __init__(self, time, shortForecast, temperature, humidity, chanceOfRain, windSpeed):
        self.time = time
        self.shortForecast = shortForecast
        self.temperature = temperature
        self.humidity = humidity
        self.chanceOfRain = chanceOfRain
        self.windSpeed = windSpeed

    def __str__(self) -> str:
        return str(self.time) + ", " + str(self.shortForecast) + ", " + str(self.temperature) + ", " + str(self.humidity) + ", " + str(self.chanceOfRain) + ", " + str(self.windSpeed)

@app.route('/<user>')
def hello(user):
    # name = "Dongmae"
    # return '<html><body><h1>Hello ' + user + '!</h1></body></html>'
    return render_template('hello_test_templates.html', name = user)


@app.route('/exam_score/<int:score>')
def exam_score(score):
    return render_template('int_test_templates.html', int_score = score)

@app.route('/list')
def list_example():
    nameList = ['Jay', 'Dongmae', 'Hansol']
    return render_template('list_templates.html', testList = nameList)

@app.route('/dict')
def dict_example():
    nameDict = {1:'Jay', 2:'Dongmae', 3:'Hansol'}
    return render_template('dict_templates.html', testDict = nameDict)

@app.route('/1')
def test1page():
    return "page 1 ok"

@app.route('/2')
def test2page():
    return "page 2 ok"

@app.route('/weather')
def weatherinformation():
    weather = ""

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://api.weather.gov/gridpoints/BMX/110,46/forecast/hourly", headers=headers)

    data_json = response.json()

    

    # print(data_json)
    # print(data_json['properties']['periods'][0]['temperature'])

    temperatureWeather = str(data_json['properties']['periods'][0]['temperature'])

    periods = data_json['properties']['periods']
    print(periods)

    temperatures = []

    for period in periods:
        temperatures.append(period['temperature'])
        print(period['temperature'])

    



    return str(temperatures)

# temperature, probabilityOfPrecipitation, relativeHumidity, windSpeed
@app.route('/shortweather')
def shortWeatherinformation():
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://api.weather.gov/gridpoints/BMX/110,46/forecast/hourly", headers=headers)

    data_json = response.json()

    periods = data_json['properties']['periods']

    shortForecasts = []
    startTimeList = []

    temperatureList = []
    probabilityOfPrecipitationList = []
    humidityList = []
    windSpeedList = []


    for period in periods:
        shortForecasts.append(period['shortForecast'])
        startTimeList.append(period['startTime'])
        temperatureList.append(period['temperature'])
        probabilityOfPrecipitationList.append(period['probabilityOfPrecipitation']['value'])
        humidityList.append(period['relativeHumidity']['value'])
        windSpeedList.append(period['windSpeed'])

    # print(temperatureList)
    # print(probabilityOfPrecipitationList)
    # print(humidityList)
    # print(windSpeedList)


    # shortForecastsThreeHours = []
    # startTimeListThreeHours = []

    # temperatureListThreeHours = []
    # probabilityOfPrecipitationListThreeHours = []
    # humidityListThreeHours = []
    # windSpeedListThreeHours = []

    # timeAndForecastList = []
    # timeAndForecastDict = {}

    weatherInformationList = []
    
    # 0, 3, 6, 9, 
    for i in range(len(shortForecasts)):
        if i % 3 == 0:
            # shortForecastsThreeHours.append(shortForecasts[i])
            
            tempStartTime = startTimeList[i]
            
            tempStartTime = tempStartTime[8:13]
            tempTemperature = temperatureList[i]
            tempWindSpeed = windSpeedList[i]
            tempPrecipitation = probabilityOfPrecipitationList[i]
            tempShortForecast = shortForecasts[i]
            tempHumidity = humidityList[i]



            tempWeatherInformationInstance = weatherInformation(tempStartTime, tempShortForecast, tempTemperature, tempHumidity, tempPrecipitation, tempWindSpeed)
            weatherInformationList.append(tempWeatherInformationInstance)

            # startTimeListThreeHours.append(tempStartTime)

            # timeAndForecastList.append(tempStartTime + ": " + shortForecasts[i])
            # timeAndForecastDict[tempStartTime] = shortForecasts[i]

        else:
            pass

    # return timeAndForecastList
    # print(weatherInformationList)
    for info in weatherInformationList:
        print(str(info))

    return render_template('classList_to_table_templates.html', htmlList = weatherInformationList)

    # 1. passing dictionary = {Time: shortForecast}
    # + humidity + windspeed + temperature 
    # temp_dict = {1: "Jay", 2: "Dongmae"}

    # 2. passing List = [ee, eq, qwe,r,qw ]
    # Make scheme / protocol
    # weatherInfoList = [02-19T09, "Partly ㄷSunny", 50, 66, "5 mph", "S", 02-19T12, "Sunny", 52, 43, "3 mph"]
    # List =

    # [weatherInformmationInstnace 1, weatherInformmationInstnace 2]


def main():
    app.run(debug=True, port=8080)
    # weatherinformation()

if __name__ == '__main__':
    main() 
 
