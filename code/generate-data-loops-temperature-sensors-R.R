# Script to generate temperature sensor data files for looping exercise
set.seed(42)

n_sensors <- 5
n_hours <- 24

sensor_info <- data.frame(
  sensor_id = paste0("sensor_", 1:n_sensors),
  base_temp = c(20, 22, 18, 21, 19),
  amplitude = c(8, 10, 7, 9, 6)
)

for (i in 1:n_sensors) {
  hours <- 0:23
  base_temp <- sensor_info$base_temp[i]
  amplitude <- sensor_info$amplitude[i]
  temperatures <- base_temp + amplitude * sin((hours - 8) * pi / 12)
  temperatures <- temperatures + rnorm(n_hours, mean = 0, sd = 0.5)
  temperatures <- round(temperatures, 1)

  sensor_data <- data.frame(
    hour = hours,
    temperature = temperatures
  )

  filename <- paste0("sensor-", i, "-temp.csv")
  write.csv(sensor_data, filename, row.names = FALSE)
}
