# Text Summarization

A web application that allows users to summarize long texts using an AI model. Users can register, log in, and paste any text to get a concise summary using the T5 model from Hugging Face's Transformers library.

## Features

- User registration and login system using SQLite
- Text summarization using the T5-base model
- Clean and responsive frontend with HTML and CSS
- Flask-based backend with session handling
- Error handling and flash messaging

## Project Structure

```
project/
├── App.py                  # Main Flask application
├── Dashboard.html          # Dashboard for summarizing text
├── Index.html              # Landing page
├── login.html              # Login page
├── Signup.html             # Signup/Registration page
├── Style.css               # Shared styling for all HTML pages
└── users.db                # SQLite database (generated at runtime)
```

##  Technologies Used

- Python
- Flask
- SQLAlchemy (SQLite backend)
- Hugging Face Transformers (T5 model)
- HTML, CSS (Glassmorphism UI style)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone this repository or download the files.

2. Install the required dependencies:

   ```bash
   pip install flask transformers flask_sqlalchemy
   ```

3. Run the application:

   ```bash
   python App.py
   ```

4. Open a browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

## User Authentication

- Users can sign up and log in securely.
- Session-based login to access the dashboard.

## Text Summarization

- Powered by the `t5-base` model from Hugging Face.
- API endpoint `/summarize` accepts POST requests with a JSON body like:

```json
{
  "text": "Your long input text here..."
}
```

- Response contains:

```json
{
  "summary": "Generated concise summary."
}
```

