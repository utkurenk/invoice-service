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

## Usage

Please refer to "api/swagger/swagger.json" for the API documentation.Note that the documentation was made with swagger 2.0. If you don't have access to Swagger UI, read below for a quick summary of HTTP requests and endpoints.

* GET /api/invoices - get list of invoices
* GET /api/invoices/<invoice_id> - get single invoice
* POST /api/invoices/add - create an invoice 
* PUT /api/invoices/update/<invoice_id> - update an invoice
* DEL /api/invoices/delete/<invoice_id> - delete an invoice

