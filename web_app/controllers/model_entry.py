import web_app.models as datastore
import ustream_api
class DataEntryHelper:
#class to help in Data Entry Helper
	def save_stream_details_to_model(self,url,emergency_contact=0,location_description=" "):
		#Method to enter stream details to model by using Ustream URL 
		#param: Ustream URL
		#return: True if the URL is sucessfully added. False otherwise
		api_object = ustream_api.UstreamAPI()
		stream_details = api_object.get_stream_details_by_url(url)
		if(stream_details == None):
			return False
		ustream_uid = self.none_to_na_macro(stream_details['id'])
		title = self.none_to_na_macro(stream_details['title'])
		url = self.none_to_na_macro(stream_details['url'])
		#is_protected = stream_details['is_protected']
		description = self.none_to_na_macro(stream_details['description'])
		status = self.none_to_na_macro(stream_details['status'])
		image_url = self.none_to_na_macro(stream_details['imageUrl'])
		#print ustream_uid+" "+title+" "+url+" "+description+" "+image_url+" "+ status
		# A total of 7 entries must be present
		entry = datastore.UstreamListing()
		entry.ustream_uid = ustream_uid
		entry.description = description
		entry.status = status
		entry.image_url = image_url
		entry.location_description = self.none_to_na_macro(location_description)
		entry.url = url
		entry.emergency_contact = self.none_to_na_macro(emergency_contact)
		entry.title = title
		entry.save()
		return True

	def none_to_na_macro(self,s):
		#Macro to help with null variables returned from network
		if(s==None):
			return "N/A"
		else:
			return s