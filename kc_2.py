import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read in csv and fix dtype errors
df = pd.read_csv(r'assets/UFO_sightings_scrubbed.csv')
df["duration (seconds)"].astype(float)
df["latitude"].astype(float)

#change unique feild to NAN 
df.replace('unknown', np.nan, inplace=True)

#count number of times each UFO shape is reported
sphere_count = df['shape'].value_counts()["sphere"]
cone_count = df['shape'].value_counts()["cone"]
diamond_count = df['shape'].value_counts()["diamond"]
flare_count = df['shape'].value_counts()["flare"]
changed_shape_count = df['shape'].value_counts()["changed"]
other_shape_count = df['shape'].value_counts()["other"]

#group all shapes, sort, create labels
all_shapes = [sphere_count, cone_count, diamond_count, flare_count, changed_shape_count, other_shape_count]
all_shapes_sorted = all_shapes.sort(reverse=True)
shape_names = ["Sphere", "Cone", "Diamond", "Flare", "Changed Shape", "Other"]

#create and format pie chart
plt.style.use("ggplot")
plt.bar(shape_names, all_shapes)

plt.title("Reported Shapes of UFOs (1906-2014)")
plt.xlabel("Reported Shape")
plt.ylabel("Number of Reports")

plt.show()