import geocoder

def main():
  # Declare destinations list here
  destinations = ['Space Needle', 'Crater Lake', 'Golden Gate Bridge', 'Yosemite National Park',
  'Las Vegas, Nevada', 'Grand Canyon National Park', 'Aspen, Colorado', 'Mount Rushmore', 'Yellowstone National Park', 
  'Sandpoint, Idaho', 'Banff National Park', 'Capilano Suspension Bridge']

  # Loop through each destination
  for destination in destinations:
    #   Get the lat-long coordinates from `geocoder.arcgis`
    location = geocoder.arcgis(destination)
    #   Print out the place name and the coordinates
    print(f'{destination} is located at ({location.latlng[0]:.4f}, {location.latlng[1]:.4f})')
    
main()
