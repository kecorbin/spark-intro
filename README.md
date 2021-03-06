# Introduction to using Spark API with python

Some basic examples of consuming the Cisco Spark API using python.  This repo
is designed to demonstrate some basic usage of the following:

* Python Strings
* Python Lists
* Python Dictionaries

* Python requests module (GET/POST)
* Python JSON module


## Prerequisites

* Python 2.7
* Virtualenv
* pip
* requests


## Installation

```
git clone https://github.com/kecorbin/spark-intro
cd spark-intro
virtualenv venv
source venv/bin/activate
pip install -r requirements.text
```


## Setup

You will need a Spark account, you can sign up for free at https://ciscospark.com

You will also need your spark token, which you can find by visiting https://developer.ciscospark.com and clicking your avatar in the upper right hand corner of the screen

Once you have this information, you will need to modify the following lines in (./spark-intro.py)

```
# Set your spark token here
SPARK_TOKEN = "CHANGEME"

# Change this to be the room name as it appears in your spark client
SPARK_ROOM_NAME = "Demo Spark Room"
```


## Running the sample script

```
python spark-intro.py
```
