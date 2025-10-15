from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'name': "Sherlok Holmes",
        'pages': 200
    },
    {
        'id': 2,
        'name': "Código Da Vinci",
        'pages': 300
    },
    {
        'id': 3,
        'name': "De Arquimedes a Einstein",
        'pages': 260
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_books_id(id):
    for book in books:
        if book.get('id') == id:
            break
    return jsonify(book)

@app.route('/books/<int:id>', methods=['PUT'])
def edit_books_id(id):
    edited_book = request.get_json()

    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(edited_book)
            break
    return jsonify(books[index])

@app.route('/books', methods=['POST'])
def add_books():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)

app.run(port=5000, host='localhost', debug=True)
