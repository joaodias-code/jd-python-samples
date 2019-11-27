# tuples
city, year, pop, chg, area = (' Tokyo', 2003, 32450, 0.66, 8014)
print(city, year, pop, chg, area)

traveler_ids = [(' USA', '31195855'), (' BRA', 'CE342567'), (' ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s / %s' % passport)

# "_": valor não interessa (descarta) 
for country, _ in traveler_ids:
    print(country)

# tuple unpacking
lax_coordinates = (33.95, -118.40)
latitude, longitude = lax_coordinates

print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

import os
_, filename = os.path.split('home/luciano/.ssh/idrsa.pub')
print(filename)

# using " * " grab
a, b, *rest = range(5)
print([a, b, rest])

a, *body, c, d = range(5)
print(a, body, c, d)

# nested tuples
metro_areas = [ (' Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
                (' Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)), 
                (' Mexico City', 'MX', 20.142, (19.433333, -99.133333)), 
                (' New York-Newa', 'US', 20.104, (40.808611, -74.020386)), 
                (' Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)), ]

print('{:15} | {:^9} | {:^9}'. format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas: 
    if longitude <= 0: 
        print(fmt.format(name, latitude, longitude))

# named tuples
from collections import namedtuple

city = namedtuple('City', 'name country population coordinates')
tokyo = city('Tokyo', 'JP', 36.933, (35.693, 139.9349))
print(tokyo)
print(tokyo.name, tokyo.population)
print(tokyo[3])
print(tokyo._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong( 28.613889, 77.208889))
delhi = city._make(delhi_data)
print(delhi)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ":", value)




