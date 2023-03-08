
# Weather API with Django

For this project, Django was chosen as the framework for building the REST API. The Django ORM was used to create models for the weather data records and migrations were created to set up the tables in the SQLite database. Migrations allow changes to the database schema to be easily managed over time.

A script was written to ingest weather data from raw text files into the database using the Django ORM. The script checks for duplicates and provides log output indicating start and end times and the number of records ingested.

For data analysis, Django's ORM was used to filter and aggregate the data in the database. Two API endpoints were created (/api/weather and /api/weather/stats) using the Django REST Framework. The generics.ListAPIView class was used to return a list of objects from the database, while PageNumberPagination was used for pagination purposes. The DjangoFilterBackend class provided filtering capabilities to the API, allowing clients to filter the response by specific fields.

The Weather and Stats classes were created, both inherited from generics.ListAPIView, with queryset, serializer_class, pagination_class, filter_backends, and filterset_fields attributes defined for each. Django's QuerySet API was used to filter the data based on date and station ID parameters in the query string, and to calculate the average maximum and minimum temperatures and total accumulated precipitation for each year and each weather station.

Overall, Django's ORM and QuerySet API make it easy to work with databases in a more object-oriented way, while the Django REST framework and its built-in support for pagination and filtering capabilities made implementing the API endpoints straightforward.

To implement Swagger with Django, I first installed the django-rest-swagger package using pip. Then, I added the rest_framework_swagger app to my Django project's settings file. I defined my API endpoints using Django's REST framework, and used the @swagger_auto_schema decorator to document each endpoint. This decorator allowed me to specify the expected request and response formats, authentication requirements, and other details that would be displayed in the Swagger documentation. Once my API endpoints were defined and documented, I could view the Swagger documentation by navigating to the /swagger/ endpoint of my Django application. From there, I could easily explore and test my API endpoints, making it easier to develop and debug my API.


The API endpoints provide access to the following functionalities:

    /api/weather - retrieves weather data
    /api/weather/stats - provides statistics about the data
    /api/schema/swagger-ui/ - Swagger UI that provides an overview of the API's capabilities.

## Prerequisites

The following prerequisites are required to use this API:

    Python (3.7 or higher)
    Virtualenv
    SQLite

## Installation and Usage

### To install the required dependencies, create and activate a virtual environment with the following commands:

    pip install virtualenv
    virtualenv env

### To activate the virtual environment:

    env/Scripts/activate (in Windows)
    source env/bin/activate (in Linux and Mac)

### Then, install the required dependencies:

    pip install -r requirements.txt

### To run migrations:

    python3 src/manage.py makemigrations
    python3 src/manage.py migrate

### To ingest the data:

    python3 run.py

### To run the server:

    python3 src/manage.py runserver

### To access the API endpoints, use the following links:

    http://127.0.0.1:8000/api/weather
    http://127.0.0.1:8000/api/weather/stats
    http://127.0.0.1:8000/api/schema/swagger-ui/

