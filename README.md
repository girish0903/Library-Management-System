# Library Management System API

This is a simple REST API for a Library Management System built using Flask. It allows you to perform CRUD (Create, Read, Update, Delete) operations for books and members, as well as search functionality and pagination.

## Features

- **CRUD Operations** for Books:
  - Create a new book
  - Get a list of all books
  - Update a book's information
  - Delete a book
- **CRUD Operations** for Members:
  - Create a new member
  - Get a list of all members
  - Update member details
  - Delete a member
- **Search Functionality**:
  - Search books by title or author
- **Pagination**:
  - Retrieve books with pagination support, specifying the page and number of books per page.

## Requirements

- Python 3.8 or later
- Flask 2.3.0

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

## Step 2: Set up a Virtual Environment

A virtual environment helps you manage dependencies specific to your project. Follow the steps below to set up a virtual environment:

### For Windows:

1. Open your command prompt (CMD) or PowerShell.
2. Navigate to the directory where you cloned the repository.

   ```bash
   cd path/to/library-management-system
   python -m venv venv
   ```

## Step 3: Install Dependencies

1. Now that the virtual environment is active, you need to install the project dependencies. Run the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Step 5: Run the Application

1. After installing the dependencies, you can start the Flask application by running:
   ```bash
   python app.py
   ```
2. You can open your browser and access the API at http://127.0.0.1:5000/.

## Step 6: Running Tests

1. If you'd like to run the tests for the API, you can use the following command to run all the unit tests:
   ```bash
   python -m unittest discover tests
   ```
2. This will discover and run all the test cases located in the tests directory
