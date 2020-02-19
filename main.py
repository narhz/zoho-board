import requests
from pprint import pprint
import json
from dhooks import Webhook
import pickle

# account was deleted, auth token is not active
auth_token="e0ef9683503f396f145e872c730d79eb"
# org id is vaild though, do whatever you want with that i guess
org_id="694212024"

AGENTS = {
    '419932000000128292': 'Seth',
    '419932000001637008': 'Alex',
    '419932000000155091': 'Michelle'
}

params="sortBy=-createdTime&limit=15"

headers={
    "Authorization":auth_token,
    "orgId":org_id,
    "contentType": "application/json; charset=utf-8"
}



request = requests.get('https://desk.zoho.com/api/v1/tickets?' + params, headers=headers)

if request.status_code == 200:
    tickets =  json.loads(request.content.decode('utf-8'))
    for ticket in tickets.get('data'):
        status = ticket.get('status')
        number = ticket.get('ticketNumber')
        create_time = ticket.get('createdTime')
        close_time = ticket.get('closedTime')
        subject = ticket.get('subject')
        agent = ticket.get('assigneeId')
        ticket_id = ticket.get('id')

        print('| #' + number + ' - ' + subject)
        print('| Created at - ' + create_time)
        print('| Status - ' + status)

        if agent:
            print('| Assigned to - ' + AGENTS.get(agent, 'Unknown Agent'))
        else:
            print('| Unassigned')

        if close_time:
            print('| Closed at - ' + close_time)

        print('---------------------------------')
else:
    pprint("Request not successful. Response code ", request.status_code, " \nResponse : ", request.content)
