##Django Boilerplate

Django Boilerplate is a set of project layouts that through trial and error we use
as a best practice.  Details about each project are stored in conf/project.py and are imported to
allow for maximum re-usability.


#Assumptions

* Python 2.7, PIP, and virtualenv installed.
* Use south
* Django 1.3.1 is the latest version of django at the current time.

## Setup

Setup a new virtualenv

    virtualenv projectname --no-site-packages
    
Activate the virtualenv
    
    source project/bin/activate
    
Install the build requirement of fabric

    pip install fabric

Add any vendor apps to requirements.txt.

