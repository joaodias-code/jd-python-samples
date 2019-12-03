import json
import requests

def suspender_evento(event_code):
    
    url = 'https://api.eventosgofree.com'
    headers = {'access_token': ''}
    payload = {'id_evento': event_code}

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    if r.status_code == r.codes.ok:
        return True
    else:
        return False 
