This project involves combining KONG, Nginx and Python servers within Docker containers.

Use the build.sh script in the ngi directory to build the Nginx image. Don't forget to use chmod +x build.sh to make sure build.sh is executable.

Use the build.sh script in the py directory to build the Python server image. Also, remember to make the script executable by revising it accordingly.

Finally, run the docker-compose.yml file in the py directory to start both services at once.

Components Involved
1.	Kong API Gateway: Listens on VM ports (e.g., 8000 for HTTP and 8443 for HTTPS) to route requests to backend services.
2.	Nginx: Acts as a reverse proxy to the Python application and listens on container ports 80 (HTTP) and 443 (HTTPS), mapped to the host.
3.	Python Application: Serves content or APIs, accessible through Nginx.

   
Workflow Breakdown
1.	Client Request to Kong:
 - The client sends a request to http://localhost:8000.
 - Kong listens on the VM's port 8000 for HTTP requests (and 8443 for HTTPS if configured).
2.	Kong Routes Request to Nginx:
 - Kong is configured to route incoming requests to the Nginx service.
 - In kongconfig.yml, you specify that requests to http://localhost:8000 should be routed to http://HOST_IP:80 (where HOST_IP is the IP address of the VM).
3.	Nginx Receives and Processes Request:
 - Nginx, listening on container port 80, receives the request from Kong.
 - Nginx acts as a reverse proxy and forwards the request to the Python application.
4.	Python Application Handles Request:
 - The Python application, running behind Nginx, processes the request and sends the response back through Nginx.
 - Nginx forwards the response to Kong, which in turn sends it back to the client.



