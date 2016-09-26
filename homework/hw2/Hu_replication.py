# Title: Homework2_Replication
# Author: Yue Hu
# Environment: Win 10, Python 3.5
# Purpose: The assignment is a project using the New York Time API to scrape text data.

## module preload
import requests # imported the `requests` package for request url later.
import csv # for saving the results into csv files.

## Data scriping
content = "obamacare" # content to search
dateStart = "20160101" # starting date
dateEnd = "20161231" #ending date

apiKey = "951312b93d9e42d8b16c699a130fa5ef"

url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=" + content + "&page=1&begin_date=" + dateStart + "&end_date=" + dateEnd + "&api-key=" + apiKey

print("The URL is ", url, "\n") # check the url output
# http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=obamacare&page=1&begin_date=20160101&end_date=20161231&api-key=951312b93d9e42d8b16c699a130fa5ef

response = requests.get(url)
data = response.json() 


## Data glimpse
print("The type of the data is ")
print(type(data))  # check the type of the data
# <class 'dict'>

print("\nThe keys in the 'data' dictionary are ", data.keys(), "\n") # check what are in the data

print("The type of the 'response' is")
print(type(data["response"]))

print("The keys in the 'response' dictionary are ", data["response"].keys, "\n") # check what are in the data

print(data["response"]["meta"]) # show what's in "meta".
# 'offset': 10, each time calls the API will return 10 articles. 
# 'hits': 430, there are 430 total articles 

print("The type of the 'response' is")
print(type(data["response"]["docs"]))

doc_num = 0
print("The type of the article ", doc_num, " is")
print(type(data["response"]["docs"][doc_num])) # check the type of the first document

print("The keys of the docs dictionary are ", data["response"]["docs"][doc_num].keys())

## Draw specific info from the data
#pub_date: data["response"]["docs"][doc_num]["pub_date"]
print("The date the article ", doc_num," is published: ", data["response"]["docs"][doc_num]["pub_date"])

#headline: data["response"]["docs"][doc_num]["headline"]["main"]
print("The headline of the article ", doc_num,": ", data["response"]["docs"][doc_num]["headline"]["main"])

#byline: data["response"]["docs"][doc_num]["byline"]["original"]
print("The byline of the article ", doc_num,": ", data["response"]["docs"][doc_num]["byline"]["original"])

#lead_paragraph: data["response"]["docs"][doc_num]["lead_paragraph"]
print("The lead paragraph of the article ", doc_num,": ", data["response"]["docs"][doc_num]["lead_paragraph"])


## Save the results


keep_going = True # set the trigger when the while loop ends.
page_num = 1 # start scrapping from the first page
doc_total = 10 # found from the previous checks

while keep_going == True:
	print(page_num) # double check if going through each page
	content = "obamacare" # content to search
	dateStart = "20160101" # starting date
	dateEnd = "20161231" #ending date

	apiKey = "951312b93d9e42d8b16c699a130fa5ef"

	url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=" + content + "&page=" + str(page_num) +"&begin_date=" + dateStart + "&end_date=" + dateEnd + "&api-key=" + apiKey
	
	response = requests.get(url)	
	data = response.json()

	if len(data["response"]["docs"]) == 0: # when there is no docs
		keep_going = False
	else:
		page_num += 1
		 # python excludes the last one in a range.

		doc_total = len(data["response"]["docs"])
		for doc_num in range(doc_total):
			print(doc_num, "/", doc_total) # to trace the progress
			# Create the variables
			pub_date = data["response"]["docs"][doc_num]["pub_date"]
			if len(pub_date) == 0: pub_date == "NA"  # in case of the missing data

			headline = data["response"]["docs"][doc_num]["headline"]["main"]
			if len(headline) == 0: headline == "NA"

			if isinstance(data["response"]["docs"][doc_num]["byline"], dict): 
				byline = data["response"]["docs"][doc_num]["byline"]["original"]
                # When the byline is empty, it may return an empty list rather than a dictonary, and there could return an error.
			if len(byline) == 0: byline == "NA"

			lead_paragraph = data["response"]["docs"][doc_num]["lead_paragraph"]
			if lead_paragraph == None or len(lead_paragraph) == 0: lead_paragraph == "NA"

			# Write the data into the csv file
			row = [pub_date, headline, byline, lead_paragraph]
			# for x in row:
			# 	if x != None:
			# 		x = x.encode("gbk", "ignore")
			with open("./results.csv", "a") as my_csv: # “a” means append
				data_writer = csv.writer(my_csv).writerow(row)

