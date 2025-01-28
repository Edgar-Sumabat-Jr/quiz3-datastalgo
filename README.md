# Django Backend API

## Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run migrations:
    ```bash
    python manage.py migrate
    ```
4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
5. Run the server:
    ```bash
    python manage.py runserver
    ```

## Endpoints
- `GET /api/accounts/users/` - List of all users.
- `GET /api/accounts/user/{id}/` - Specific user details.
- `GET /api/products/products/` - List of all products.
- `GET /api/products/product/{uuid}/` - Specific product details.
        
