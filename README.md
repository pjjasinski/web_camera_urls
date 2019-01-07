# web_camera_urls

Web online camera url crawler
Extracts camera image url from portal(login, etc...) and store it in a database.

## Getting Started

Download and go to project root directory.  

Run development server
```
python manage.py runserver
```

Run crawl for HZS portal:  
Crawls portal and adds snapshots to database  
```
python manage.py add_snapshots HZS
```
another example...  
```
python manage.py add_snapshots TOPR
```
this commands may be run periodically from cron


### Prerequisites

```
pip install -r requirements.txt
```

### Installing

Migrate and create superuser

```
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
```

Creating portals from cam_crawler directory

```
python manage.py create_portals
```