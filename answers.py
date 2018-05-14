#!/usr/bin/env python3
import psycopg2
import create_views.sql

#Write three functions, one for each question, and a fourth that calls them in order

#top_three_articles
def top_three_articles(db):
    c = db.cursor()
    c.execute("SELECT * FROM top_articles")
    response = c.fetchall();
    print "The 3 most viewed articles are:"
    for row in response:
        print row[0] + " --- " + row[1] + " views."

#authors_in_order
def authors_in_order(db):

#lots_o_failures
def high_failure_rate(db):

def print_report():
    #open connection
    #create_views
    #top_three_articles
    #authors_in_order
    #lots_o_failures
    #close connection

print_report()
