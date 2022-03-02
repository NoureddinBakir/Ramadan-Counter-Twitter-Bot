import os
import tweepy
from datetime import timedelta, datetime
import Wallpaper
import math

# from apscheduler.schedulers.blocking import BlockingScheduler

# sched = BlockingScheduler()

# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=8)
# def scheduled_job():
#     print('This job is run every weekday at 8am.')

# sched.start()

# os.getenv('/.env')
# os holds all the keys
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']

# Place keys for api access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

d0 = datetime.now()
d1 = datetime(2022, 4, 2, 19, 31, 0)
delta = d1-d0
deltaN = int(str(delta.days))
moonsLeft = round((365 - deltaN)/365 *10)
moonsDone = round(10-moonsLeft)
percent =  (365-deltaN)/365 * 100
print("Percent:"+str(round(percent, 5)))
percent=math.floor(percent)
count = str( delta.days ) + " days left until #Ramadan! \n \n"+ "We are " + str(math.floor(percent)) + "% of the way there \n \n" + moonsLeft * "\U0001F315" + moonsDone * "\U0001F311"

quote = str( delta.days ) + " days left until Ramadan!"

# File writing code, ensuring we print only every few days
f = open("lastTime.txt", "r")
lastPercent = f.read(2)
f.close()
print(lastPercent)

if(percent > int(lastPercent)):
  f = open("lastTime.txt", "w")
  f.write(str(percent))
  f.close()
  try:
    Wallpaper.get_wallpaper(quote, round(percent))
    media = api.media_upload("created_image.png")
    api.update_status(count, media_ids=[media.media_id])
    print(count)
  except:
    print('Try again G')