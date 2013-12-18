include:
  - python 

newrelic-ppa:
  pkgrepo.managed:
    - human_name: New Relic PPA
    - name: deb http://apt.newrelic.com/debian/ newrelic non-free
    - key_url: http://download.newrelic.com/548C16BF.gpg

newrelic-php5:
  pkg.installed:
    - require:
      - pkgrepo: newrelic-ppa

newrelic-sysmond:
  pkg.installed:
    - require:
      - pkgrepo: newrelic-ppa
  service.running:
    - watch:
      - pkg: newrelic-sysmond
      - file: newrelic-sysmond-conf
    - require:
      - file: newrelic-sysmond-conf

newrelic-sysmond-conf:
  file.managed:
    - name: /etc/newrelic/nrsysmond.cfg
    - source: salt://newrelic/nrsysmond.cfg.jinja
    - template: jinja
    - require:
      - pkg: newrelic-sysmond

/etc/php5/fpm/conf.d/newrelic.ini:
  file.managed:
    - source: salt://newrelic/newrelic.ini
    - template: jinja
    - require:
      - pkg: newrelic-php5
      - pkgrepo: newrelic-ppa

newrelic-plugin-agent:
  pip.installed

/etc/newrelic/newrelic_plugin_agent.cfg:
  file.managed:
    - source: salt://newrelic/newrelic_plugin_agent.cfg
    - user: newrelic
    - group: newrelic
    - require:
      - pip: newrelic-plugin-agent

/var/run/newrelic:
  file.directory:
    - makedirs: True
    - user: newrelic
    - group: newrelic

/var/log/newrelic:
  file.directory:
    - makedirs: True
    - user: newrelic
    - group: newrelic
