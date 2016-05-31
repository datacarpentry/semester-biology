---
layout: page
title: Getting Data From The Web
---

Data on the web is increasingly available in ways that go beyond downloading csv files.

APIs
----

Often data is provided through an [Application programming interface](http://en.wikipedia.org/wiki/Application_programming_interface).
An API is just an agreed up language for two different software components to talk to one another.
On the web, using an API typically involves calling a specially structured URL,
and handling the data that is returned.

* XML
* JSON
* REST

eBird Examples
---------------

eBird is a real-time, online, checklist program that allows users to report their bird observations.
It is currently adding several million records per month.
This data can be queried using [eBird's API](https://confluence.cornell.edu/display/CLOISAPI/eBird+API+1.1).

Let's start by looking at the results of an API call in the browser.

### Recent observations near Logan, UT

To find recent observations near Logan, we use this specially formatted url the includes the latitude and longitude.

#### XML
[http://ebird.org/ws1.1/data/obs/geo/recent?lng=-111.83&lat=41.74](http://ebird.org/ws1.1/data/obs/geo/recent?lng=-111.83&lat=41.74)

#### JSON
[http://ebird.org/ws1.1/data/obs/geo/recent?lng=-111.83&lat=41.74&fmt=json](http://ebird.org/ws1.1/data/obs/geo/recent?lng=-111.83&lat=41.74&fmt=json)

### We can also access this data from Python

We could do this using ``urllib``, but there are better ways to do this.

#### XML

One of the best modules for dealing with XML (and HTML) is [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/).
It makes it easy to work with tagged data.

    from bs4 import BeautifulSoup
    import urllib

    url = "http://ebird.org/ws1.1/data/obs/geo/recent?lng=-111.83&lat=41.74"
    webpage = urllib.urlopen(url)
    webdata = BeautifulSoup(webpage)
    print webdata.prettify()

    for sighting in webdata.find_all('sighting'):
        print sighting.lat.text, sighting.lng.text, sighting.find('sci-name').text

This sort of approach will also work well for scraped HTML data.

#### JSON

The [requests module](http://docs.python-requests.org) makes dealing with web APIs incredibly easy.

    import requests

    url = "http://ebird.org/ws1.1/data/obs/geo/recent?lng=-111.83&lat=41.74&fmt=json"
    recent_observations = requests.get(url)
    recent_observations.json

Which then lets us do things like:

    for observation in recent_observations.json:
        print observation['sciName'], observation['howMany']

Wrapping APIs
-------------

We can make it easier to use APIs in a particular language by writing a series of functions
that build the proper URLs.
Often someone has already done this for us, so it's definitely worth looking around.
For example, here's a [Python eBird wrapper](https://github.com/carsonmcdonald/python-ebird-wrapper).
Then getting the data is as easy as importing a module.

    from EBird import EBird

    ebird = EBird()
    ebird.recent_notable_observations_geo(41.7, -111)
