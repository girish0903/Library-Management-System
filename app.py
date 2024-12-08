from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for books and members
books = []
members = []

# Counters for generating unique IDs
book_id_counter = 1
member_id_counter = 1

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Library Management System API!"})

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    data = request.get_json()
    new_book = {
        "id": book_id_counter,
        "title": data["title"],
        "author": data["author"],
        "year_published": data["year_published"]
    }
    books.append(new_book)
    book_id_counter += 1
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book.update(data)
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200

@app.route('/members', methods=['POST'])
def add_member():
    global member_id_counter
    data = request.get_json()
    new_member = {
        "id": member_id_counter,
        "name": data["name"],
        "email": data["email"],
        "membership_date": data["membership_date"]
    }
    members.append(new_member)
    member_id_counter += 1
    return jsonify(new_member), 201

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    for member in members:
        if member["id"] == member_id:
            member.update(data)
            return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    members = [member for member in members if member["id"] != member_id]
    return jsonify({"message": "Member deleted"}), 200

@app.route('/books/search', methods=['GET'])
def search_books():
    title = request.args.get('title')
    author = request.args.get('author')

    filtered_books = books
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book['title'].lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]

    return jsonify(filtered_books), 200

@app.route('/books/pagination', methods=['GET'])
def get_books_with_pagination():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    start = (page - 1) * per_page
    end = start + per_page

    return jsonify(books[start:end]), 200

if __name__ == '__main__':
    app.run(debug=True)
