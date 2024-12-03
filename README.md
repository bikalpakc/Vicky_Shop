
# Vicky Shop

A simple e-commerce website with all the required features to make Shopping and Selling easy.


## Features

- Real-time Notification with Django Channels
- Notification scheduling functionality for Admin
- Live Chat Service with Tawk
- Fast and Efficient search with Elastic Search
- Redis Caching enabled for faster Loading Time
- Payment made easy with Paypal
- Email is sent with bill through Celery worker after the order is placed
- Ajax updates the Cart Live.

Screenshots attached at the end of this file.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY` (Django)

`client_id` (Paypal)

#To send email:

`EMAIL_HOST_USER`

`EMAIL_HOST_PASSWORD`


## Run Locally

Clone the project or download as a Zip file and extract.

```bash
  git clone https://github.com/bikalpakc/Vicky_Shop
```

Go to the project directory

```bash
  cd vicky
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the Redis Server

```bash
  Download Redis and activate on port 6379
```

Run the docker-compose.yml file for Elastic Search

```bash
  docker compose up
```

Start the Celery server

```bash
  celery -A vicky.celery worker --pool=solo -l info
```

Start the Celery-beat server

```bash
  celery -A vicky beat -l info
```

Start the Daphne ASGI server

```bash
  daphne -p 8000 vicky.asgi:application
```

If you don't want websocket connection features, start the WSGI server instead

```bash
  python manage.py runserver
```





## Acknowledgements

 - [Front-end Templates by Geeky Shows](https://github.com/geekyshow1/shoppinglyx)
 - [Live Chat API](https://www.tawk.to/)



## Technologies Used
- HTML
- CSS
- JS
- BootStrap
- Python
- Python Django
- Ajax
- Elastic Search
- Redis
- Celery
- Celery-beat
- tawk.to API




## Screenshots



