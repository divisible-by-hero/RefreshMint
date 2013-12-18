include:
- python

/home/vagrant/.virtualenvs/refresh:
    virtualenv.managed:
        - no_site_packages: True
        - runas: vagrant
        - requirements: salt://django/requirements.txt
        - require:
            - pkg: python-virtualenv
            - pkg: libxml2-dev
            - pkg: libxslt-dev
