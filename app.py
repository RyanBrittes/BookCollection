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

app.run(port=5000, host='localhost', debug=True)
