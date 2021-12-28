# Woohoo!

This django application illustrates some of the failure modes described by the presentation. 

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
All the action happens here: `/woohoo/notaduck/views.py`

### /notaduck/ 
`curl -X POST localhost:8000/notaduck/?vara=1&varb=1 -d '{"foo":123,"q":123}'`
The base URL loads two query parameters, and two json body attributes and then applies various casts and math operations, it outputs the results (and types) so that you can get a feel for how NaN and INFs are handled. 

### /notaduck/rate

Rate allows users to submit a rating for a book, users can only submit one review per title. Rate keeps track of each book's average rating and displays the name of the highest rated book. Here an attacker can submit a malicious rating for books they do not like, causing their average to be effectively zero.

### /notaduck/blindbids

Allows users to submit bids for a blind auction. Upon request of `GET /notaduck/whowon` the results of the auction will be tallied using sorting mechanism. An attacker can submit malicious bids that interfere with the sorting and cause their own low bid to win, dispite higher bids being in the system.

### /notaduck/bid

Another bidding case, however in this case the mechanism only allows the attacker to achieve being selected the winner, their bid will be nan.
