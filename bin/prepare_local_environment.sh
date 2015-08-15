#!/bin/bash

PROJECT_NAME=''

SCRIPT_SOURCE=`dirname "$BASH_SOURCE"`
PROJ_DIR=$SCRIPT_SOURCE/..
LOG_DIR=$PROJ_DIR/../var/logs
STATIC_DIR=$PROJ_DIR/frontend/static
MEDIA_DIR=$PROJ_DIR/frontend/media
ENV_DIR=$PROJ_DIR/../env


echo "CHECKING LOGS DIRECTORY..."
test -d $LOG_DIR || mkdir -p $LOG_DIR

echo "CHECKING STATIC FILES DIRECTORY..."
test -d $STATIC_DIR || mkdir -p $STATIC_DIR

echo "CHECKING MEDIA FILES DIRECTORY..."
test -d $MEDIA_DIR || mkdir -p $MEDIA_DIR

echo 'CHECKING VIRTUAL ENVIRONMENT...'
if [ -x "$(command -v deactivate)" ]; then deactivate; fi
test -d $ENV_DIR || virtualenv --prompt="($PROJECT_NAME)" $ENV_DIR

echo 'ACTIVATING VIRTUALENV...'
source $ENV_DIR/bin/activate

echo 'INSTALLING DEPENDENCIES...'
pip install -q -r $PROJ_DIR/requirements.txt

echo "CREATING DATABASE MIGRATIONS..."
python $PROJ_DIR/manage.py makemigrations

echo "APPLYING MIGRATIONS..."
python $PROJ_DIR/manage.py migrate

echo "COLLECTING STATIC FILES..."
python $PROJ_DIR/manage.py collectstatic


echo 'DONE!'
echo 'You can now activate your virtualenv and runserver.'
