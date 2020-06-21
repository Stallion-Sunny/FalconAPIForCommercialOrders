To start the Mock API server on Mac
gunicorn --reload app:app

To start the Mock API server on Windows
waitress-serve --port=8000 app:app


Default server starts on http://127.0.0.1:8000

Endpoints Mocked
/orders/{order_id}
/tracking/{tracking_id}
/cancel/{id}
/complaint/{id}