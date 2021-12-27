# Ducktales - woohoo!

## Validation library by @RSNAKE
`./lib/nan_safety.py`

## Vulnerable Djanjo "API" 
`./woohoo`
Illustrates some of the failure modes described by the presentation, see the postman collections for how.


### Running

#### Docker
```
cd woohoo
docker build -t notaduck .
docker run -it -p 8000:8000 notaduck
```

#### Django
If you already have django installed you can do the typical
`python manage.py runserver`
