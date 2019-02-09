import tweepy 
import os
f=open('password/botkeys.txt','r')
passwords=f.read().split('\n')


def send_data(donor,description,quantity,module):
    message=donor + " has decided to donate " + module +"\nQuantity :  " + str(quantity) + "\nDescription : " + description  + "\n\nUse #helpinghands and be the part of the change in the world"; 
    consumer_key=str(passwords[0])
    consumer_secret=str(passwords[1])
    access_token=str(passwords[2])
    access_token_secret=str(passwords[3])
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(message)



send_data("DIT MESS","Leftover food of the mess ",20,"Food")