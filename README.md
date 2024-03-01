## Installation on Docker

This Dockerfile starts with a Python 3.7 base image, sets the working directory to /app, installs the necessary packages, exposes port 80 for the Flask application, and finally runs [`api.py`](vscode-file://vscode-app/c:/Users/jorge/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "api.py") when the container is started.

You can build the Docker image by running:

```
docker build -t pothole-cost-svc .
```

And then run the Docker container with:

```
docker run -p 5000:5000 my-python-app
```

This will start your Flask application inside a Docker container and it will be accessible at `localhost:4000` on your machine.


## Request Example

URL: http://127.0.0.1:5000/cost?area=44&&depth=10&&material=ASPHALT
```
GET /cost?area=44&&depth=10&&material=ASPHALT HTTP/1.1
Connection: keep-alive
Host: 127.0.0.1:5000
```

### Response Example 
```
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.9.18
Date: Fri, 01 Mar 2024 20:29:15 GMT
Content-Type: application/json
Content-Length: 26
Connection: close
{"price":6080.5068359375}
```
