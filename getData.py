import urllib.request
import json
import ssl
import certifi

# Create an SSL context using certifi's CA bundle
context = ssl.create_default_context(cafile=certifi.where())

# The base URL to access the NFRA API
base_url = "https://nrfaapps.ceh.ac.uk/nrfa/ws"
format = "format=json-object"

stations = [53001, 53002, 53003, 53004, 53005, 53006, 53007, 53008, 
            53013, 53017, 53018, 53019, 53020, 53022, 53023, 53024, 
            53025, 53026, 53028, 53029]

fields = ["lcm2007", "geology", "catchment-rainfall"] 
# Land cover map data (2007): lcm2007-woodland, lcm2007-arable-horticultural, 
# lcm2007-grassland, lcm2007-mountain-heath-bog, lcm2007-urban.
# Catchment geology data: high-perm-bedrock, moderate-perm-bedrock, low-perm-bedrock, 
# mixed-perm-bedrock, high-perm-superficial, low-perm-superficial, mixed-perm-superficial.
# Catchment rainfall standard period data: saar-1941-1970, saar-1961-1990.
formattedFields = ",".join(fields)

for station in stations:

    stations_info_url = "{BASE}/station-info?station={STATION}&{FORMAT}&fields={FIELDS}".format(BASE=base_url,
                                                            STATION=station, FORMAT=format, FIELDS=formattedFields)
    # Send request and read response
    response = urllib.request.urlopen(stations_info_url, context=context).read()

    # Decode from JSON to Python dictionary
    response = json.loads(response)

    # See info from each station
    stations_info = response['data']
    print("Station {STATION} info:".format(STATION=station))
    for station_info in stations_info:
        print(station_info)
    print()