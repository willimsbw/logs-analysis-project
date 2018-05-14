#!/usr/bin/env python3
import psycopg2
from datetime import datetime

#Write three functions, one for each question, and a fourth that calls them in order

def get_results(c, query):
    c.execute(query)
    return c.fetchall()

#top_three_articles
def top_three_articles(c):
    response = get_results(c, "SELECT * FROM top_articles")
    print "\nThe 3 most viewed articles are:\n"
    for row in response:
        print "  * " + row[0] + " --- " + str(row[1]) + " views."

#authors_in_order
def authors_in_order(c):
    response = get_results(c, "SELECT * FROM authors_views")
    print "\n\nHere are all authors on the site, in order of whose articles have gotten the most views over time:\n"
    for row in response:
        print "  * " + row[0] + " --- " + str(row[1]) + " views."

#lots_o_failures
def high_failure_rate(c):
    response = get_results(c, "SELECT * FROM many_failures")
    print "\n\nThese are the dates where more than 1{} of requests to the server resulted in an error:\n".format("%")
    for row in response:
        new_format_date = row[1].strftime("%B %d, %Y")
        print "  * " + str(new_format_date) + " --- " + str(int(row[0] * 100)) + "{} errors\n".format("%")

def print_report():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = open("create-views.sql").read()
    c.execute(query)
    top_three_articles(c)
    authors_in_order(c)
    high_failure_rate(c)
    db.close()

print_report()
