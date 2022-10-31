# Thing

## About Thing
Thing is an open source API project to help people record all the thing in realworld or virtual space.

Thing provide robust API let people can:
- record
- update
- delete
and do all kind of operation they want easily and quickly.

## Documentation
- API: Under Developing
- Documentation: Under Developing
- [Design and the working note](https://hackmd.io/@LJsdk/things)

## Dev

### Initialize dev env

recommand using docker to dev
```
docker compose build
docker compose up
```

and in the docker sh
```
python manage.py runserver
```
And API will run at: http://127.0.0.1:8000/

### Tests
Unit tests
- To run unit tests
```
python -m pytest
```