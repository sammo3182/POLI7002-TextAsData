# Title: Homework2_Hillary
# Author: Yue Hu
# Environment: Win 10, Python 3.5
# Purpose: The assignment is a project using the New York Time API to scrape text data.

## module preload
import requests # imported the `requests` package for request url later.
import csv # for saving the results into csv files.

# ## Data scriping
# content = "Hilary" # content to search
# dateStart = "20160101" # starting date
# dateEnd = "20161231" #ending date

# apiKey = "951312b93d9e42d8b16c699a130fa5ef"

# url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=" + content + "&page=1&begin_date=" + dateStart + "&end_date=" + dateEnd + "&api-key=" + apiKey

# print("The URL is ", url, "\n") # check the url output
# # http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=obamacare&page=1&begin_date=20160101&end_date=20161231&api-key=951312b93d9e42d8b16c699a130fa5ef

# response = requests.get(url)
# data = response.json() 

# doc_num = 1
# print("Dictionary keys are ", data["response"]["docs"][doc_num].keys())
# ## Draw specific info from the data

# # print(data["response"]["docs"][1])
# # print(data["response"]["docs"][doc_num]["keywords"][0])
# # print("The wordcount of the article ", doc_num,": ", data["response"]["docs"][doc_num]["wordcount"])



## Save the results


keep_going = True # set the trigger when the while loop ends.
page_num = 1 # start scrapping from the first page
doc_total = 10 # found from the previous checks


def keywordScan(lim):
	n = 0
	kw_list = []
	while n < lim:
		word = data["response"]["docs"][doc_num]["keywords"][n]["value"]
		kw_list.append(word)
		n += 1
	return kw_list

while keep_going == True:
	print(page_num) # double check if going through each page
	content = "Hillary" # content to search
	dateStart = "20160101" # starting date
	dateEnd = "20160131" #ending date

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
			else: headline = headline.encode("utf-8", "ignore")

			if isinstance(data["response"]["docs"][doc_num]["byline"], dict): 
				byline = data["response"]["docs"][doc_num]["byline"]["original"].encode("utf-8")
                # When the byline is empty, it may return an empty list rather than a dictonary, and there could return an error.
			if len(byline) == 0: byline == "NA"
			

			lead_paragraph = data["response"]["docs"][doc_num]["lead_paragraph"]
			if lead_paragraph == None or len(lead_paragraph) == 0: lead_paragraph == "NA"
			else: lead_paragraph = lead_paragraph.encode("utf-8", "ignore")

			word_count = data["response"]["docs"][doc_num]["word_count"]
			if word_count == None or len(word_count) == 0:
				word_count == "NA"

			key_len = len(data["response"]["docs"][doc_num]["keywords"])
			if key_len == 0:
				keywords = "NA"
			elif key_len == 1:
				keywords = data["response"]["docs"][doc_num]["keywords"][0]["value"]
			else:
				keywords = keywordScan(2)

			# Write the data into the csv file
			row = [pub_date, headline, byline, lead_paragraph, word_count, keywords]
			# for x in row:
			# 	if isinstance(x, str):
			# 		x = x.encode("utf-8", "ignore")
			with open("./clinton.csv", "a") as my_csv: # “a” means append
				data_writer = csv.writer(my_csv).writerow(row)

