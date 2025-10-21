---
layout: exercise
topic: Loops
title: Temperature Sensors
language: R
---

You have deployed multiple temperature sensors at different locations to monitor daily temperature patterns. Each sensor records temperature readings every hour for a 24-hour period. The data from each sensor is stored in a separate CSV file with the naming pattern `sensor-X-temp.csv` where X is the sensor number.

- If `temperature_sensor_data.zip` is not already in your working directory download [the zip file]({{ site.baseurl }}/data/temperature_sensor_data.zip) using `download.file()`
- Unzip it using `unzip()`
- Obtain a list of all of the files with file names matching the pattern `"sensor-"` (using `list.files()`)

Each file contains two columns:

- `hour`: Hour of the day (0-23)
- `temperature`: Temperature reading in Celsius

1\. Use a loop to load each sensor data file and calculate the mean temperature for the sensor. Store the results in a vector called `mean_temps`. After the loop display the completed vector.

2\. Create a copy of your code from (1) and modify it to also find the maximum temperature recorded by each sensor and the temperature range (difference between maximum and minimum temperature) for each sensor. Store these values in vectors called `max_temps`, and `temp_ranges`. After the loop display the completed vectors.

3\. Create an empty data frame to store all your results and then write a loop to determine the following values for each file and store them in the data frame:

- `sensor_file`: The filename of the sensor data
- `mean_temp`: Mean temperature for that sensor
- `max_temp`: Maximum temperature recorded
- `min_temp`: Minimum temperature recorded
- `temp_range`: Temperature range (max - min)

4\. **Challenge (optional)** Extend your analysis to find the hour when each sensor recorded its highest temperature. Add a column called `peak_hour` to your results data frame and display the data frame.
