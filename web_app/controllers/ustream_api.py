# import the library for making Rest API calls
import urllib2
# import the logging library
import logging
import string
import json
import re

# Get an instance of a logger
logger = logging.getLogger(__name__)

#A general function to check if a string is a number or not
def is_number(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

class UstreamAPI:
	#class to handle all UStream requests
	
	def __init__(self):
	#initializing variables for use in UStream calls
		self.api_key = '8039C02A34E21EF13AD946E516A643EF'
		self.format = 'json'
		self.base_url = "http://api.ustream.tv/"
		
	def execute(self,request):
		#param: Formatted request string
		#return: Raw API result string
		#central method for executing all UStream calls
		url = self.base_url+self.format + request + "?key="+self.api_key
		logger.info("Execute "+url)
		#debug here after every new function 
		call = urllib2.urlopen(url)
		return call.read()
		
	def search_by_title(self,title):
		#param: Ustream channel title
		#return: Raw API result string
		request = "/channel/recent/search/title:like:"+title
		logger.info("Search By Title URL: "+request)
		return self.execute(request)
		
	def getinfo_by_uid(self,uid):
		#param: Ustream UID
		#return: Raw API result string
		request = "/channel/"+uid+"/getInfo"
		logger.info("Get info by Ustream UID: "+uid)
		return self.execute(request)
	
	def get_embed_tag_by_urltitle(self,urltitle):
		#param: Ustream url-title
		#return: Raw API result string
		request = "/channel/"+urltitle+"/getEmbedTag"
		logger.info("Getting Embed Tags for UrlTitle: "+urltitle)
		return self.execute(request)
	
	def get_embed_tag_by_url(self,url):
		#param: Ustream url
		#return: Raw API result string
		splitted = string.split(url,"/")
		return self.get_embed_tag_by_urltitle(splitted[-1])
	
	def get_uid_from_url(self,url):
		#param: Ustream url
		#return: UID(String)
		#Ustream returns results, msg, processTime, error, version. We are interested in msg, error and results
		data = json.loads(self.get_embed_tag_by_url(url))
		results = data['results']
		msg = data['msg']
		error = data['error']
		if(error == None ):
			#Using regular expression to extract the UID from "&cid=**" present in the Embed URL
			m = re.match(r".*(cid)=(\d+).*", results)
			return m.group(2)
		else:
			return "Message Returned:"+msg +" Error returned:"+error
	
	def get_stream_details_by_url(self,url):
		#param: Ustream url
		#return: dict() struture containing Stream details like name, title, etc. if present, else Me
		uid = self.get_uid_from_url(url)
		if(is_number(uid)):
			data = json.loads(self.getinfo_by_uid(uid))
			results = data['results']
			msg = data['msg']
			error = data['error']
			#Todo: Some bugs here related to None and results- fixit.
			#Todo: Remove embed-tag for faster performance 
			if(results == None ):
				#Using regular expression to extract the UID from "&cid=**" present in the Embed URL
				return {'Message' : msg,'Error':error}
			else:
				return results
			
#Debugging		
#x = UstreamAPI()
#print x.get_stream_details_by_url("http://www.ustream.tv/channel/test-channed")