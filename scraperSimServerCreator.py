# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Camron
#
# Created:     10/09/2014
# Copyright:   (c) Camron 2014
# Licence:     <your licence>
#
# The purpose of this script is to take the information scraped from the mirc
# site
# and add it to a simserver. this code is tailored to the format provided by
# the mirc
# spider coded using scrapy.
# -------------------------------------------------------------------------------
import json
import os
import sys
from lxml import etree as ET
from gensim import utils
from gensim import corpora
from simserver import SessionServer

documents = []


def main():
    json_data = open('./items.json')
    data = json.load(json_data)
    print 'starting'
    for i in range(0, len(data)-1):
        print i
        s = ""
        identifier = ""
        title = ""
        totalText = ""
        try:
            s = data[i]['identifier']
            identifier = s[0][18:].replace("%3A", "")
            summary = data[i]['desc'][0].strip()
            title = data[i]['title'][0].strip()
            totalText += summary
            totalText += " "
            totalText += title
            totalText += " "
            totalText += identifier
        except:
            print "error"
        documentPayload = ({'identifier':identifier, 'title': title, 'summary' : summary})
        documents.append({'text' : totalText, 'payload' : documentPayload})
    corpus =[{'id': text['payload']['identifier'], 'tokens' : utils.simple_preprocess(text['text']), 'payload' : text['payload']} for num, text in enumerate(documents)]
    service = SessionServer('./thesite/simdatabase')
    service.train(corpus, method='lsi')
    service.index(corpus)
    service.commit()


if __name__ == '__main__':
    main()
