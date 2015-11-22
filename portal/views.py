from django.shortcuts import render
from django.http import JsonResponse

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getConfig(request):
    versionName = request.GET.get('id')
    configPath = os.path.join(BASE_DIR, 'json/config.json')
    config = json.load(open(configPath))
    name = config[versionName];
    if name:
        fileName = '%s.json' % name
        filePath = os.path.join(BASE_DIR, 'json/%s' % fileName);
        data = json.load(open(filePath))
        return JsonResponse({
            'data': data
        })
    else:
        return JsonResponse({
            'data': {}    
        })
