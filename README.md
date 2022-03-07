sudo docker build -t futimage .

sudo docker run -d --name fut -p 8010:5000 futimage:latest
