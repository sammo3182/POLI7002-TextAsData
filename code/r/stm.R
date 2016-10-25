library(stm)

#read data
speech_results<-read.csv("./code/r/speech_results.csv",as.is=TRUE)

#process text
processed<-textProcessor(documents=speech_results$text,metadata=speech_results)
meta<-processed$meta
vocab<-processed$vocab
docs<-processed$documents
out <- prepDocuments(docs,vocab,meta)

#k = 3
docs<-out$documents
vocab<-out$vocab
meta <-out$meta
mod3 <- stm(docs, vocab, 3, prevalence=~s(days) + s(dw1), data=meta, max.em.its=10, init.type="LDA")
mod3a <- stm(docs, vocab, 3, data=meta, max.em.its=10, init.type="LDA")

#k = 4
mod4 <- stm(docs, vocab, 4, prevalence=~s(days) + s(dw1), data=meta, max.em.its=10, init.type="LDA")
mod4a <- stm(docs, vocab, 4, data=meta, max.em.its=10, init.type="LDA")

# check out topics
#k = 3
#labels
labelTopics(mod3)
mod3$theta # proportion of the topics for each document.
colMeans(mod3$theta)

labelTopics(mod3a)

#clouds
cloud(mod3)
cloud(mod3a)

#thoughs
thoughts <- findThoughts(mod3,text=speech_results$text,topics=1,n=5)
thoughts$index # show the document index

#k = 4
#labels
labelTopics(mod4)
labelTopics(mod4a)

#clouds
cloud(mod4)
cloud(mod4a)

#thoughs
findThoughts(mod4,text=speech_results$text,topics=1,n=5)

# evaluate fit
topicQuality(mod3,documents=docs)
topicQuality(mod3a,documents=docs)

topicQuality(mod4,documents=docs)

# heldout 
heldout <- make.heldout(out$documents, out$vocab)
documents <- heldout$documents
vocab <- heldout$vocab
meta <- out$meta

stm1<- stm(documents, vocab, 3, prevalence=~s(days)+s(dw1), init.type="Random", data=meta,max.em.its=5)
stm2<- stm(documents, vocab, 4, prevalence=~s(days)+s(dw1), init.type="Random", data=meta,max.em.its=5)
eval.heldout(stm1, heldout$missing)
eval.heldout(stm2, heldout$missing)

#estimate effect
prep <- estimateEffect(1 ~s(dw1), mod3, meta = out$meta, uncertainty = "Global")
plot.estimateEffect(prep, "dw1", method = "continuous", topics = 1, model = z, printlegend = F, xlab = "Ideology")

prep <- estimateEffect(c(1,3) ~s(dw1), mod3, meta = out$meta, uncertainty = "Global")
plot.estimateEffect(prep, "dw1", method = "continuous", topics = c(1,3), model = z, printlegend = F, xlab = "Ideology")
