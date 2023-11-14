
print("hallo wereld")
import logging
import datetime
import time
import requests
from sense_hat import SenseHat
import json
sense = SenseHat()

color = "black"
colornames = {}
colornames["red"] = (255,0,0)
colornames["green"] = (0,255,0)
colornames["blue"] = (0,0,255)
colornames["yellow"] = (255,255,0)
colornames["black"] = (0,0,0)
fsUrl = "https://services9.arcgis.com/7e6lF03RcLhwFtm5/arcgis/rest/services/Selected_Color/FeatureServer/0"
logFilepath = "/home/admin/Documents/logs/updatecolor_{}.log".format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

def main():
	logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s - %(message)s',datefmt='%Y%m%d-%H:%M:%S',handlers=[logging.StreamHandler(),logging.FileHandler(logFilepath)])
	logging.info("Start update color v20231110.01")
	r = 0
	g = 0
	b = 0
	for i in range(0,254):
		sense.clear((r,i,b))
		#time.sleep(0.01)
	
	logging.info("Startting script")
	sense.show_message("starting",0.05)
	
	sense.color.gain = 16
	sense.color.integration_cycles = 256
	counter = 0
	
	logging.info("Showing M")
	sense.show_letter("M")
	x = 0
	y = 0
	rvalue = 75
	gvalue = 75
	while True:
		try:
			sense.set_pixel(x,y,colornames[color])
			y +=1
			if y > 7:
				y = 0
				x+=1
			if x > 7:
				x = 0
				if CheckConnection():
					rvalue = 75
					gvalue = 150
				else:
					rvalue = 150
					gvalue = 75
			sense.set_pixel(x,y,(rvalue,gvalue,75))
			#print("waiting for input")
			for event in sense.stick.get_events():
				logging.info(f"stick event: {event.direction},{event.action}")
				direction = event.direction
				if event.action=="pressed":
					if direction =="middle":
						SentColor()
					if direction == "up":
						SaveColor("red")
					if direction == "right":
						SaveColor("green")
					if direction == "down":
						SaveColor("blue")
					if direction == "left":
						SaveColor("yellow")
			time.sleep(0.1)
		except:
			logging.exception("Error in main loop")
				
def SaveColor(colorname):
	global color
	if colorname==color:
		colorname= "black"
	logging.info(f"Setting color to: {colorname}")
	sense.clear(colornames[colorname])
	color = colorname
	
def SentColor():
	try:
		text = f"sending  {color}"
		logging.info(text)
		sense.show_message(text,0.07, text_colour=colornames[color])
		
		#query feature for its objectid
		queryParams = {"f":"json","where":"1=1","outFields":"*"}
		queryUrl = f"{fsUrl}/query"
		
		r = requests.get(queryUrl,queryParams)
		print(r.text)
		results = r.json()
		feature = results["features"][0]
		logging.info(feature)
		#updating feature
		feature["attributes"]["color"] = color
		feature["attributes"]["color_count"] = feature["attributes"]["color_count"] + 1
		updateParams = {"f":"json","features":json.dumps([feature])}
		updateUrl = f"{fsUrl}/updateFeatures"
		
		r = requests.post(updateUrl,updateParams)
		logging.info(r.text)
		results = r.json()
		
		#{"updateResults":[{"objectId":1,"uniqueId":1,"globalId":null,"success":true}]}
		text = f"results: {results['updateResults'][0]['success']}"

		sense.show_message(text, text_colour=colornames[color])
	except:
		logging.exception("Error in SentColor")
	
def CheckConnection():
	logging.info("Checking connection")
	retValue = False
	
	try:
		params = {}
		params["f"] = "json"
		params["where"]="1=1"
		params["returncountOnly"]=True
		queryUrl = f"{fsUrl}/query"
		logging.info(f"requesting {queryUrl}")
		r = requests.get(queryUrl,params)
		
		result = r.json()
		logging.debug(f"result: {result}")
		
		if "count" in result:
			retValue = True
	except:
		logging.exception("Error getting value")
	return retValue
				
if __name__=="__main__":
	main()
		
