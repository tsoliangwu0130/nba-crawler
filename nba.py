import json
import requests
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-d', dest='date', help='Games date')

option, _ = parser.parse_args()
date = option.date

res = requests.get('https://data.nba.net/prod/v2/{}/scoreboard.json'.format(date))
html_doc = res.text

json_object = json.loads(html_doc)

for game in json_object['games']:
    host = game['hTeam']
    vistor = game['vTeam']
    print('{} - {} : {} - {}'.format(
        host['triCode'],
        host['score'],
        vistor['triCode'],
        vistor['score'])
    )
