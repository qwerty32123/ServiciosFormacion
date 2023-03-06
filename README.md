Microservicio Solver de Sudoku
Este es un microservicio sencillo basado en Flask que resuelve, agrega y devuelve Sudokus. También permite a los usuarios crear, recuperar y obtener una lista de sudokus de una base de datos SQLite.

Requisitos
Python 3.6+
Flask 2.0.1+
SQLite 3.28+
Instalación
Clone el repositorio en su máquina local.
Cree un entorno virtual y actívelo.
Instale las dependencias usando pip: pip install -r requirements.txt.
Cree la base de datos SQLite ejecutando el punto final createDB.
Inicie el servidor ejecutando python app.py.

EndPoints
GET /
Devuelve un mensaje JSON sencillo para confirmar que el microservicio está en funcionamiento.

GET /createDB
Crea la base de datos SQLite que se utilizará para almacenar sudokus.

POST /sudoku/solve
Acepta un objeto JSON con un tablero de sudoku y devuelve un objeto JSON con la solución, si existe alguna.

POST /sudokus
Acepta un objeto JSON con un nombre y una cuadrícula de sudoku, y la almacena en la base de datos SQLite.

GET /sudokus/<int:sudoku_id>
Recupera el sudoku con el ID especificado de la base de datos SQLite y devuelve un objeto JSON con su nombre y cuadrícula.

GET /sudokus
Recupera todos los sudokus de la base de datos SQLite y devuelve un objeto JSON con una lista de sus IDs, nombres y cuadrículas.
