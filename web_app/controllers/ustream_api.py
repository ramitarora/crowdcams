# import the library for making Rest API calls
import urllib2
# import the logging library
import logging
import string

# Get an instance of a logger
logger = logging.getLogger(__name__)

class UstreamAPI:
	#class to handle all UStream requests
	
	def __init__(self):
	#initializing variables for use in UStream calls
		self.api_key = '8039C02A34E21EF13AD946E516A643EF'
		self.format = 'xml'
		self.base_url = "http://api.ustream.tv/"
		
	def execute(self,request):
		#central method for executing all UStream calls
		url = self.base_url+self.format + request + "?key="+self.api_key
		logger.info("Execute "+url)
		#debug here after every new function 
		call = urllib2.urlopen(url)
		return call.read()
		
	def search_by_title(self,title):
		request = "/channel/recent/search/title:like:"+title
		logger.info("Search By Title URL: "+request)
		return self.execute(request)
		
	def getinfo_by_uid(self,uid):
		request = "/channel/"+uid+"/getInfo"
		logger.info("Get info by Ustream UID: "+uid)
		return self.execute(request)
	
	def get_embed_tag_by_urltitle(self,urltitle):
		request = "/channel/"+urltitle+"/getEmbedTag"
		logger.info("Getting Embed Tags for UrlTitle: "+urltitle)
		return self.execute(request)
	
	def get_embed_tag_by_url(self,url):
		splitted = string.split(url,"/")
		return self.get_embed_tag_by_urltitle(splitted[-1])

#Debugging		
#x = UstreamAPI()
#print x.get_embed_tag_by_url("http://www.ustream.tv/channel/test-channed")