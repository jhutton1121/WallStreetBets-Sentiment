import praw
import pandas as pd
import datetime as dt

def get_data(posts, subreddit):
    start = dt.datetime.now()
    print("Starting scrape: {}".format(start))
    secret = '' #developer key

    app_id = '' #developer id

    user = '' #username

    pw = '' #password

    reddit = praw.Reddit(client_id = app_id,
                         client_secret = secret ,
                         username = user,
                         password = pw,
                         user_agent= 'wsb bot'
                         ) #creates instance of reddit using the above authenticatos

    sub = reddit.subreddit(subreddit) #select subreddit

    new_wsb = sub.hot(limit = posts) #sorts by new and pulls the last 1000 posts of r/wsb

    commentlist =[]
    titlelist =[]
    for submission in new_wsb:
        titlelist.append(submission.title)   #creates list of post subjects, elements strings

        submission.comments.replace_more(limit=1)
        for comment in submission.comments.list():
            commentlist.append([str(comment.body), dt.datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S')]) #creates list of comments, elements strings

    finish = dt.datetime.now()
    print("Scrape completed at {}".format(finish))
    print("Scraping {} comments took {}".format(len(commentlist),finish - start))


    return commentlist
