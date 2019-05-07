Weiti
===========

## Description
Weiti is a web app made for managing a single queue at supermarkets or events. <br/>
It speeds up the check-out process in order to improve customer service.

## Installation
Install the requirements:
`pip install -r requirements.txt` <br/>
Get the server running:
`python manage.py runserver` <br/>
Install redis in a Docker container and set the published ip:port to 32768: 
`sudo docker run --name my-redis-container -d redis` <br/>
