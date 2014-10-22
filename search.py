##############################################
#  Alright so this program basically takes
#  a keyword (in this case "the odyssey")
#  and prints the author, title, biblion
#  link, and status of all copies for the
#  first 50 results.
#  I'll add author, title, and subject
#  searches later, and if there is anything
#  else that needs shown in the preliminary
#  query, I'll fix it during the next
#  ECC meeting.
#  --Atticus
##############################################

from urllib import urlencode
from urllib2 import *
from re import findall, search, DOTALL

def printb(biblink, title, author, status):
        if not biblink:
                biblink="N/A"
        if not title:
                title="N/A"
        if not author:
                author="N/A"
        if not status:
                status="N/A"
        print "Title:  "+title
        print "By:     "+author
        print "@:      "+biblink
        print "Status: "+status
        print "\n\n\n"

kwrd="the odyssey"
stype="X"
values=""
values=values+urlencode({"searchtype" : stype})
values=values+"&"+urlencode({"SORT" : "D"})
values=values+"&"+urlencode({"searcharg" : kwrd})
content=urlopen(Request("http://biblion.exeter.edu/search/"+"?"+values)).read()
content=findall('<div class="briefcitDetailMain">(.+?)<div class="briefcitDetail">', content, DOTALL)
for book in content:
        (biblink, title, author)=findall(r'<a href="(.+?)">(.*?)</a>.*?<br.*?>(.+?)<', book, DOTALL)[0]
        biblink="http://biblion.exeter.edu/"+biblink
        biblink=biblink.replace("\r", "").replace("\n", "")
        title=title.replace("\r", "").replace("\n", "")
        author=author.replace("\r", "").replace("\n", "")
        status=findall(r'<tr  class="bibItemsEntry">(.*?)</tr>', book, DOTALL)
        if len(status)>0:
                for a in range(0, len(status)):
                        status[a]=search(r'<td.*?>.*?</td>.*?<td.*?>.*?</td>.*?<td.*>(.*?)</td>', status[a], DOTAL$
                status=" ||| ".join(status).replace("&nbsp;", "")
        else:
                status=None
        printb(biblink, title, author, status)
