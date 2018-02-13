import json
import requests


res = requests.get('http://fcast.us-west-2.espncdn.com/FastcastService/pubsub/profiles/12000/topic/event-topevents/message/5118057/checkpoint')
data = json.loads(res.text)
basketball = data['sports'][0]

for league in basketball['leagues']:
    for event in league['events']:
        competitors = [{}, {}]
        for index, competitor in enumerate(event['competitors']):
            competitors[index]['name'] = competitor['name']
            competitors[index]['score'] = competitor['score']
        print('{} - {}: {} - {}'.format(
            competitors[0]['name'], competitors[0]['score'],
            competitors[1]['name'], competitors[1]['score']))
