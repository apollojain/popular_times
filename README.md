# Popular Times Library

This package allows for users to gain access to the Google Popular Times feature. To use this package, it is first necessary to install geckodriver, which will be used by Selenium to spin up a headless Firefox browser. Google how to do this on your OS. On Macs, the command is: 
```
brew install geckodriver
```

It is next necessary to download a few otherpackages using the following commands: 

```
pip install beautifulsoup4
pip install python-google-places
pip install selenium
```

After this, we can install our package: 
```
pip install popular_times
```

We can use the package by running this function
```
>>> import popular_times as pt
>>> pt.popular_times_search(api_key, keyword, language, lat_lng, location, name, pagetoken, radius, rankby, sensor, type, types)
```

The parameters are as follows (taken from python-google-places README): 
```
api_key -- Your Google Places API Key 

keyword  -- A term to be matched against all available fields, including but
            not limited to name, type, and address (default None)

language -- The language code, indicating in which language the results
            should be returned, if possble. (default en)

lat_lng  -- A dict containing the following keys: lat, lng (default None)

location -- A human readable location, e.g 'London, England' (default None)

name     -- A term to be matched against the names of the Places.
            Results will be restricted to those containing the passed name value. (default None)

pagetoken-- Optional parameter to force the search result to return the next
            20 results from a previously run search. Setting this parameter
            will execute a search with the same parameters used previously. (default None)

radius   -- The radius (in meters) around the location/lat_lng to restrict
            the search to. The maximum is 50000 meters (default 3200)

rankby   -- Specifies the order in which results are listed:
            'prominence' (default) or 'distance' (imply no radius argument)

sensor   -- Indicates whether or not the Place request came from a device
            using a location sensor (default False)

type     -- An optional type used for restricting the results to Places (default None)

types    -- An optional list of types, restricting the results to Places (default []).
            This kwarg has been deprecated in favour of the 'type' kwarg.
```
The output will be an array of dictionaries that looks like this: 
```
[
    {
        'name' = 'SOME_NAME'
        'place_id' = 'SOME_ID'
        'geo_location' = SOME_LOCATION, 
        'url': 'SOME_URL', 
        'popular_times': {
            'Monday': [0, 0, 0, 0, 0, 0, 8, 13, 19, 25, 30, 33, 33, 31, 31, 37, 50, 71, 90, 100, 92, 70, 44, 23], 
            'Tuesday': [0, 0, 0, 0, 0, 0, 7, 13, 22, 29, 34, 34, 30, 26, 25, 34, 53, 77, 90, 86, 71, 64, 58, 31], 
            'Friday': [0, 0, 0, 0, 0, 0, 8, 15, 23, 31, 36, 37, 35, 32, 33, 42, 56, 68, 70, 62, 55, 52, 36, 0], 
            'Wednesday': [0, 0, 0, 0, 0, 0, 11, 21, 31, 37, 36, 31, 27, 27, 34, 44, 55, 63, 69, 75, 76, 65, 43, 20], 
            'Thursday': [0, 0, 0, 0, 0, 0, 8, 13, 19, 24, 28, 30, 29, 25, 22, 28, 51, 83, 93, 77, 65, 66, 54, 27], 
            'Sunday': [0, 0, 0, 0, 0, 0, 0, 0, 17, 30, 40, 42, 37, 31, 31, 38, 47, 50, 47, 43, 45, 46, 35, 18], 
            'Saturday': [0, 0, 0, 0, 0, 0, 0, 0, 14, 28, 43, 50, 46, 35, 28, 29, 37, 45, 44, 38, 41, 49, 33, 0]
        }
    }, 
    ...
]
```