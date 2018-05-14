#!/usr/bin/env python3
import psycopg2

#Write three functions, one for each question, and a fourth that calls them in order

#top_three_articles
def top_three_articles(c):
    c.execute("SELECT * FROM top_articles")
    response = c.fetchall();
    print "The 3 most viewed articles are:"
    for row in response:
        print row[0] + " --- " + str(row[1]) + " views."

#authors_in_order
def authors_in_order(db):
    #content goes here

#lots_o_failures
def high_failure_rate(db):
    #content goes here

def print_report():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = open("create-views.sql").read()
    c.execute(query)
    top_three_articles(c)
    #authors_in_order
    #lots_o_failures
    db.close()

print_report()
