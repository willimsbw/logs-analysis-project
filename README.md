# News site logs Analysis

This program utilizes the postgreSQL database "news" from a new website to answer questions about that site's traffic. It will tell you the 3 most-visited articles, show how many views the site's authors have across all of their articles, and the days where more than 1% of requests

## Getting Started

The first thing to do is download answers.py and create-views.sql. Then, on a machine with [PostgreSQL](https://www.postgresql.org/) installed, you can create a database called "news" containing the following tables, and fill those tables with records:

```
CREATE TABLE articles (
    author integer NOT NULL,
    title text NOT NULL,
    slug text NOT NULL,
    lead text,
    body text,
    "time" timestamp with time zone DEFAULT now(),
    id integer NOT NULL
);

CREATE TABLE authors (
    name text NOT NULL,
    bio text,
    id integer NOT NULL
);

CREATE TABLE log (
    path text,
    ip inet,
    method text,
    status text,
    "time" timestamp with time zone DEFAULT now(),
    id integer NOT NULL
);
```

At that point, make sure answers.py and create-views.sql are in the same directory, and execute one of the following commands (depending on your python configuration):

```
python answers.py

or

python3 answers.py
```

### Prerequisites

* Make sure you have [Python 3](https://docs.python.org/3/) installed
* Make sure you have [PostgreSQL](https://www.postgresql.org/) installed
* Make sure you have the [psycopg2 library](http://initd.org/psycopg/download/) installed

```
pip3 psycopg2
```

## Built With

* [Python 3](https://docs.python.org/3/)
* The [psycopg2 library](http://initd.org/psycopg/download/)
* [PostgreSQL](https://www.postgresql.org/)

## Authors

* **Bryan Williams** - *Initial work* - [willimsbw](https://github.com/willimsbw)
* Udacity's team, who provided a pre-configured Vagrant VM and the database's content

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Acknowledgments

* Thanks to Udacity for their nanodegree programs
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2), for providing this really great readme template
