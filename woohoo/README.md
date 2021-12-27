# Woohoo!

This application illustrates some of the failure modes described by the presentation. 

The postman collection provides additional runnable documentation. 

## Running

### Docker
```
cd woohoo
docker build -t notaduck .
docker run -it -p 8000:8000 notaduck
```

### Django
If you already have django installed you can do the typical
`python manage.py runserver`


## Examples

### `curl -X POST lcoalhost:8000/notaduck/?vara=1&varb=1 -d '{"foo":123,"q":123}'`
The base URL loads two query parameters, and two json body attributes and then applies various casts and math operations, it outputs the results (and types) so that you can get a feel for how NaN and INFs are handled.
