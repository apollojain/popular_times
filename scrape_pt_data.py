# import libraries
'''
'https://www.google.com/maps/place/Recreational+Sports+Facility/@37.868727,-122.2645519,17z/data=!3m1!4b1!4m5!3m4!1s0x80857c27cc9713eb:0x13657f86e249d525!8m2!3d37.8687228!4d-122.2623632'
'https://maps.google.com/?cid=3061752025524222642'
'''
import re, utils, argparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import get_place_data as gpt

SUNDAY = "Sunday"
MONDAY = "Monday"
TUESDAY = "Tuesday"
WEDNESDAY = "Wednesday"
THURSDAY = "Thursday"
FRIDAY = "Friday"
SATURDAY = "Saturday"

DAYS = [SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]

def try_pt_html_from_url(url, browser, delay=6):
    # browser = webdriver.Firefox()
    browser.get(url)
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'section-popular-times-container')))
        innerHTML = myElem.get_attribute('innerHTML').encode('utf-8')
        print("Page is ready!")
        return innerHTML
    except TimeoutException:
        print("Loading took too much time!")
        return None

def process_hour_to_military_time(hour, ampm):
    if (ampm == 'P' and hour != 12) or (ampm == 'A' and hour == 12):
        hour += 12
    return hour

def weekday_info_array_helper(weekday_sre_match): 
    n = len(weekday_sre_match)
    hourly_popularity = [0 for i in range(24)]
    for i in range(n):
        regular, current = weekday_sre_match[i]
        hour = 0
        popularity = 0
        if current == '':
            processed = re.findall("([0-9]+)% busy at ([0-9]+) (A|P)", regular)
            if len(processed) == 1: 
                result = processed[0]
                popularity = int(result[0])
                hour = int(result[1])
                ap = result[2]
                hour = process_hour_to_military_time(hour, ap)
        else: 
            '''
            Edge cases: 
            - 11 am is i - 1
            - 11 pm is i - 1
            - 12 pm is i + 1
            - 12 am is i + 1
            '''
            processed = re.findall("usually ([0-9]+)% busy", current)
            if len(processed) == 1: 
                popularity = int(processed[0])
                if i == 0: 
                    regular, current = weekday_sre_match[i + 1]
                    placeholder = re.findall("([0-9]+)% busy at ([0-9]+) (A|P)", regular)
                    result = placeholder[0]
                    hour = int(result[1]) 
                    ap = result[2]
                    hour = process_hour_to_military_time(hour, ap)
                    hour -= 1
                else: 
                    regular, current = weekday_sre_match[i - 1]
                    placeholder = re.findall("([0-9]+)% busy at ([0-9]+) (A|P)", regular)
                    result = placeholder[0]
                    hour = int(result[1])
                    ap = result[2]
                    hour = process_hour_to_military_time(hour, ap)
                    hour += 1
        hour %= 24
        hourly_popularity[hour] = popularity
    return hourly_popularity

        
def get_headless_browser():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(firefox_options=options)
    return browser


def get_weekday_info(weekday_div):
    matches = re.findall("([0-9]+% busy at [0-9]+ [A|P])|(usually [0-9]+% busy)", str(weekday_div))
    hours_pop_arr = weekday_info_array_helper(matches)
    return hours_pop_arr


def get_dictionary_from_pt_html(pt_html):
    '''
    pt_html is the html recieved from the try_pt_html_from_url function
    '''
    if pt_html: 
        pt_dictionary = {}
        soup = BeautifulSoup(pt_html, 'html.parser')
        pt_divs = soup.findAll("div", {"class": "section-popular-times-graph"})
        n = len(pt_divs)
        for i in range(n):

            day_key = DAYS[i]
            weekday_div = pt_divs[i]
            day_array = get_weekday_info(weekday_div)
            pt_dictionary[day_key] = day_array
        print(pt_dictionary)
        return pt_dictionary
    else: 
        return None

def get_pt_data_from_places_dict(places_dict, browser): 
    url = places_dict['url']
    pt_html = try_pt_html_from_url(url, browser)
    if pt_html: 
        pt_dictionary = get_dictionary_from_pt_html(pt_html)
        places_dict["popular_times"] = pt_dictionary
    
