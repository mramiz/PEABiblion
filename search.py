##############################################
#  Alright so this program basically takes
#  a keyword (in this case "the odyssey")
#  and prints the author, title, and biblion
#  link for the first 50 results.
#  I'll add author, title, and subject
#  searches later, and if there is anything
#  else that needs shown in the preliminary
#  query, I'll fix it during the next
#  ECC meeting.
#  --Atticus
##############################################

from urllib import urlencode
from urllib2 import *
from re import findall, DOTALL

def printb(biblink, title, author):
        print "Title: "+title
        print "By:    "+author
        print "@:     "+biblink
        print "\n\n\n"

kwrd="the odyssey"
stype="X"
values=""
values=values+urlencode({"searchtype" : stype})
values=values+"&"+urlencode({"SORT" : "D"})
values=values+"&"+urlencode({"searcharg" : kwrd})
content=urlopen(Request("http://biblion.exeter.edu/search/"+"?"+values)).read()
content=findall('<div class="briefcitDetail">(.+?)&nbsp;</div>', content, DOTALL)
for book in content:
        (biblink, title, author)=findall('<a href="(.+?)">(.*?)</a>.*?<br.*?>(.+?)<', book, DOTALL)[0]
        biblink="http://biblion.exeter.edu/"+biblink
        biblink=biblink.replace("\r", "").replace("\n", "")
        title=title.replace("\r", "").replace("\n", "")
        author=author.replace("\r", "").replace("\n", "")
        printb(biblink, title, author)
