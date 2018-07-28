from googleplaces import GooglePlaces, types, lang
import get_pt_data
import pickle, json

def place_to_dict(place): 
    place_dict = {} 
    place.get_details()
    place_dict['name'] = place.name
    place_dict['place_id'] = place.place_id
    place_dict['geo_location'] = place.geo_location 
    place_dict['url'] = place.url
    return place_dict

def nearby_search(api_key, keyword=None, language='en', lat_lng=None, location=None, name=None, 
                pagetoken=None, radius=3200, rankby='prominence', sensor=False, type=None, types=[]):
    '''
    types can be found in https://github.com/slimkrazy/python-google-places/blob/master/googleplaces/types.py
    '''
    google_places = GooglePlaces(YOUR_API_KEY)
    if types == None: 
        types = []
    query_result = google_places.nearby_search(keyword=keyword, language=language, lat_lng=lat_lng, 
        location=location, name=name, pagetoken=pagetoken, radius=radius, rankby=rankby, sensor=sensor, 
        type=type, types=types)
    resulting_places = [place_to_dict(place) for place in query_result.places]
    return resulting_places

