#!/usr/bin/env python


from geopy.geocoders import Nominatim

def getcoord (address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    print((location.latitude, location.longitude))
    return { "latitude": location.latitude, "longitude": location.longitude}

def getaddress (x, y):
    geolocator = Nominatim()
    location = geolocator.reverse(x + "," + y)
    return location.address

def main( argv ):
    """
    Script execution entry point
    @param argv         Arguments passed to the script
    @return             Exit code (0 = success)
    """

    # imports when using this as a script
    import argparse

    # create and configure an argument parser
    parser = argparse.ArgumentParser(
        description = 'A Shell Script',
        add_help    = False
    )
    parser.add_argument(
        '-h',
        '--help',
        default = False,
        help    = 'Prints a geojson point with these args: --address (-a) --name (-n) and --type (-t)',
        action  = 'help'
    )
    parser.add_argument(
        '-n',
        '--name',
        default = False,
        help    = 'Give the name of the item.',
        action  = 'store',
    )
    parser.add_argument(
        '-t',
        '--type',
        default = False,
        help    = 'Give the type of the item.',
        action  = 'store',
    )
    parser.add_argument(
        '-a',
        '--address',
        default = False,
        help    = 'Give the address of the item.',
        action  = 'store',
    )

    # parse the arguments
    args = parser.parse_args( argv[ 1 : ] )

    coord = getcoord (args.address)

    feature = '\n\
    {\n\
      "type": "Feature",\n\
      "properties": {\n\
        "marker-color": "#0076A8",\n\
        "marker-size": "medium",\n\
        "marker-symbol": "",\n\
        "nom": "' + args.name + '",\n\
        "type": "' + args.type + '",\n\
        "adresse": "' + args.address + '"\n\
      },\n\
      "geometry": {\n\
        "type": "Point",\n\
        "coordinates": [\n\
          ' + str(coord["longitude"]) + ',\n\
          ' + str(coord["latitude"]) + '\n\
        ]\n\
      }\n\
    }'
    print (feature)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit( main( sys.argv ) )
