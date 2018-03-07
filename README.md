# IoT Project NTU
# Collaborator Alejandro Ly Liu, Wang, Kai-Sheng

This is an IoT project made for the class Introduction to Internet of Things at National Taiwan University.
We make use of Arduino, Bluetooth, Azure DB, Power BI and Azure ML.
Here you can find a PDF explaining the project and the code we use for making it.

Basically, What we did was:
1. Using an Arduino UNO and a few sensors to get temperature, humidity to try to know the Precipitacion Probability.
2. Send the information by Bluetooth to a Raspberry Pi 3
3. Send the data via Raspberri Pi 3 to Azure Machine Learning Studio Service (using Weather Prediction template)
4. Combined data transmission , prediction result storage( API ) and send all data to Azure DataBase.
5. Make a representation of our data by using PowerBI.

The equipment list:
1. Arduino UNO
2. Raspberry Pi 3
3. Bluetooth module HC05
4. DHT-22
5. Raining Sensor
