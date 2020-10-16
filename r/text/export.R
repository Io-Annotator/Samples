library(httr)
library(rlist)
library(jsonlite)

# get your API key https://app.ioannotator.com/api
query = list(apikey = "add your API key here", dataset="add your dataset ID here")

res <- GET("https://api.ioannotator.com/export", query = query, verbose())
http_type(res)
jsonRespText<-content(res,as="text") 
fromJSON(jsonRespText)

