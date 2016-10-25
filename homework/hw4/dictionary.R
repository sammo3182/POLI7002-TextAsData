#load library
library("rjson")
library("quanteda")

#set working directory
setwd("/Users/brycedietrich/Dropbox/text_class/homework/homework4/")

#read dictionary
liwc <- dictionary(file = "LIWC2007.txt",format = "LIWC")

#load lexis download
lexis<- fromJSON(file="lexis.json")

#convert to a vector
lexis_articles<-NULL
for(i in 1:length(lexis)){
  lexis_articles<-c(lexis_articles,lexis[[i]]$text)
}

#convert to corpus
lexis_corpus<-corpus(lexis_articles)

#word count...one way
lexis_wc<-rowSums(dfm(lexis_corpus))

#word count...another way
lexis_wc2<-NULL
for(i in 1:length(lexis)){
  lexis_wc2<-c(lexis_wc2,length(unlist(strsplit(lexis[[i]]$text," "))[unlist(strsplit(lexis[[i]]$text," "))!=""]))
}

#liwc
lexis_dfm<-dfm(lexis_corpus,dictionary=liwc,removeNumbers = TRUE, removePunct = TRUE, ignoredFeatures = stopwords("english"))
lexis_pos<-as.numeric(lexis_dfm[,24])
lexis_neg<-as.numeric(lexis_dfm[,25])

#boxplot
boxplot(data.frame(cbind("Positive"=lexis_pos/lexis_wc,"Negative"=lexis_neg/lexis_wc)))

#custom dictionary
my_dictionary <- list(spending=c("expensive", "cost", "deficit","spending"),
               spending2=c("expensive", "cost", "deficit","spend*"))

lexis_dfm2<-dfm(lexis_corpus,dictionary=my_dictionary,removeNumbers = TRUE, removePunct = TRUE, ignoredFeatures = stopwords("english"))
lexis_spend<-as.numeric(lexis_dfm2[,1])
lexis_spend2<-as.numeric(lexis_dfm2[,2])

#boxplot...spending
boxplot(data.frame(cbind("Spending1"=lexis_spend/lexis_wc,"Spending2"=lexis_spend2/lexis_wc)))
