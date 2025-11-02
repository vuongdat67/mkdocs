# Docker Compose Django PostgreSQL Nginx

Complete guide to setting up a production-ready Django application with Docker Compose.

## Project Structure

```
myproject/
├── docker-compose.yml
├── Dockerfile
├── nginx/
│   └── nginx.conf
├── requirements.txt
└── myapp/
    ├── manage.py
    └── ...
```

## Docker Compose Configuration

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=mypassword
    
  web:
    build: .
    command: gunicorn myapp.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/code
      - static_volume:/code/staticfiles
    expose:
      - 8000
    environment:
      - DATABASE_URL=postgresql://myuser:mypassword@db:5432/mydb
    depends_on:
      - db
    
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/code/staticfiles
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
```

## Dockerfile

```dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN python manage.py collectstatic --noinput
```

## Nginx Configuration

```nginx
events {
    worker_connections 1024;
}

http {
    upstream web {
        server web:8000;
    }

    server {
        listen 80;
        
        location / {
            proxy_pass http://web;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
        
        location /static/ {
            alias /code/staticfiles/;
        }
    }
}
```

## Requirements

```txt
Django>=4.2
psycopg2-binary>=2.9
gunicorn>=21.0
```

## Running the Stack

```bash
# Build and start
docker-compose up -d --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# View logs
docker-compose logs -f
```

!!! warning "Production Note"
    Remember to set proper environment variables and secrets in production!

## Benefits

- ✅ Isolated environment
- ✅ Easy to replicate
- ✅ Scalable architecture
- ✅ Production-ready setup

That's it! Your Django app is now running with PostgreSQL and Nginx.
