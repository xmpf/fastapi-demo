MongoDB:

```
$ docker run --name mongodb -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=password mongodb/mongodb-community-server:latest
```

Webserver:

```
$ pipenv run uvicorn --host 127.0.0.1 app.main:app --reload
```

Swagger API docs: http://localhost:8000/docs