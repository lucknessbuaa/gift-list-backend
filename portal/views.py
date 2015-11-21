from django.shortcuts import render
from django.http import JsonResponse

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getArticle(request):
    articlePath = os.path.join(BASE_DIR, 'json/article.json')
    article = json.load(open(articlePath))
    return JsonResponse({
        'data': article    
    })

def getOverview(request):
    overviewPath = os.path.join(BASE_DIR, 'json/overview.json')
    overview = json.load(open(overviewPath))
    return JsonResponse({
        'data': overview    
    })

def getRank(request):
    rankPath = os.path.join(BASE_DIR, 'json/rank.json')
    rank = json.load(open(rankPath))
    return JsonResponse({
        'data': rank    
    })

def getPartners(request):
    partnersPath = os.path.join(BASE_DIR, 'json/partners.json')
    partners = json.load(open(partnersPath))
    return JsonResponse({
        'data': partners    
    })

def getCover(request):
    coverPath = os.path.join(BASE_DIR, 'json/cover.json')
    cover = json.load(open(coverPath))
    return JsonResponse({
        'data': cover    
    })

def getShare(request):
    sharePath = os.path.join(BASE_DIR, 'json/share.json')
    share = json.load(open(sharePath))
    return JsonResponse({
        'data': share    
    })
