# 
# Example file for parsing and processing JSON
#
from turtle import title
import urllib.request
import json 
import ssl

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  print("Title : ", theJSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
  count = theJSON["metadata"]["count"]
  print("Earthquakes recorded : ", str(count), "events")
  
  # for each event, print the place where it occurred
  for i in theJSON["features"]:
    print(i["properties"]["place"])
  print("--------------------------\n")

  # print the events that only have a magnitude greater than 4
  for i in theJSON["features"]:
    if i["properties"]["mag"] >= 4.0:
      print("%2.1f" % i["properties"]["mag"], "mag,", i["properties"]["place"])
  print("--------------------------\n")

  # print only the events where at least 1 person reported feeling something
  print("Felt reported\n")
  for i in theJSON["features"]:
    feltReports = i["properties"]["felt"]
    if feltReports != None:
      print("%2.1f" % i["properties"]["mag"], "mag,", i["properties"]["place"], "Reported :", str(feltReports), "times")


  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  context = ssl._create_unverified_context()
  webUrl = urllib.request.urlopen(urlData, context=context)
  print ("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
  else:
    print("Error, can't parse URL results")

if __name__ == "__main__":
  main()
