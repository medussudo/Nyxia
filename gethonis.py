import codecs
import requests
from random import randint

class Gethonis():
	token: str
	auth = False
	data: dict
	model: str
	stream: bool
	base_url: str
	def __init__(self, token, model, stream, base_url):
		test = {"token": token}
		self.base_url = base_url
		rs = requests.post(f"{base_url}/api/authorisation", json=test)
		resp = rs.json()
		print(resp['Status'])
		if resp['Status'] == "Positive":
			self.auth = True
		else: 
			self.auth = False

		if self.auth == True:
			self.token = token
			self.stream = stream
			self.data = {
				"headers": token,
				"messages": [
					{"role": "system", "content": "You are a helpful assistant"}
            	],
            	"stream": stream
			}
			self.model = model


	def get_message(self, message):
		self.data["messages"].append({"role": "user", "content": message})
		if self.stream:
			self.data["messages"].append({"role": "user", "content": message})
			decoder = codecs.getincrementaldecoder('utf-8')()
			response = requests.post(f"{self.base_url}/api/{self.model}", json=self.data, stream=True)
			return response
		response = requests.post(f"{self.base_url}/api/{self.model}", json=self.data)
		rs = response.json()
		return rs[0]
		
		
		      