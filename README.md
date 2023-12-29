# Google Gemini Model API Integration with Django

## Overview

This project demonstrates the integration of Google's Gemini model API into a Python Django application. The Gemini model is a powerful generative AI model developed by Google. This README provides instructions on setting up the project, obtaining the API credentials, and running the Django application locally.

## Prerequisites

- Python 3.x installed
- Django installed (`pip install Django`)
- Google Cloud Platform (GCP) account
- Service account credentials with access to the Gemini model API
- Google AI Studio API key

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/gemini-django-integration.git
    ```

2. Navigate to the project directory:

    ```bash
    cd gemini
    ```

3. Set up Django migrations:

    ```bash
    python manage.py migrate
    ```

## Configuration

1. Obtain Google AI Studio API key and replace the placeholder in `config/settings.py`:

    ```python
    # config/settings.py

    GOOGLE_API_KEY = 'your_google_ai_studio_api_key'
    ```

2. Set up service account credentials:

    - Download the service account JSON key file.
    - Rename the file to `service_account.json`.
    - Place the file in the project root directory.

## Running the Application

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your browser and navigate to [http://localhost:8000](http://localhost:8000).

## Usage

- Visit the homepage to see a simple implementation of the Gemini model API in action.
- Explore the Django code to understand how to integrate the API into your own views and templates.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and improvements are welcome!


**Note**: Ensure that you keep your API keys and service account credentials secure. Do not share them publicly or commit them to version control.
