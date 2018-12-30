from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def kappahttp(request):
    x = 'The request was: <h1>nothing?<h1/> hmm'
    return HttpResponse(x)


def about(request):
    return render(request,'about.html')


def count(request):
    entry = request.GET['fulltext']
    # print(entry)
    wordslist = entry.split()
    dic1 = {
    'entry':entry,
    'wordcount':len(wordslist)}

    wordic = {}

    for word in wordslist:
        # print(word)
        if word not in wordic:
            wordic[word] = 1
        else:
            wordic[word] += 1
        # wordic[word] += 1

    sorted_dic = sorted(wordic.items(), key=operator.itemgetter(1), reverse = True)
    # print(wordic)

    return render(request,'count.html',{'dic1':dic1,'sorted_dic':sorted_dic})
