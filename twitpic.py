#!/usr/bin/env python
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

API_URL = 'http://twitpic.com/api/uploadAndPost'

def upload_file(filename, username = "", password = "", message = "" ):
    register_openers()
    data = {'media' :open(filename),
            'username': username,
            "password": password,
            'message': message
            }
    datagen, headers = multipart_encode(data)
    req = urllib2.Request(API_URL, datagen,headers)
    u = urllib2.urlopen(req)
    return u.read()

if __name__ == "__main__":
    import sys
    print upload_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    
    
    
