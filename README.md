# FarmStack 

Proof-of-concept for an open API for agri data powered by Wageningen University's AgroDataCube.  

Endpoint: http://farmstack.nl/api/v1/

Docs: http://farmstack.nl/api/v1/docs/

Forum: https://forum.farmstack.nl


# Usage

The API currently contains one dataset: gewaspercelen. It contains all agricultural parcels in The Netherlands. See http://farmstack.nl/api/v1/gewaspercelen.

## Geo filters

### Point

You can request a single parcel by supplying a location through the `?point=x,y` request parameter like so [http://farmstack.nl/api/v1/gewaspercelen/?point=210641,489026](http://farmstack.nl/api/v1/gewaspercelen/?point=210641,489026).

### Bounding Box

TODO