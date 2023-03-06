import os

from flask import Flask, jsonify, request
import sqlite3

import Solver

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'mensaje': 'Bienvenido a el microservicio de sudokus'})

@app.route('/createDB')
def createDB():
    #  comprobamos si la BBDD existe
    if os.path.isfile('sudoku.db'):
        return jsonify({'mensaje': 'La base de datos ya existe!'})
    else:
        # creamos una conexion a la BBDD
        conn = sqlite3.connect('sudoku.db')

        c = conn.cursor()

        # creamos la tabla
        c.execute('''CREATE TABLE Sudokus
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  grid TEXT NOT NULL)''')

        # guardamos los cambios
        conn.commit()

        # cerramos la conexion
        c.close()
        conn.close()

        return jsonify({'message': 'La base de datos se ha creado!'})



@app.route('/sudoku/solve', methods=['POST'])
def solve_sudoku():
    board_str = request.get_data().decode('utf-8')["sudoku"]
    print(board_str)
    board = [[int(board_str[row*9+col]) for col in range(9)] for row in range(9)]
    solver = Solver.SudokuSolver(board)
    solution = solver.solve()
    if solution is not None:
        return jsonify({'solution': ''.join(str(num) for row in solution for num in row)})
    else:
        return jsonify({'error': 'No solution found'})



@app.route('/sudokus', methods=['POST'])
def create_sudoku():
    # datos que se pasan en el post
    data = request.get_json()

    # creamos al conexion a sudoku db
    conn = sqlite3.connect('sudoku.db')
    c = conn.cursor()

    # insertamos los datos del sudoku en la tabla de sudokus
    c.execute("INSERT INTO Sudokus (name, grid) VALUES (?, ?)", (data['name'], data['grid']))
    conn.commit()

    # cerramos la conexion
    c.close()
    conn.close()

    # return a JSON response with the new Sudoku ID
    return jsonify({'id': c.lastrowid})

@app.route('/sudokus/<int:sudoku_id>', methods=['GET'])
def get_sudoku(sudoku_id):
    # creamos la conexion a la BBDD
    conn = sqlite3.connect('sudoku.db')
    c = conn.cursor()

    # seleccionamos el sudoku
    c.execute("SELECT name, grid FROM Sudokus WHERE id = ?", (sudoku_id,))
    result = c.fetchone()

    # cerramos el cursos y la conexion
    c.close()
    conn.close()

    # devolvemos un json con la informacion del sudoku
    if result:
        return jsonify({'name': result[0], 'grid': result[1]})
    else:
        return jsonify({'message': 'Sudoku not found'}), 404


@app.route('/sudokus', methods=['GET'])
def get_all_sudokus():
    # creamos la conexion a la BBDD
    conn = sqlite3.connect('sudoku.db')
    c = conn.cursor()

    # seleccionamos todos los sudokus de la base de datos
    c.execute("SELECT id, name, grid FROM Sudokus")
    results = c.fetchall()

    # cerramos el cursos y la conexion
    c.close()
    conn.close()

    # devolvemos un json con todos los sudokus
    sudokus = []
    for result in results:
        sudokus.append({'id': result[0], 'name': result[1], 'grid': result[2]})
    return jsonify({'sudokus': sudokus})


