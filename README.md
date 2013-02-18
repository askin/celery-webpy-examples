Celery Web.py Examples
=====================

# Installation

    # Install RabbitMQ Server
    sudo apt-get install rabbitmq-server

    # Install Celery
    sudo pip install celery

    # Install webpy
    sudo pip install web.py

# Running

    # Run Web.py web services
    cd webpy
    python services.py

    # Run Celery
    cd celery
    celeryd -I tasks

    # run example codes
    cd client
    python client.py

    # play with tasks function
    cd celery
    python
    >>> from tasks import remoteAdd
    >>> result = remoteAdd.delay(2, 2)
    >>> result.get()
    4
