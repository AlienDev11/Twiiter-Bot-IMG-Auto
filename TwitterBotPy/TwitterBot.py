import tweepy
import ImageCheck
import os
#import DetectChanges


#credentials
Consumer_Key = "n2l1YpgOPyid44v12geMJuqbA"
Consumer_Secret_Key = "zoCDmjgie3sfGwfupOslnOt12uVF7rvvHaZURJJXYnhNFRYjTm"
Access_Token = "1043379803724730368-ZbwcYva0VZtk2gYnPUSLl5R3OyD0ar"
Access_Token_Secret = "kZpsrOzpHBTOTB5ZnGg2rlAnv3rVjLWJ4PQ8v4dx6U5ka"

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
