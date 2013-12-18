##RefreshMint

RefreshMint is an open-source starter kit for creating your own Refresh communities.

[Refreshing Cities](http://www.refreshingcities.org)

Features include:
* Blog
* Events
* Member profiles
* Social media integration
* Code of Conduct templates

#Assumptions

* Python 2.7, PIP, and virtualenv installed.
* Use south
* Django 1.6.1 is the latest version of django at the current time.

## Setup

Setup a new virtualenv

    virtualenv projectname --no-site-packages
    
Activate the virtualenv
    
    source projectname/bin/activate
    

Run the demo instance

    cd example/
    python manage.py runserver --settings=example.settings
