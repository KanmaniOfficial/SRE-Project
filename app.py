from flask import Flask, render_template, request

app = Flask(__name__)

books = []
authors = []


@app.route('/')
def index():
    return render_template('index.html', books=books, authors=authors)


@app.route('/add_book', methods=['POST'])
def add_book():
    book_name = request.form['book_name']
    author_name = request.form['author_name']
    books.append(book_name)
    authors.append(author_name)
    return render_template('index.html', books=books, authors=authors)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
