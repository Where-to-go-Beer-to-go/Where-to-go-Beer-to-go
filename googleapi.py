import googlemaps
import requests

gmaps = googlemaps.Client(key='AIzaSyDzmR8ASXf0heSJqmhFMmCDZ2-0fB7m4CQ')

api_key = 'AIzaSyDzmR8ASXf0heSJqmhFMmCDZ2-0fB7m4CQ'

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search
query = 'drinken in Groningen'

# get method of requests module
# return response object
r = requests.get(url + 'query=' + query +
                 '&key=' + api_key)

# json method of response object convert
#  json format data into python format data
x = r.json()

# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
y = x['results']

# keep looping upto length of y
for i in range(len(y)):
    # Print value corresponding to the
    # 'name' key at the ith index of y
    print(y[i]['name'])