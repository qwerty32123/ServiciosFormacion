import requests

# define the endpoint URL
url = 'http://localhost:5000/sudoku/solve'
headers = {'Content-Type': 'text/plain'}

# define the Sudoku data to insert
data = '708100495040560008095080000003601507109800364580004910000006270002700009950200643'

# send a POST request to create a new Sudoku
response = requests.post(url, data=data,headers=headers)

# print the response status code and content
print('Status code:', response.status_code)
print('Response content:', response.content)
