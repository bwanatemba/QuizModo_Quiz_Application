

# QuizModo Quiz Application

This project is an interactive quiz application built using Python (Flask), HTML, and CSS. The application features user authentication, quiz scoring, result storage, and responsive design. Additionally, it includes an admin interface for adding new quiz questions and exposes a REST API for quiz questions and results.

## Features

- User Authentication (Sign up, Login, Logout)
- Multiple Choice Quiz
- Quiz Scoring and Result Storage
- Responsive Design
- Admin Interface for Adding Questions
- REST API for Quiz Questions and Results

## Project Structure

```
quizmodo/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── index.html
│   │   ├── quiz.html
│   │   ├── result.html
│   │   ├── admin.html
│   │   ├── add_question.html
│   ├── static/
│   ├── api.py
│   ├── main.py
│   ├── admin.py
├── migrations/
├── tests/
├── config.py
├── requirements.txt
└── run.py
```

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/quizmodo.git
   cd quizmodo
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the application**

   Update the configuration in `config.py` as needed.

5. **Initialize the database**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the application**

   ```bash
   flask run
   ```

7. **Access the application**

   Open your browser and go to `http://127.0.0.1:5000/`.

## Usage Guidelines

1. **User Authentication**

   - Sign up for a new account at `/signup`.
   - Login with your account at `/login`.
   - Logout using the `/logout` link.

2. **Taking the Quiz**

   - Access the quiz at `/quiz`.
   - Answer the questions and submit the quiz.
   - View your results at `/result`.

3. **Admin Interface**

   - Access the admin panel at `/admin` (ensure you are logged in).
   - Add new quiz questions via the admin interface.

4. **REST API**

   - Get all quiz questions at `/api/questions`.
   - Get all quiz results at `/api/results`.

## Overview of Project Architecture

- **Flask App Factory Pattern**: The application follows the Flask app factory pattern to create an instance of the app.
- **Blueprints**: The application is organized into blueprints for modularity:
  - `auth.py` handles user authentication.
  - `main.py` handles the main quiz functionality.
  - `admin.py` handles the admin interface.
  - `api.py` handles the REST API endpoints.
- **Templates**: HTML templates for different pages are stored in the `templates` directory.
- **Static Files**: Static files (CSS, JS) are stored in the `static` directory.
- **Models**: Database models are defined in `models.py`.
- **Forms**: WTForms are used for form handling in `forms.py`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

## Contributors
1. Edgar Temba	([X](https://x.com/bwanatemba), [LinkedIn](https://www.linkedin.com/in/bwanatemba/))

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
