import math
import json
import requests
import itertools
import numpy as np
import pandas as pd
import time
from tqdm import trange,tqdm
from datetime import datetime, timedelta
import sys


if len(sys.argv) > 3:
    first_step = int(sys.argv[3])
else:
    first_step = 1

if len(sys.argv) > 2:
    max_crawls = int(sys.argv[2])
else:
    max_crawls = 40000
if sys.argv[1] == "remote":
    r = range(first_step,max_crawls)
elif sys.argv[1] == "local":
    r = trange(first_step,max_crawls)



uri = "https://api.pushshift.io/reddit/search/comment/?size=100&subreddit=europe&after={}h&before={}h"

#how many steps in the past, each step is of *hourly_step* hours
dataset_list = []
step = 60
hourly_step = 2
consec_errors = 0
last_was_error = False

for i in r:
    #get the url
    url = uri.format(hourly_step*(i+1), hourly_step*i)
    #get the data
    try:    
        raw_data = requests.get(url)
        data =raw_data.json()
        #save the data
        dataset_list.append(pd.DataFrame.from_dict(data["data"])[["body","author_flair_text","permalink","author","created_utc"]])
        if sys.argv[1] == "remote":
            print(f"{i}-th iteration")
        if i%step==0:
            f_num = int(i/step)
            if sys.argv[1] == "remote":
                print(f"Printing {f_num}-th File")
            elif sys.argv[1] == "local":
                tqdm.write(f"Printing {f_num}-th File")
            dataframe = pd.concat(dataset_list,ignore_index=True)
            filename = "{}.csv".format(f_num).zfill(12)
            dataframe.to_csv(f"data/{filename}")
            dataset_list = []
        time.sleep(0.6)
    except Exception as e:
        last_was_error = True
        if sys.argv[1] == "remote":
            print(f"####################################################")
            print(f"Error at {i}-th Iteration")
            print(f"####################################################")
            print(f"####################################################")
            print(f"####################################################")
            print(f"url of the error: {url}")
            print(f"####################################################")
            print(f"Type of error:\n{e}")
            print(f"####################################################")
            print(f"Raw Data:\n{raw_data}")
            print(f"####################################################")
            if consec_errors>=1000:
                print(f"Something is not working, bye...")
                raise RuntimeError('Failed to do anything') from exc
            else:
                if consec_errors>=100:
                    multiplier = consec_errors%4
                    print(f"Waiting for {60*multiplier} seconds and retrying...")
                    time.sleep(timer*multiplier)
                consec_errors+=1
        else:
            tqdm.write(f"####################################################")
            tqdm.write(f"Error at {i}-th Iteration")
            tqdm.write(f"####################################################")
            tqdm.write(f"####################################################")
            tqdm.write(f"####################################################")
            tqdm.write(f"url of the error: {url}")
            tqdm.write(f"####################################################")
            tqdm.write(f"Type of error:\n{e}")
            tqdm.write(f"####################################################")
            tqdm.write(f"Raw Data:\n{raw_data}")
            tqdm.write(f"####################################################")
            if consec_errors>=5:
                tqdm.write(f"Something is not working, bye...")
            else:
                if consec_errors>=100:
                    multiplier = consec_errors%4
                    tqdm.write(f"Waiting for {60*multiplier} seconds and retrying...")
                    time.sleep(timer*multiplier)
                consec_errors+=1
    else:
        consec_errors = 0

            

