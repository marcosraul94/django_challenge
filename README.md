# Musical Works project
Simple `django` project challenge with `works_single_view` app.

## Requirements
Only `docker` is needed.

## Running the app
Just run `docker-compose up` and  it  will start the django app 
and run any migrations inside the postgres container.

## Test endpoint
For hitting the django backend use `127.0.0.1:3000/musical-work/<iswc>`.

## Running tests
In order to execute the tests you would need to be inside the django container
`docker-compose exec api sh`. Once there do `python manage.py test` to run the test
suits.

## Questions

#### Describe briefly the matching and reconciling method chosen.
Matching is performed on `iswc` or `title` and compared by 
individual `contributors` then reconciliation merges the two
musical works by filling missing `iswc` and joining the 
`contributors` without duplicates.

#### We constantly receive metadata from our providers, how would you automatize the process?
I would add an endpoint where we reuse the same logic from the data ingestion migration so
clients can dynamically send new metadata.

#### Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?
The queries for fetching and updating the musical works with newer data would run
slower. 

#### If not, what would you do to improve it?
We can add `indexes` to the `iswc` and `title` fields to compensate this.
We can also add a cache so we don't hit the db that hard.



