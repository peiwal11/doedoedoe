#!/bin/sh
sleep 5

#specify a kong service of nginx
curl -i -X POST http://kong:8001/service/ \
	--data name=nginx-service \
	--data url=http://ngi:80

#create a route to this nginx service, Every get request route to nginx
curl -i -X POST http://kong:8001/service/nginx-service/routes \
	--data 'methods[]=GET'
