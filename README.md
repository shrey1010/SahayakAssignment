
---

# Django Certificate Generator Project

## Overview

This Django project is a certificate generator with three levels of functionality. The levels are as follows:

### Level 1

- Implements a many-to-many relationship between students and teachers.
- Stores their data in respective tables.
- Allows users to select a teacher and view corresponding students, or select a student and view corresponding teachers.

### Level 2

- Allows users to choose a teacher-student pair and generate a certificate.
- The certificate includes a predefined text along with the names of the teacher and student.

### Level 3

- Implements JWT (JSON Web Tokens) for certificate verification.
- Generates a token upon certificate creation.
- Provides an endpoint to verify the certificate using the token.

## Completed Levels

I have successfully completed all three levels of the assignment.

## Getting Started

Follow these steps to set up and run the project locally:

1. **Clone the Repository**

    ```
    git clone https://github.com/shrey1010/SahayakAssignment.git
    cd django-certificate-generator
    ```

2. **Set Up Virtual Environment (Optional but recommended)**

    ```
    python3 -m venv env
    source env/bin/activate  # On Windows, use: .\env\Scripts\activate
    ```

3. **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```

4. **Run Migrations**

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Start Development Server**

    ```
    python manage.py runserver
    ```

6. **Access the API**

    Open your web browser and go to `http://127.0.0.1:8000/api/`.

## Usage

- Use the provided API endpoints to interact with the project.
- Refer to the API documentation or code comments for details on how to use each endpoint.

## Additional Information

- For more information about Django, visit [Django Documentation](https://docs.djangoproject.com/en/3.2/).
- This project was completed as part of an assignment, and all three levels were successfully implemented.

---

