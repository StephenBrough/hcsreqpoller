
# Hunter Thornsberry
# http://www.adventuresintechland.com

# Additions: Stephen Brough

# WebChange.py
# Alerts you when a webpage has changed it's content by comparing checksums of the html.

import hashlib
import urllib2
import random
import time
from bs4 import BeautifulSoup
import sys
from playsound import playsound

# url to be scraped
url = "https://www.halowaypoint.com/en-us/forums/6e35355aecdf4fd0acdaee3cc4156fd4/topics/hcs-dreamhack-atlanta-code-thread/317738ec-d0c8-4473-ab1c-473aac0c4b40/posts?page=3"
page = 0

# time between checks in seconds
sleeptime = 20
current_count = 0

def getHash():
    return hashlib.sha224(getHtmlPage()).hexdigest()

def getCount():
    global current_count
    print "\tGetting count..."
    print "\t\tCount is currently:",current_count
    soup =  BeautifulSoup(getHtmlPage(), 'html.parser')
    print"\t\tGot soup..."
    list = soup.find_all('div', {"class": "region--post"})
    print"\t\tGot list..."
   
    return len(list)

def setCurrentPage():
    print "\tSetting current page..."
    global page
    global url
    global current_count

    print "\t\tPage:",page
    current_count = getCount()
    print"\t\tCurrent count:",current_count
    while current_count == 20:
        url = url[:-len(str(page))]
        page = page + 1
        print "\t\t\tPage Update:",page
        url = url + str(page)
        
        current_count = getCount()
        print"\t\t\tCurrent count update:",current_count
        print"\t\t\tUrl update:",url[-len("page=123"):]

def getHtmlPage():
    global url
    print "\tGetting html page..."
     # random integer to select user agent
    randomint = random.randint(0,7)
    the_page = None

    # User_Agents
    # This helps skirt a bit around servers that detect repeaded requests from the same machine.
    # This will not prevent your IP from getting banned but will help a bit by pretending to be different browsers
    # and operating systems.
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
    ]

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', user_agents[randomint])]
    print "\t\tSending request..."
    while the_page == None:
        try:
            response = opener.open(url, timeout=4)
            print "\t\tGot response..." # This prints, but then hangs sometimes - put a try/catch around the response.read()
            print"\t\tResponse Code:",response.code
            print"\t\tResponse URL:",response.geturl()
            # print"\t\tResponse:",response
            #print"\t\tResponse read:",response.read()
            the_page = response.read()
            print "\t\tRead the page..."
        except: 
            print "\tRetrying attempt..."
            pass

    return the_page

setCurrentPage()
current_count = getCount()


while 1: # Run forever
    if getCount() == current_count: # If nothing has changed
        print "Not Changed"
        print "\tCurrent Count:", current_count
        print "\tOn page:",page
    else: # If something has changed
        print "Changed"
        print "\tCurrent Count:",current_count
       # url = url{:-1}
        playsound('mgs.mp3')
        setCurrentPage()
        current_count = getCount()

    time.sleep(sleeptime)