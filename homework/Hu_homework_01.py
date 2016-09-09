# Title: Homework 2
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

print("The type of the 'data' is")
print(type(data))

print("The keys in the 'data' dictionary are ", data["response"].keys, "\n") # check what are in the data

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

while keep_going == True:
	print(page_num) # double check if going through each page
	content = "obamacare" # content to search
	dateStart = "20160101" # starting date
	dateEnd = "20161231" #ending date

	apiKey = "951312b93d9e42d8b16c699a130fa5ef"

	url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=" + content + "&page=" + str(page_num) +"&begin_date=" + dateStart + "&end_date=" + dateEnd + "&api-key=" + apiKey

	if len(data["response"]["docs"]) == 0: # when there is no docs
		keep_going = False
	else:
		page_num += 1
		start_doc = 0
		end_doc = data["response"]["meta"]["offset"] - 1

		response = requests.get(url)
		
		data = response.json() 
		
		for doc_num in range(start_doc, end_doc):
			# Create the variables
			pub_date = data["response"]["docs"][doc_num]["pub_date"]
			if len(pub_date) == 0: pub_date == "NA"  # in case of the missing data

			headline = data["response"]["docs"][doc_num]["headline"]["main"]
			if len(headline) == 0: headline == "NA"

			if doc_num == 2:
				print(data["response"]["docs"][doc_num]["byline"])

			byline = data["response"]["docs"][doc_num]["byline"]["original"]
			if len(byline) == 0: byline == "NA"

			lead_paragraph = data["response"]["docs"][doc_num]["lead_paragraph"]
			if len(lead_paragraph) == 0: lead_paragraph == "NA"

			# Write the data into the csv file
			row = [pub_date, headline, byline, lead_paragraph]
			with open("./results.csv", "a") as my_csv: # “a” means append
				data_writer = csv.writer(my_csv).writerow(row)

