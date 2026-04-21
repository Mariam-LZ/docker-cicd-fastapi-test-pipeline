import os
import requests

# définition de l'adresse de l'API
api_address = 'api'
# port de l'API
api_port = 8000

tests = [
      ('alice', 'wonderland', 200), 
      ('bob', 'builder', 200),
      ('clementine', 'mandarine', 403)
]


for username, password, expected in tests:
# requête
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params={
           'username': username,
           'password': password
    }
)

    status_code = r.status_code
   
    if status_code == expected:
       test_status = "SUCCESS"
    else:
       test_status = "FAILED"


    output = '''
============================
    Authentication test
============================

request done at "/permissions"
| username="{username}"
| password="{password}"

expected result = {expected}
actual restult = {status_code}

==>  {test_status}

'''.format(
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
