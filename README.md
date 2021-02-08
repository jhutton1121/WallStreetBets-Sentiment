# WallStreetBets-Sentiment

The purpose of this code is to allow you the user to connect to Reddit's API via the Python Reddit API Wrapper, praw. It scrapes comments from the subreddit of your choice over up to the last x amount of posts, sorted by hot. It then creates a graph of the top 10 most mentioned comments, color coded to their sentiment, which is determined using vaderSentiment.

https://github.com/cjhutto/vaderSentiment
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.



TO RUN THE CODE:
To begin, you need a reddit dev account. You will need to enter the relevant login information for your account entered into the WSBscraper module.

You'll need all three modules downloaded as well as any libraries used. To run the code, use WSBprocedure.py. On line 7, you can choose to scrape comments from the last x amount of posts in whatever subreddit you choose. The limit is 1000. 

Try it out on different subreddits and compare the resulting graphs.

There's a lot of stuff done like scraping positions that isn't being used, this is more of a blueprint for future updates. 
