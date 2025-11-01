
# Here gonna count the request each service handle after being load balanced 
# or load distributed
import requests
from tqdm import tqdm
import matplotlib.pyplot as plt

max_requests=10000


count={}

# gonna make API request

for _ in tqdm(range(max_requests)):
    res=requests.get("http://127.0.0.1:8000/")

    host_name=res.json()["hostname"]

    if count.get(host_name):
        count[host_name]=count[host_name]+1
    else:
        count[host_name]=1

print(count)

# Bar chart
plt.bar(count.keys(), count.values())
plt.xlabel("Container Hostname")
plt.ylabel("Number of Requests")
plt.title("Load Balancing Request Distribution")
plt.show()

# almost equally distributed
# {'0e526d71457f': 332, '1fa129aab9fa': 334, 'f601aba4acdf': 334}

