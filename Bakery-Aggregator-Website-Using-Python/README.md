**Bakery Aggregator Website Using Python (Django Framework)**

This project is a dynamic web-based application designed to aggregate bakery services, allowing users to browse and purchase cakes from various bakeries. Developed using the Django framework, the platform includes robust user and admin authentication, efficient search and filter functionalities, and a streamlined inventory and order management system for administrators.

**Steps:**

1. Clone the repository
2. Create a virtual environment:

    ```python -m venv venv```
   
   ```source venv/bin/activate  # On Windows, use "venv\Scripts\activate"```

3. Install the required packages:

certifi
chardet
defusedxml
Django
django-allauth
idna
oauthlib
Pillow
pkg-resources
python-decouple
python3-openid
pytz
requests
requests-oauthlib
sqlparse
urllib3


4. Apply migrations:

```python manage.py migrate```

5. Create a superuser:

```python manage.py createsuperuser```

6. Run the development server:

```python manage.py runserver```

7. Access the application:
Open your web browser and navigate to http://127.0.0.1:8000/.
