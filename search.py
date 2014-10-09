##############################################
#  Alright so this program basically takes
#  a keyword (in this case "the odyssey")
#  and returns the html of the page we would
#  receive if we searched for it on biblion
#  I'll add author, title, and subject
#  searches later.
#  --Atticus
##############################################

from urllib import urlencode
from urllib2 import *
kwrd="the odyssey"
values=""
values=values+urlencode({"searchtype" : "X"})
values=values+"&"+urlencode({"SORT" : "D"})
values=values+"&"+urlencode({"searcharg" : kwrd})
content=urlopen(Request("http://biblion.exeter.edu/search/"+"?"+values)).read()
print content
