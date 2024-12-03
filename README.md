
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
![Screenshot 2024-12-02 140028](https://github.com/user-attachments/assets/9aada217-60dd-4b01-96a6-0c0a261f83bb)
![Screenshot 2024-12-02 203218](https://github.com/user-attachments/assets/fbfd7e89-72c7-4378-8f69-30b82f1204c5)
![Screenshot 2024-12-03 140957](https://github.com/user-attachments/assets/b359a809-5fc9-460c-abd1-6e914b93fda1)
![Screenshot 2024-12-03 141142](https://github.com/user-attachments/assets/928ff9ef-8596-46ea-8882-c36bfcc37669)
![Screenshot 2024-12-03 143049](https://github.com/user-attachments/assets/4dd06c95-2190-4700-ae90-2909a98f1df4)
![Screenshot 2024-12-03 141620](https://github.com/user-attachments/assets/11a5678a-bec3-43a7-9537-b517d09fe6fb)
![Screenshot 2024-12-03 141704](https://github.com/user-attachments/assets/03e0082c-fb78-459a-b489-a682982cfaa6)
![Screenshot 2024-12-03 141439](https://github.com/user-attachments/assets/70e76b91-29dd-458e-828c-b3d6d2ea5233)







