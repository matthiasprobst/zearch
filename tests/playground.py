import datetime

import json

import requests

from pprint import pprint

url = 'https://sandbox.zenodo.org/api/deposit/depositions/8170'
ACCESS_TOKEN = 'lI4TUf18GUMCmJYyfNtnrvsHHrrgjox8pHYCCCfkL6H462MaPv8WumHYm1YH'
r = requests.get(url,
                  params={'access_token': ACCESS_TOKEN})
r.status_code
# 200
r.json()
print(r.json())
bucket_url = r.json()["links"]["bucket"]

print(bucket_url)
# for rr in r.json():
#     pprint(rr)



# edit:
# r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/8170/actions/edit',
#                   params={'access_token': ACCESS_TOKEN})

# # new version:
# r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/8170/actions/newversion',
#                   params={'access_token': ACCESS_TOKEN})
data = {
     'metadata': {
         'title': 'My second upload',
         'upload_type': 'other',
         'version': 'v0.1.0',
         'description': 'This is my first upload. h5rdmoolbox==1.0.0',
         'creators': [{'name': 'Probst, Matthias',
                       'affiliation': 'Karlsruhe Institute of Technology',
                       'orcid': '1232-0001-8729-0482',
                       'gnd': None}],
         'publication_type': 'invalid',
         'publication_date': datetime.datetime.today().strftime("%Y-%m-%d"),

     }
 }

headers = {"Content-Type": "application/json"}
# change record:
r = requests.put(url,
    json=data,
    params={"access_token": ACCESS_TOKEN},
    headers=headers
)

print(r.status_code)


# publish:
if False:
    import requests
    r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/8170/actions/publish',
                      params={'access_token': ACCESS_TOKEN})
