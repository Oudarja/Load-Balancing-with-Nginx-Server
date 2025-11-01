from fastapi import FastAPI
import socket

app=FastAPI()

# No need to use async since there are no awaitable operations here
# To know which operation is awaitable, look for functions defined with 'async def'
# some example of awaitable operations are database calls, network requests, etc.
# and here we are using socket function which works synchronously
@app.get("/")
def read_root():
    # Get the hostname and IP address of the server
    hostname = socket.gethostname()
    # Get the IP address associated with the hostname
    ip_address = socket.gethostbyname(hostname)
    return {"message": "Hello, World!", "hostname": hostname, "ip_address": ip_address} 