import json, math
from shapely.geometry import shape, Point
import geopy.distance

def in_geojson(geojson_shape, lat, lng): 
	# NEED TO FIX THIS
	point = Point(lng, lat)
	return geojson_shape.contains(point)

def get_geojson_geometry(geojson_filename):
	with open(geojson_filename) as json_data: 
		d = json.load(json_data)
		features = d['features'][0]
		geometry = features['geometry']
		return geometry

def get_geojson_lat_lng_pts(geojson_geometry):
	# FIX THIS UP!!!!
	coordinates = geojson_geometry['coordinates'][0]
	lat_longs = [[pair[1], pair[0]] for pair in coordinates]
	return lat_longs

def two_point_distance(location_1, location_2):
	'''
	location_1 and location_2 should be (lat, lng) pairs
	'''
	return geopy.distance.vincenty(location_1, location_2).m


def get_sample_points_from_geojson(geojson_file, num_latitudes=10, num_longitudes=10):
	'''
	DESCRIPTIONS
	------------
	
	'''
	geojson_geometry = get_geojson_geometry(geojson_file)
	gj_lat_lng_pts = get_geojson_lat_lng_pts(geojson_geometry)
	lat_pts = [pair[0] for pair in gj_lat_lng_pts]
	lon_pts = [pair[1] for pair in gj_lat_lng_pts]
	min_lat, max_lat = min(lat_pts), max(lat_pts)
	min_lng, max_lng = min(lon_pts), max(lon_pts)
	lat_lng_sampling_locations = [] 

	lat_width = float(max_lat - min_lat)/float(num_latitudes)
	lon_width = float(max_lng - min_lng)/float(num_longitudes)

	geojson_shape = shape(geojson_geometry)
	cur_lat, cur_lng = min_lat, min_lng 
	while cur_lat < max_lat:
		while cur_lng < max_lng: 


			if in_geojson(geojson_shape, cur_lat, cur_lng): 
				lat_lng_sampling_locations.append([cur_lat, cur_lng])

			cur_lng += lon_width
		cur_lng = min_lng 
		cur_lat += lat_width

	point_1 = (min_lat, min_lng)
	point_2 = (min_lat + lat_width, min_lng + lon_width)
	diameter = two_point_distance(point_1, point_2)

	results = {} 
	results['radius'] = diameter/1.5 
	results['lat_lng_sampling_locations'] = lat_lng_sampling_locations
	return results

def sample_locations_to_file(key_name, input_geojson, output_filepath, num_latitudes=10, num_longitudes=10):
	results = get_sample_points_from_geojson(input_geojson, num_latitudes, num_longitudes)
	results['key'] = key_name
	with open(output_filepath, 'w') as fp:
		json.dump(results, fp)
	
if __name__ == '__main__':
	sample_locations_to_file('cancun', 'inputs/geojson_files/cancun.geojson', 'inputs/sample_locations/cancun_samples.json')
	# sample_locations_to_file('chihuahua', 'inputs/geojson_files/chihuahua.geojson', 'inputs/sample_locations/chihuahua_samples.json')
	# sample_locations_to_file('guadalajara', inputs/geojson_files/guadalajara.geojson', 'inputs/sample_locations/guadalajara_samples.json')
	# sample_locations_to_file('juarez', 'inputs/geojson_files/juarez.geojson', 'inputs/sample_locations/juarez_samples.json')
	# sample_locations_to_file('mexicali', 'inputs/geojson_files/mexicali.geojson', 'inputs/sample_locations/mexicali_samples.json')
	# sample_locations_to_file('monterrey', 'inputs/geojson_files/monterrey.geojson', 'inputs/sample_locations/monterrey_samples.json')
	# sample_locations_to_file('morelia', 'inputs/geojson_files/morelia.geojson', 'inputs/sample_locations/morelia_samples.json')
	# sample_locations_to_file('tijuana', 'inputs/geojson_files/tijuana.geojson', 'inputs/sample_locations/tijuana_samples.json')
	# sample_locations_to_file('veracruz', 'inputs/geojson_files/veracruz.geojson', 'inputs/sample_locations/veracruz_samples.json')


	