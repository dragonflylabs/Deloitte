from django.http import JsonResponse
from django.shortcuts import render
import requests
from requests_ntlm import HttpNtlmAuth


def news(request):
    SITE = "http://deloitte.lennken.com/_api/web/lists/getbytitle('New')/items"
    PASSWORD = "Lennken123$"
    USERNAME = "http://deloitte.lennken.com\\sp.admin"
    headers = {'accept': 'application/json;odata=verbose'}
    response = requests.get(SITE, auth=HttpNtlmAuth(USERNAME,PASSWORD), headers=headers)
    return JsonResponse(dict(response.json()))
