# List compreheension
symbols = '$%¨(@#&'
codes = [ord(symbol) for symbol in symbols]
print(codes)

x = 'my precious'
dummy = [x for x in 'ABC']
print(x, dummy)

# Listcomps x Map and filter
symbols = '$%¨(@#&'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c>127, map(ord, symbols)))
print(beyond_ascii)

# listcomps: cartesian product
colors = ['black', 'blue']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors 
                         for size in sizes]
print(tshirts)

# Genexps: use the same syntax as listcomps, but are enclosed in parentheses rather than brackets.
symbols = '$¢£¥€¤'
beyond_ascii = tuple(ord(s) for s in symbols)
print(beyond_ascii)

import array
ar = array.array('I', (ord(symbol) for symbol in symbols))
print(ar)

# Genexps: cartesian product
colors = ['black', 'blue']
sizes = ['S', 'M', 'L']
for tshirt in ('%s - %s' % (c, s) for c in colors 
                                for s in sizes):
                                    print(tshirt)