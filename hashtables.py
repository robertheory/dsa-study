# Description: This file contains the implementation of a simple hashtable in Python

# A hashtable is a data structure that stores key-value pairs.
# It uses a hash function to compute an index into an array of buckets or slots
# from which the desired value can be found.
# The hash function will assign each key to a unique bucket in the hashtable.

cache = {}

cache['http://site.com'] = 'This is the content of the site'
cache['http://site.com'] = 'This is the content of the site'
cache['http://sample.net'] = 'This is the content of the sample site'
cache['http://onlymovies.com'] = 'This is the content of the onlymovies site'
cache['http://musikmedia.com'] = 'This is the content of the musikmedia site'
cache['http://supersups.com'] = 'This is the content of the supersups site'
cache['http://trueraggae.com'] = 'This is the content of the trueraggae site'
cache['http://itsbrazil.com'] = 'This is the content of the itsbrazil site'
cache['http://sheriffstore.com'] = 'This is the content of the sheriffstore site'

print(cache)
print(cache.keys())
print(cache.values())
