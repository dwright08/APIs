import geocoder
import requests

# Replace XXXXXXXXXXXX with your actual key, which
# will look like a bunch of letters and numbers!
API_KEY = XXXXXXXXXXXXXXXXXX
# When you are done with the homework, remove your actual key
# and replace it back with XXXXXXXXXXXXXXXXXX before you commit
# and push to Github.

API_BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?units=imperial&appid={API_KEY}'

def main():
  destinations = ['Space Needle', 'Crater Lake', 'Golden Gate Bridge', 'Yosemite National Park',
  'Las Vegas, Nevada', 'Grand Canyon National Park', 'Aspen, Colorado', 'Mount Rushmore', 'Yellowstone National Park', 
  'Sandpoint, Idaho', 'Banff National Park', 'Capilano Suspension Bridge']

  # Loop through each destination
  for destination in destinations:
    ###########
    # COPY & PASTE RELEVANT CODE FROM PART 1 HERE
    ###########
    location = geocoder.arcgis(destination)
    print(f'{destination} is located at ({location.latlng[0]:.4f}, {location.latlng[1]:.4f})')
    # You'll need to construct the full API url with the latitude and longitude,
    # with something like this:
    # full_api_url = API_BASE_URL + '&lat=' + latitude + '&lon=' + longitude
    
    #latitude = f'{location.latlng[0]:.4f}'
    #longitude = f'{location.latlng[1]:.4f}'

    
    full_api_url = f'{API_BASE_URL}&lat={location.latlng[0]:.4f}&lon={location.latlng[1]:.4f}'
    
    result = requests.get(full_api_url).json()
  
    # From the result, print out the summary and current temperature
    print(f"At {destination} right now, it's {result['weather'][0]['description']} with a temperature of {result['main']['temp']}")
main()
