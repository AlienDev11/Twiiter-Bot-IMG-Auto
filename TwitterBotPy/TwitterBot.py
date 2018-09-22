import tweepy
import ImageCheck
import os
#import DetectChanges


#credentials
Consumer_Key = ""
Consumer_Secret_Key = ""
Access_Token = ""
Access_Token_Secret = ""

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret_Key)
auth.set_access_token(Access_Token,Access_Token_Secret)
Jack = tweepy.API(auth)

def Initiate():
    ImageCheck.FileCreate()
    ImageCheck.ImageCh()
    print("Woohoo Start")

def ReRun():
    ImageCheck.ImageCh()

if __name__ == "__main__":
    Initiate()
