import time
import requests
import json

import serial

firebase_url = 'https://hearthealthypi.firebaseio.com'
# Connect to Serial Port for communication
ser = serial.Serial('COM1', 115200, timeout=0)
# Setup a loop to send Temperature values at fixed intervals
# in seconds
fixed_interval = 1
while 1:
    try:
        # temperature value obtained from Arduino + LM35 Temp Sensor
        heartRate = ser.readline().decode('utf-8').strip('\r\n')

        # current time and date
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%d/%m/%Y')

        # current location name
        db_location = 'BPM';
        print(heartRate + ',' + time_hhmmss + ',' + date_mmddyyyy + ',' +db_location)

        # insert record
        data = {'date': date_mmddyyyy, 'time': time_hhmmss, 'value': heartRate}
        result = requests.post(firebase_url + '/' + db_location + '/BPM.json', data=json.dumps(data))

        print('Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text)
        time.sleep(fixed_interval)
    except IOError:
        print('Error! Something went wrong.')
    time.sleep(fixed_interval)


