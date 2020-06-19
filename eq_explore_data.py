import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

# Store the data in a dictionary
all_eq_dicts = all_eq_data['features']

# Locate magnitude data
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])