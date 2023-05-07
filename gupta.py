import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn" 
headers = {"Authorization": "Bearer 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"} 
data= '''
The tower is 324 metres (1,063 ft) tall, about the same height as an  
81-storey building, and the tallest structure in Paris. Its base is  
square, measuring 125 metres (410 ft) on each side. During its 
construction, the Eiffel Tower surpassed the Washington Monument 
to become the tallest man-made structure in the world, a title it held 
for 41 years until the Chrysler Building in New York City was finished in 1930.'''

minL=20 
maxL=50
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs":data, 
    "parameter":{"min_length":minL, "max_length":maxL},
}) 
print(output) 