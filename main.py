import requests
from pprint import pprint
import json

auth_token="e0ef9683503f396f145e872c730d79eb" #YOUR_AUTH_TOKEN
org_id="694212024" #YOUR_ORGANISATION_ID

params="sortBy=-createdTime&limit=15"

headers={
    "Authorization":auth_token,
    "orgId":org_id,
    "contentType": "application/json; charset=utf-8"
}

request=requests.get('https://desk.zoho.com/api/v1/tickets?' + params, headers=headers)

if request.status_code == 200:
    tickets =  json.loads(request.content.decode('utf-8'))
    for ticket in tickets.get('data'):
        print(ticket.get('subject'))
        print(ticket.get('createdTime'))
        print('Status - ' + ticket.get('status'))
        if ticket.get('closedTime') == None:
            pass
        else:
            print('Closed at - ' + ticket.get('closedTime'))
            
        print('------------------')
else:
    pprint("Request not successful,Response code ",request.status_code," \nResponse : ",request.content)