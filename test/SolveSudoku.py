import requests

# define the endpoint URL
url = 'http://localhost:5000/sudoku/solve'
headers = {'Content-Type': 'text/plain'}

# define the Sudoku data to insert
data = '530070000600195000098000060800060003400803001700020006060000280000419005000080079'

# send a POST request to create a new Sudoku
response = requests.post(url, data=data,headers=headers)

# print the response status code and content
print('Status code:', response.status_code)
print('Response content:', response.content)
