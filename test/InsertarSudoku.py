import requests

# define the endpoint URL
url = 'http://localhost:5000/sudokus'

# define the Sudoku data to insert
data = {'name': 'Sudoku 1', 'grid': '530070000600195000098000060800060003400803001700020006060000280000419005000080079'}

# send a POST request to create a new Sudoku
response = requests.post(url, json=data)

# print the response status code and content
print('Status code:', response.status_code)
print('Response content:', response.content)

# define another Sudoku data to insert
data = {'name': 'Sudoku 2', 'grid': '004300209005009001070060043006002087190007400050083000600000105003508690042910300'}

# send another POST request to create a new Sudoku
response = requests.post(url, json=data)

# print the response status code and content
print('Status code:', response.status_code)
print('Response content:', response.content)