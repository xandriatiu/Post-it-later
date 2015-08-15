Django Boilerplate
==================

A base template for Django projects.

- Django v1.8.3
- Bootstrap v3.3.5
- jQuery v2.1.4

This repository contains multiple branches from which you can clone. The master branch contains the most minimal setup from which all other base branches which contain enhancements branch out from.

Please refer to the branch list below for more information.


------------


####**Branch: Master**####
- Django v1.8.3

####**Branch: Enhanced**####
- Django v1.8.3
- Bootstrap v3.3.5
- jQuery v2.1.4

- django-bootstrap-form==3.2
- django-braces==1.8.1
- django-flat-theme==0.9.5
- easy-thumbnails==2.2

- MySQL and Postgre ready


-----------


Setup:
------

    1. update ./requirements.txt change `base` to [ local, test, or prod ]

    2. update PROJECT_NAME on the bin/*.sh files

    3. cp ./conf/local_settings.tpl ./conf/local_settings.py

Bash Scripts
------------

    1. ./bin/install_os_dependencies.sh

    2. ./bin/check_python_dependencies.sh

    3. ./bin/prepare_local_environment.sh

    4. ./bin/sync_dev.sh


-----------


Contribution
------------

Feel free to issue pull requests guys! :)

This repository is still very much a work in progress and may not work properly for some people. If you find any issues, don't hesitate to file an issue or submit a pull request with your fix.
