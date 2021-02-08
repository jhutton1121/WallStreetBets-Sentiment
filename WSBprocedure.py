import plotly.express as px
import pandas as pd
from WSBobjects import create_tickers
import re
from WSBreader import get_data

#Get the comments by calling the get_data function from the WSBreader module
commentlist = get_data(100, "wallstreetbets") #adjust this number to pull different amounts of posts, limit 1000
commentlist.sort(key = lambda x:x[1]) #Sort it by time

#The following code block searches through each comment for '$' and then whatever letters come after. This is understood to be a ticker, due to popular notation.
#Once it finds it, it takes away the $ and appends it to a master tickerlist.
#The master tickerlist is then used to search through each comment for any tickers it picked up. Over a large enough amount of data, this is very accurate for picking up the most talked about stocks.
tickerlist = []
for i in commentlist:
    tickers = re.findall(r'\$[a-zA-Z]+\b', str(i[0])) 
    if len(tickers) > 0:
        for j in tickers:
            clean_tick = str(j[1:])
            tickerlist.append(clean_tick.upper())
        
tickerlist = set(tickerlist) #removes duplicates

final_list = create_tickers(tickerlist,commentlist) #Logs on, scrapes comments, creates ticker objects


graph_list = []
#creates a nested list that has elements like [GME, 32, .5] for graphing
for obj in final_list:
    graph_list.append([obj.ticker,obj.count,obj.avg_sent])
    



df = pd.DataFrame(graph_list, columns = ['Ticker', 'Count', 'Avg_Sentiment']) #creates a dataframe from the graph_list
df = df.sort_values(by = 'Count', ascending = False)#Sorts it by count
df = df.head(10) #Gives us the top 10 rows

fig = px.bar(df, x = df.Ticker, y = df.Count, color = df.Avg_Sentiment) #creates bar graph

fig.update_layout(
    title={
        'text': "Top 10 Most Mentioned Stocks on r/wallstreetbets and their Sentiment",
        'x' : .5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.show() #initiates graph

