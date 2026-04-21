import os
import requests

# définition de l'adresse de l'API
api_address = 'api'
# port de l'API
api_port = 8000

sentences = [
      ('life is beautiful', 1),
      ('that sucks', -1)
]


for sentence, expected_sign in sentences:
 for version in ['v1', 'v2']:
# requête
    r = requests.get(
        url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version=version),
        params= {
           'username': 'alice',
           'password': 'wonderland',
           'sentence' : sentence
    }
)

    score = r.json().get('score', 0)
    if (score > 0 and expected_sign == 1) or  (score < 0 and expected_sign == -1):
      test_status = "SUCCESS"
    else:
      test_status = "FAILED"


    output = '''
============================
    Content test
============================

request done at "/{version}/sentiment"
| sentence = '{sentence}'

expected sentiment = {expected}
actual score = {score}

==>  {test_status}

'''.format(
           version=version,
           sentence=sentence,
           expected='positive' if  expected_sign == 1 else 'negative',
           score=score,
           test_status=test_status
)

    if os.environ.get('LOG') == '1':  
            with open('/logs/api_test.log', 'a') as file:  
                file.write(output)
