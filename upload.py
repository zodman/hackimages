#!/usr/bin/env python
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

API_URL = 'http://www.imageshack.us/index.php'

def yesno(x):
    if x:
        return 'yes'
    else:
        return 'no'

def upload_file(filename, optsize=None,
                user_cookie=None,
                remove_bar=True,
                tags=None,
                public=True,
                ):
    register_openers()
    data = {'fileupload' :open(filename),
            'xml':yesno(True)
            }
    datagen, headers = multipart_encode(data)

    # Some optional parameters
    if optsize:
        data['optsize'] = optsize
    if user_cookie:
        data['cookie'] = user_cookie
    if tags:
        data['tags'] = tags
    
    req = urllib2.Request(API_URL, datagen,headers)
    u = urllib2.urlopen(req)
    return u.read()

if __name__ == "__main__":
    import sys
    print upload_file(sys.argv[1])
    
    
    
