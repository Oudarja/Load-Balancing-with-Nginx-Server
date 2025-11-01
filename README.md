# Load-Balancing-with-Nginx-Server
This repo demonstartes how ngnix server can be used as a load balancer and how client request can be balanced by  distributing incoming client requests across multiple backend servers.

## Working
### Multiple FastAPI Containers
- Three instances of a FastAPI app (app1, app2, app3) run inside separate Docker containers.
- Each container runs Uvicorn on port 8000 internally.

### Nginx as a Load Balancer
- Nginx is configured to balance incoming requests across the three containers.
- Nginx communicates with containers using Docker service names (app1, app2, app3) and container port 8000.
- Host ports (like 8001, 8002, 8003) are mapped for external access if needed, but Nginx uses internal ports for load balancing.

```
upstream app {
    server app1:8000;
    server app2:8000;
    server app3:8000;
}

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://app;
    }
}
```
### Docker Compose
- Manages all containers together: FastAPI apps and Nginx.


### Testing Load Balancing

- A Python script (test_load.py) sends 10000 requests to Nginx (http://127.0.0.1:8000/).
- Each FastAPI container returns its hostname.
- The script counts how many requests each container handles:
```
{'0e526d71457f': 3334, '1fa129aab9fa': 3333, 'f601aba4acdf': 3333}
```
Requests are almost equally distributed, showing load balancing is working.

<img width="500" height="450" alt="distribution" src="https://github.com/user-attachments/assets/eda98043-b33e-4cf1-add2-537ac1ae2540" />

## How to Run Locally


### 1. Python version

```bash
 3.9.13
```

### 2. Clone the Repository

```bash
git clone "https://github.com/Oudarja/Load-Balancing-with-Nginx-Server.git"
```

### 3. Set Up a Virtual Environment

```bash
python -m venv .venv
myenv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```
### Build and start all containers:
```
docker compose up --build
```

### Check Nginx logs to see requests being forwarded:
```
docker logs nginx
```

### Test load distribution (optional):
```
python test.py
```
