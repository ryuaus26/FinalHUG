import pandas as pd
from darts import TimeSeries
from darts.models import ExponentialSmoothing

# Read a pandas DataFrame
df = pd.read_csv("world_population.csv", delimiter=",")

world_pop = pd.read_csv("EDU_DEM_13052024180357081.csv", delimiter= ",")

# Create a TimeSeries, specifying the time and value columns
series = TimeSeries.from_dataframe(world_pop, "Year", "Value")

# Set aside the last 36 months as a validation series
train, val = series[:-36], series[-36:]

model = ExponentialSmoothing()
model.fit(train)
prediction = model.predict(len(val), num_samples=1000)