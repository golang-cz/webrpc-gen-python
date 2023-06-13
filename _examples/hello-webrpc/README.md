hello-webrpc
============

* Server: Flask (Python)
* Client: Web Browser

Simple client+server app with Flask backend (server) and 
Web client.

1. `$ make tools` - to download `webify` cli to serve the 
'webapp/' local files
2. `$ make run-server` - to start the  server
3. Open your browser to https://localhost:5000/ and open 
your console, tada

webrpc comes with its own schema design language called 
RIDL, which stands for "RPC interface
design language" :) it reads and feels like documentation, 
but it very flexible. See
[hello-api.ridl](./hello-api.ridl) for the RIDL file for 
this service.

as well, webrpc supports a json-formatted schema with the 
identical functionality as the RIDL format.
See here, 
[hello-api.webrpc.json](./hello-api.webrpc.json).

