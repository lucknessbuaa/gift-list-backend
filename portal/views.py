from django.shortcuts import render
from django.http import JsonResponse

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getConfig(request):
    fileId = request.GET.get('id')
    configPath = os.path.join(BASE_DIR, 'json/config.json')
    config = json.load(open(configPath))
    name = config[fileId];
    if name:
        return JsonResponse({
            'id': name 
        })
    else:
        return JsonResponse({
            '': ''  
        })

def getData(request):
    id = request.GET.get('id')
    fileName = id + '.json'
    filePath = os.path.join(BASE_DIR, 'json/%s' % fileName);
    data = json.load(open(filePath))
    return JsonResponse({
        'data': data     
    })

