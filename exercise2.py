import geocoder
import requests

# Replace XXXXXXXXXXXX with your actual key, which
# will look like a bunch of letters and numbers!
API_KEY = 'XXXXXXXXXXXX'
# When you are done with the homework, remove your actual key
# and replace it back with XXXXXXXXXXXXXXXXXX before you commit
# and push to Github.

API_BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?units=imperial&appid={API_KEY}'

def main():
  destinations = ???

  # Loop through each destination
  for destination in destinations:
    ###########
    # COPY & PASTE RELEVANT CODE FROM PART 1 HERE
    ###########

    # You'll need to construct the full API url with the latitude and longitude,
    # with something like this:
    # full_api_url = API_BASE_URL + '&lat=' + latitude + '&lon=' + longitude

    result = requests.get(full_api_url).json()

    # From the result, print out the summary and current temperature

main()
