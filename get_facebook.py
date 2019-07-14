import facebook

import configparser
config = configparser.RawConfigParser()
config.read('config.ini')

accesstoken = config.get('Facebook', 'access_token')
print (accesstoken)


graph = facebook.GraphAPI(access_token=accesstoken, version="2.12")

# Search for places near 1 Hacker Way in Menlo Park, California.
places = graph.search(type='place',
                      center='46.814309,-71.207917',
                      distance=1000,
                      fields='name,checkins,location')

# Each given id maps to an object the contains the requested fields.
for place in places['data']:
    print('%s %s' % (place['name'].encode(),place['location'].get('zip')))
    print (place['checkins'])