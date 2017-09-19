from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from time import ctime as ct

# This file aims at scrapping a youtube channel in order to get data as:
# the number of subscribers, the number of views and the starting date of this
# particular channel.


channelName="Mister Geopolitix"
channelUrl="https://www.youtube.com/channel/UCX9lsdsTKfTi1eqoyL-RS-Q/about"

#Opening connection, grabbing the page
uClient = uReq(channelUrl)
pageHtml = uClient.read()
uClient.close()

# Using beautifulsoup module we parse the source code of the webpage
pageSoup = soup(pageHtml, "html.parser")

# We are seeking the 'about-stat' span section:
stats = pageSoup.findAll("span", {"class", "about-stat"})

# Values Extraction
nbSubs = stats[0].find("b").text.replace('\xa0', ' ')
nbViews = stats[1].find("b").text.replace('\xa0', ' ')
startDate = stats[2].text.replace('\xa0', ' ')

# Save data in a file with the current date
record = open("log.txt", "a")
date = ct() #current time
record.write(channelName+","+nbSubs+","+nbViews+","+date+"\n")

print( channelName + "\t" + nbSubs + " abonnés \t" + nbViews + " vues")
