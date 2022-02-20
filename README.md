# Graphite

### Project run
```vim
docker build -t web-image .back
docker-compose up 
```

### Project update
```vim
docker-compose up -d --build
docker-compose down
```

### Run script
```vim
docker-compose exec web {script} 
```

### Swarm
```vim
docker swarm init --advertise-addr 127.0.0.1:2377
docker stack deploy -c docker-compose.yml  proj
```  
### Remove swarm 
```vim
docker stack rm proj
docker swarm leave --force
```
