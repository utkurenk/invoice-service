# invoice-service

## installation

to deploy the application run following commands

```
docker pull holyhumerus/invoice-service

docker run -p 5000:5000 holyhumerus/invoice-service
```

## installation by building docker image

to build the docker image and run the docker container, run the following commands

```
git clone https://github.com/utkurenk/invoice-service.git

docker build . -t invoice-service

docker run -p 5000:5000 invoice-service
```

