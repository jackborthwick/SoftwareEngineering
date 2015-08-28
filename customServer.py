#!/usr/bin/env python
from wsgiref.simple_server import make_server
import json
# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object (see PEP 333).
def custom_app(environ, start_response):#call apps in this simple server below to set the differnet parts of text etc.
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'text/plain; charset=utf-8')] # HTTP Headers
    start_response(status, headers)
    request_method = environ["REQUEST_METHOD"]
    path_info = environ["PATH_INFO"]
    query_string = environ["QUERY_STRING"]
    try:
        content_length = int(environ["CONTENT_LENGTH"])
    except(ValueError):
        content_length = 0
        print("CONTENT LENGTH IS 0")

    body =  environ['wsgi.input'].read(int(content_length)).decode('utf-8')

    print("method " + request_method)
    print("path " + path_info)
    print("query " + query_string)
    print("length " + str(content_length))
    if (body):
        print("body " + body)
    environProperties = {'REQUEST_METHOD':request_method,'PATH_INFO':path_info, 'QUERY_STRING':query_string, 'CONTENT_LENGTH':str(content_length), 'BODY':body }
    
    return [json.dumps(environProperties).encode('utf-8')]
    # The returned object is going to be printed
    #return [b]

httpd = make_server('', 8000, custom_app)
print("Serving on port 8000...")

# Serve until process is killed
httpd.serve_forever()