```
Weather-Data-Ingestion
├─ ingest.py
├─ README.md
├─ requirements.txt
├─ src
│  ├─ app
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ 0001_initial.cpython-310.pyc
│  │  │     ├─ 0001_initial.cpython-38.pyc
│  │  │     ├─ __init__.cpython-310.pyc
│  │  │     └─ __init__.cpython-38.pyc
│  │  ├─ models.py
│  │  ├─ serializers.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ admin.cpython-310.pyc
│  │     ├─ admin.cpython-38.pyc
│  │     ├─ apps.cpython-310.pyc
│  │     ├─ apps.cpython-38.pyc
│  │     ├─ models.cpython-310.pyc
│  │     ├─ models.cpython-38.pyc
│  │     ├─ serializers.cpython-310.pyc
│  │     ├─ serializers.cpython-38.pyc
│  │     ├─ urls.cpython-310.pyc
│  │     ├─ urls.cpython-38.pyc
│  │     ├─ views.cpython-310.pyc
│  │     ├─ views.cpython-38.pyc
│  │     ├─ __init__.cpython-310.pyc
│  │     └─ __init__.cpython-38.pyc
│  ├─ manage.py
│  └─ weather
│     ├─ asgi.py
│     ├─ settings.py
│     ├─ urls.py
│     ├─ wsgi.py
│     ├─ __init__.py
│     └─ __pycache__
│        ├─ settings.cpython-310.pyc
│        ├─ settings.cpython-38.pyc
│        ├─ settings.cpython-39.pyc
│        ├─ urls.cpython-310.pyc
│        ├─ urls.cpython-38.pyc
│        ├─ urls.cpython-39.pyc
│        ├─ wsgi.cpython-310.pyc
│        ├─ wsgi.cpython-38.pyc
│        ├─ __init__.cpython-310.pyc
│        ├─ __init__.cpython-38.pyc
│        └─ __init__.cpython-39.pyc
├─ wx_data
│  ├─ USC00110072.txt
│  ├─ USC00110187.txt
│  ├─ USC00110338.txt
│  ├─ USC00111280.txt
│  ├─ USC00111436.txt
│  ├─ USC00112140.txt
│  ├─ USC00112193.txt
│  ├─ USC00112348.txt
│  ├─ USC00112483.txt
│  ├─ USC00113335.txt
│  ├─ USC00113879.txt
│  ├─ USC00114108.txt
│  ├─ USC00114198.txt
│  ├─ USC00114442.txt
│  ├─ USC00114823.txt
│  ├─ USC00115079.txt
│  ├─ USC00115326.txt
│  ├─ USC00115515.txt
│  ├─ USC00115712.txt
│  ├─ USC00115768.txt
│  ├─ USC00115833.txt
│  ├─ USC00115901.txt
│  ├─ USC00115943.txt
│  ├─ USC00116446.txt
│  ├─ USC00116526.txt
│  ├─ USC00116558.txt
│  ├─ USC00116579.txt
│  ├─ USC00116610.txt
│  ├─ USC00116738.txt
│  ├─ USC00116910.txt
│  ├─ USC00117551.txt
│  ├─ USC00118147.txt
│  ├─ USC00118740.txt
│  ├─ USC00118916.txt
│  ├─ USC00119241.txt
│  ├─ USC00119354.txt
│  ├─ USC00120177.txt
│  ├─ USC00120200.txt
│  ├─ USC00120676.txt
│  ├─ USC00120784.txt
│  ├─ USC00121030.txt
│  ├─ USC00121229.txt
│  ├─ USC00121425.txt
│  ├─ USC00121747.txt
│  ├─ USC00121873.txt
│  ├─ USC00122149.txt
│  ├─ USC00123418.txt
│  ├─ USC00123513.txt
│  ├─ USC00123527.txt
│  ├─ USC00124008.txt
│  ├─ USC00124181.txt
│  ├─ USC00124837.txt
│  ├─ USC00125237.txt
│  ├─ USC00125337.txt
│  ├─ USC00126001.txt
│  ├─ USC00126580.txt
│  ├─ USC00126705.txt
│  ├─ USC00127125.txt
│  ├─ USC00127298.txt
│  ├─ USC00127482.txt
│  ├─ USC00127522.txt
│  ├─ USC00127646.txt
│  ├─ USC00127755.txt
│  ├─ USC00127875.txt
│  ├─ USC00127935.txt
│  ├─ USC00128036.txt
│  ├─ USC00129080.txt
│  ├─ USC00129113.txt
│  ├─ USC00129253.txt
│  ├─ USC00129511.txt
│  ├─ USC00129557.txt
│  ├─ USC00129670.txt
│  ├─ USC00130112.txt
│  ├─ USC00130133.txt
│  ├─ USC00130600.txt
│  ├─ USC00131402.txt
│  ├─ USC00131533.txt
│  ├─ USC00131635.txt
│  ├─ USC00132724.txt
│  ├─ USC00132789.txt
│  ├─ USC00132864.txt
│  ├─ USC00132977.txt
│  ├─ USC00132999.txt
│  ├─ USC00134063.txt
│  ├─ USC00134142.txt
│  ├─ USC00134735.txt
│  ├─ USC00134894.txt
│  ├─ USC00135769.txt
│  ├─ USC00135796.txt
│  ├─ USC00135952.txt
│  ├─ USC00137147.txt
│  ├─ USC00137161.txt
│  ├─ USC00137979.txt
│  ├─ USC00138296.txt
│  ├─ USC00138688.txt
│  ├─ USC00250070.txt
│  ├─ USC00250130.txt
│  ├─ USC00250375.txt
│  ├─ USC00250420.txt
│  ├─ USC00250435.txt
│  ├─ USC00250622.txt
│  ├─ USC00250640.txt
│  ├─ USC00251145.txt
│  ├─ USC00251200.txt
│  ├─ USC00252020.txt
│  ├─ USC00252100.txt
│  ├─ USC00252205.txt
│  ├─ USC00252820.txt
│  ├─ USC00252840.txt
│  ├─ USC00253035.txt
│  ├─ USC00253175.txt
│  ├─ USC00253185.txt
│  ├─ USC00253365.txt
│  ├─ USC00253615.txt
│  ├─ USC00253630.txt
│  ├─ USC00253660.txt
│  ├─ USC00253715.txt
│  ├─ USC00253735.txt
│  ├─ USC00253910.txt
│  ├─ USC00254110.txt
│  ├─ USC00254440.txt
│  ├─ USC00254900.txt
│  ├─ USC00254985.txt
│  ├─ USC00255080.txt
│  ├─ USC00255310.txt
│  ├─ USC00255470.txt
│  ├─ USC00255565.txt
│  ├─ USC00256040.txt
│  ├─ USC00256135.txt
│  ├─ USC00256570.txt
│  ├─ USC00256970.txt
│  ├─ USC00257070.txt
│  ├─ USC00257515.txt
│  ├─ USC00257715.txt
│  ├─ USC00258133.txt
│  ├─ USC00258395.txt
│  ├─ USC00258465.txt
│  ├─ USC00258480.txt
│  ├─ USC00258915.txt
│  ├─ USC00259090.txt
│  ├─ USC00259510.txt
│  ├─ USC00331072.txt
│  ├─ USC00331152.txt
│  ├─ USC00331541.txt
│  ├─ USC00331592.txt
│  ├─ USC00331890.txt
│  ├─ USC00332098.txt
│  ├─ USC00332119.txt
│  ├─ USC00332791.txt
│  ├─ USC00333375.txt
│  ├─ USC00333758.txt
│  ├─ USC00333780.txt
│  ├─ USC00334189.txt
│  ├─ USC00335041.txt
│  ├─ USC00335297.txt
│  ├─ USC00335315.txt
│  ├─ USC00336118.txt
│  ├─ USC00336196.txt
│  ├─ USC00336600.txt
│  ├─ USC00336781.txt
│  ├─ USC00338313.txt
│  ├─ USC00338534.txt
│  ├─ USC00338552.txt
│  ├─ USC00338769.txt
│  ├─ USC00338822.txt
│  ├─ USC00338830.txt
│  └─ USC00339312.txt
└─ yld_data
   └─ US_corn_grain_yield.txt

```#� �c�o�d�e�-�c�h�a�l�l�e�n�g�e�
�
�#� �c�o�d�e�
�
�#� �c�o�d�e�
�
�
