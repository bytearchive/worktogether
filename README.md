Worktogether - Simple daily team checkins
============================================================

* Get a mail at the endof the day asking what you did today
* Send a mail to worktogether with your response
* Get a mail next day with everyone's responses

Inspired by [idonethis.com](http://idonethis.com) and [Status Hero](https://statushero.com/)

Technical Details
====================

* Emails are parsed by sendgrid and https://github.com/agiliq/sendgrid-eventhooks
* Django app parses text from email

Data received in receiver function
=======================================

Data is received as a dictionary in kwargs which has two keys 'sender' and 'data'. The 'data' key has the dict of information from 'sendgrid-eventhooks'
The keys in 'data' dict are:
* Sender
* To
* Date
* Subject
* Body

Setup
=============

To setup and start using this project, follow the steps:
* Clone this repo to your local drive.
* Create a virtualenv.
* Install the requirements in requirments/local.txt.
* Setup database for the project.
* Fill the environment variables mentioned in .env file.
* Export the .env file `$ source .env`

Usage
==============
* There are two management commands `./manage.py ask_members` and `./manage.py send_digest`
* Create bash scripts to run the commands on terminal.
* Setup cron jobs to execute these scripts at the desired timings.

License
=======

MIT

Todo
=====================

* Setup front-end to allow members of organization to modify their updates and view all the progess at on place.
