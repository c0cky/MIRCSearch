from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
import json
from gensim import utils
from Assemble import Assemble
from simserver import SessionServer
from forms import SearchForm
import logging

# Create your views here.

def index(request):
    form = SearchForm()
    return render(request, 'mirc/main.html', {'form':form})

def noresults(request):
    form = SearchForm()
    return render(request, 'mirc/main.html', {'form':form, 'error_message':"No results please search again."})

def ajax(request):
    service = SessionServer('/Users/godboutc/Desktop/thesite/simdatabase')
    data = json.loads(request.body)
    print "DATA: \n"
    print data
    results = service.find_similar(data['identifier'], max_results=13)
    print results
    screen = []
    temp = []
    address = ""
    beggining = '/static/mirc/Thumbnails/'
    jpg = '.jpg'
    for i in range(0, len(results)):
        temp = results[i][2]
        address = beggining + results[i][0] + jpg
        temp['imgAdr'] = address
        screen.append(temp)
    a = Assemble(screen, data['width'], data['height'])
    a.do_the_work()
    finished = a.to_list()
    print "AJAX \n"
    print json.dumps(finished)
    return HttpResponse(json.dumps(finished), content_type = "application/json")

def rearrange(request):
    data = json.loads(request.body)
    theinfo = data['data']
    a = Assemble(theinfo, data['width'], data['height'])
    a.do_the_work()
    finished = a.to_list()
    return HttpResponse(json.dumps(finished), content_type = "application/json")

def search(request):
    #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
    service = SessionServer('/Users/godboutc/Desktop/thesite/simdatabase')
    form = SearchForm(request.POST)
    if form.is_valid() == False:
        return HttpResponse()
    search = form.cleaned_data['search']
    height = int(request.POST['height'])
    width = int(request.POST['width'])
    print height, " x ", width
    if form.is_valid():
        doc = {'tokens': utils.simple_preprocess(search)}
        print doc
        data = service.find_similar(doc, max_results=13)
        test = len(data)
        if test == 0:
            return HttpResponseRedirect('/mirc/noresults')
#run data through the circle thingy to get the positions in there.
	screen = []
    temp = []
    address = ""
    beggining = '/static/mirc/Thumbnails/'
    jpg = '.jpg'
    #p = '/home/cocky/thesite/mirc/static/mirc/Thumbnails/'
    for i in range(0, len(data)):
        temp = data[i][2]
        address =  beggining + data[i][0] + jpg
        #address = 'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg'
        temp['imgAdr'] = address
        screen.append(temp)
    a = Assemble(screen, width, height)
    a.do_the_work()
    finished = a.to_list()
    print finished
    form = SearchForm()
    return render(request, 'mirc/dashboard.html',{'data':json.dumps(finished),'form':form})
