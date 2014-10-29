from urllib import urlencode
from urllib2 import *
from re import findall, search, DOTALL

#def search(req, kwrd, stype):
def searchr(req):
	kwrd="the odyssey"
	stype="X"
	values=""
	values=values+urlencode({"searchtype" : stype})
	values=values+"&"+urlencode({"SORT" : "D"})
	values=values+"&"+urlencode({"searcharg" : kwrd})
	content=urlopen(Request("http://biblion.exeter.edu/search/"+"?"+values)).read()
	content=findall('<div class="briefcitDetailMain">(.+?)<div class="briefcitDetail">', content, DOTALL)
	result=""
	for book in content:
		(biblink, title, author)=findall(r'<a href="(.+?)">(.*?)</a>.*?<br.*?>(.+?)<', book, DOTALL)[0]
		biblink="http://biblion.exeter.edu/"+biblink
		biblink=biblink.replace("\r", "").replace("\n", "")
		title=title.replace("\r", "").replace("\n", "")
		author=author.replace("\r", "").replace("\n", "")
		status=findall(r'<tr  class="bibItemsEntry">(.*?)</tr>', book, DOTALL)
		if len(status)>0:
			for a in range(0, len(status)):
				status[a]=search(r'<td.*?>.*?</td>.*?<td.*?>.*?</td>.*?<td.*>(.*?)</td>', status[a], DOTALL).group(1)
			status=" ||| ".join(status).replace("&nbsp;", "")
		else:
			status=None
		if not biblink:
			biblink="N/A"
		if not title:
			title="N/A"
		if not author:
			author="N/A"
		if not status:
			status="N/A"
		result=result+'''
			<div class="result">
                  	        <img src="http://atticusstonestrom.com/biblion/hungergames.jpg"/>
                                <p class="title">%s</p>
				<p>By: %s</p>
                                <p>Call Number: K4TN155</p>
                                <p>Status: %s</p>
                        </div>''' % (title, author, status)





	html='''
<!DOCTYPE html>
<html>
	<head>
	<link type= "text/css" rel= "stylesheet" href= "http://atticusstonestrom.com/biblion/librarystylesheet.css"/>
	<title>Main Page Shell</title>
	</head>
	<body>
	
		<div id="header">
			<img id="pealogo" src="http://atticusstonestrom.com/biblion/pex.png"/>
			
		</div>
		
		<div class="thinbanner right">
		
		</div>
		
		<div class="thinbanner left">
		</div>
		
		<div class="middle">
			<div class="raisedsearchbar">
				Search
			</div>
			%s
			<div id="narrow">
				<ul>
					<li>
						<strong>Status</strong>
						<ul>
							<li>
								Available
							</li>
							<li>
								Checked Out
							</li>
							<li>
								Coming Soon
							</li>
						</ul>
					</li>
					<li>
						<strong>Material Type</strong>
						<ul>
							<li>
								Book
							</li>
							<li>
								E-Book
							</li>
							<li>
								DVD
							</li>
							<li>
								Audio Book
							</li>
						</ul>
					</li>
					<li>
						<strong>Rating</strong>
						<ul>
							<li>
								Unrated
							</li>
							<li>
								0-1 Stars
							</li>
							<li>
								1-2 Stars
							</li>
							<li>
								2-3 Stars
							</li>
							<li>
								3-4 Stars
							</li>
							<li>
								4-5 Stars
							</li>
						</ul>
					</li>
					<li>
						<strong>Subject</strong>
						<ul>
							<li>
								History
							</li>
							<li>
								Science
							</li>
							<li>
								Technology
							</li>
							<li>
								Modern Languages
							</li>
							<li>
								Ancient Languages
							</li>
							<li>
								Mathematics
							</li>
						</ul>
					</li>
					<li>
						<strong>Type</strong>
						<ul>
							<li>
								Fiction
							</li>
							<li>
								Non-fiction
							</li>
						</ul>
					</li>
				</ul>
		</div>
		
		
		
		<div class="footer">
			Various Contact Information Will Go Here
		</div>
		
	</body>
</html>''' % result
	return html
