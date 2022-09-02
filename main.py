import requests

response = requests.get('https://new.yapo.cl/inmuebles/departamento-irarrazaval-2d--2b_84425298')
print(response.text)
