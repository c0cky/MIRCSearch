def main():
    from Assemble import Assemble
    lst = [{'did':'doc_0','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_1','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_2','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_3','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_4','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_5','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_6','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_7','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_8','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_9','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_10','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_11','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_12','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_13','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' },
    {'did':'doc_14','munge': 'mungeyy', 'title': 'titleee', 'summary' : 'summaryy', 'imgAdr':'http://www.extremetech.com/wp-content/uploads/2013/08/bitcoin1.jpg' }]
    a = Assemble(lst, 1000)
    a.do_the_work()
    finished = a.to_list()
    for i in range(0, len(finished)):
        print 'x'
        print finished[i]['x_axis']
        print 'y'
        print finished[i]['y_axis']

if __name__ == '__main__':
    main()
