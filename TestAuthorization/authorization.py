import os
import requests

# définition de l'adresse de l'API
api_address = 'api'
# port de l'API
api_port = 8000

users = [
      ('alice', 'wonderland', [200, 200]),
      ('bob', 'builder', [200, 403])
]


for username, password, expected_codes in users:
  for i, version in enumerate(['v1', 'v2']):
# requête
      r = requests.get(
        url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version=version),
      params= {
          'username': username,
          'password': password,
          'sentence': 'test'
    }
)

      status_code = r.status_code
      expected = expected_codes[i]

      if status_code == expected:
         test_status = "SUCESS"
      else:
         test_status = "FAILED"


      output = '''
============================
    Authorization test
============================

request done at "/{version}/sentiment"
| username="{username}"
| password="{password}"

expected result = {expected}
actual result = {status_code}

==>  {test_status}

'''.format(
           version=version,
           username=username,
           password=password,
           expected=expected,
           status_code=status_code,
           test_status=test_status
)
      print(output)
      if os.environ.get('LOG') == '1':
            with open('/logs/api_test.log', 'a') as file:
                file.write(output)

