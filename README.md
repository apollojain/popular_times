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
pip install popular-times
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