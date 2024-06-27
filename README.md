This is a project of nginx and python server combination.
One could use ngi build.sh to build an nginx image, and don't forget to use chmod +x build.sh to make sure build.sh could be execute.
One then use build.sh in py dir to build an python server image, also don't forget to revise the it to be able to execute.
Finally one could run docker-compose.yml at , to run these two service all in once.
