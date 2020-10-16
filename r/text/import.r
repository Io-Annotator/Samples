library(httr)
library(jsonlite)

# get your API key https://app.ioannotator.com/api
query = list(apikey = "add your API key here")
text <- list(dataset = "add your dataset ID here", text = "the text you want to annotate")

res <- POST("https://api.ioannotator.com/import/texts", query = query, body = text, encode = "json", verbose())

