import scrape_pt_data
import get_place_data

def popular_times_search(api_key, keyword=None, language='en', lat_lng=None, location=None, name=None, 
                pagetoken=None, radius=3200, rankby='prominence', sensor=False, type=None, types=[]): 
    browser = scrape_pt_data.get_headless_browser()
    resulting_places = get_place_data.nearby_search(api_key, keyword=keyword, language=language, lat_lng=lat_lng, 
    	location=location, name=name, pagetoken=pagetoken, radius=radius, rankby=rankby, sensor=sensor, 
    	type=type, types=types)
    for place_dict in resulting_places: 
        scrape_pt_data.get_pt_data_from_places_dict(place_dict, browser)
    return resulting_places
