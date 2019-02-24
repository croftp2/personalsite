#!/usr/bin/env python

#Paul Croft
#February 24, 2019

from bottle import get, run, static_file, template

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="css")

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="js")

@get("/")
def index_page():
    return template("templates/main.html")


def main():
    run(host="0.0.0.0", port=34251, server="eventlet")


if __name__ == "__main__":
    exit(main())
