import googlemaps
import pandas as pd
import requests 
import json
import random

flag = 0
city = input("Please enter the city: ")
from youtube_easy_api.easy_wrapper import *
easy_wrapper = YoutubeEasyWrapper()
easy_wrapper.initialize(api_key="AIzaSyCPKbGLynwXuvaAKhLnd53sFMrjhktUMrs")
video_results = easy_wrapper.search_videos(search_keyword=city+"美食",
                                     order='relevance')
print("===================================================================================")
print("video:\n")
for i in range(len(video_results)):
    print(i+1)
    print("TITLE:",easy_wrapper.get_metadata(video_id=video_results[i]['video_id'])['title'])
    print("URL:","https://www.youtube.com/watch?v="+video_results[i]['video_id']+'\n')
print("===================================================================================")

gmaps = googlemaps.Client(key = "AIzaSyBK0Dwtk5ccOb97Wa9tCMrgggjDJF_ZuXM")
geocode_result = gmaps.geocode(city)
location = geocode_result[0]['geometry']['location']
key_word = input("What you want to eat today? ") 
print("\n")
query_result = gmaps.places_nearby(keyword=key_word,location=location, radius=3000)
restaurant_list = []
placeid_list = []
def restaurant(query_result,placeid_list,restaurant_list):
    for i,t in enumerate(query_result['results'],start=1):
        print(i)
        print("Restaurant:",t['name'])
        placeid_list.append(t['place_id'])
        restaurant_list.append(t['name'])
        print("Address:",t['vicinity'])
        print("Rating:",t['rating'],'\n')
        
def comment(placeid_list):
    placeid = placeid_list[int(comment_num)-1]
    print(placeid)
    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid='+placeid+'&key=AIzaSyBK0Dwtk5ccOb97Wa9tCMrgggjDJF_ZuXM'
    text = requests.get(url).text
    soup = json.loads(text)
    for i,s in enumerate(soup['result']['reviews'],start=1):    
        print(i)
        print("username:",s['author_name'])
        print("time:",s['relative_time_description'])
        print("rating:",s['rating'])
        print("comment:",s['text'],"\n")

while(1):
    if flag == 0:
        restaurant(query_result,placeid_list,restaurant_list)
        print("==============================Enter Q to quit==============================")
        comment_num = input("View the comments: ")
        print("\n")
        if comment_num == 'Q':
            break
        else:
            comment(placeid_list)
        flag = 1
    if flag == 1:
        print("=========================Enter Q to quit or Enter B to back=========================")
        comment_num = input("Input: ")
        print("\n")
        if comment_num == 'Q':
            break
        elif comment_num == 'B':
            flag = 0
        else:
            flag = 1
        
    


numlist = []
print("=========================Enter Q to quit=========================")

while(1):
    num = input("Which one? ")
    if num == "Q":
        break
    numlist.append(num)
ran = int(random.choice(numlist))
print("===================================================================================")        
print("\n今晚 我想來點..."+restaurant_list[ran-1])


   
   