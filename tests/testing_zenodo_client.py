import requests

data = {

}

access_token = 'lI4TUf18GUMCmJYyfNtnrvsHHrrgjox8pHYCCCfkL6H462MaPv8WumHYm1YH'
headers = {"Content-Type": "application/json"}
data = {
     'metadata': {
         'title': 'My first upload',
         'upload_type': 'poster',
         'description': 'This is my first upload',
         'creators': [{'name': 'Probst, Matthias',
                       'affiliation': 'KIT ITS'}]
     }
 }

# if False:
r = requests.post(
    'https://sandbox.zenodo.org/api/deposit/depositions',
    json=data,
    params={"access_token": access_token},
    headers=headers
)
print(r.status_code)
# 201
print(r.json())

bucket_url = r.json()["links"]["bucket"]

path = "test_zenodo_search.py"
with open(path, "rb") as fp:
    r = requests.put(
        "%s/%s" % (bucket_url, path),
        data=fp,
        params={"access_token": access_token},
    )
r.json()

print(r.json())




# # Define the metadata that will be used on initial upload
# data = Metadata(
#     title='Test Upload 3',
#     upload_type='dataset',
#     description='test description',
#     creators=[
#         Creator(
#             name='Probst, Matthias',
#             affiliation='My python school',
#             orcid='0000-0001-8729-0482',
#             gnd='123456789',
#         ),
#     ],
# )
# print(data)
# # res = ensure_zenodo(
# #     key='test3',  # this is a unique key you pick that will be used to store
# #     # the numeric deposition ID on your local system's cache
# #     data=data,
# #     paths=[
# #         'test_zenodo_search.py',
# #     ],
# #     sandbox=True,  # remove this when you're ready to upload to real Zenodo
# # )
# # from pprint import pprint
# #
# # pprint(res.json())
