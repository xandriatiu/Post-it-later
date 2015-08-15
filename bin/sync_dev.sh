#!/bin/bash

PROJECT_NAME=''

SCRIPT_SOURCE=`dirname "$BASH_SOURCE"`
PROJ_DIR=$SCRIPT_SOURCE/..
ENV_DIR=$SCRIPT_SOURCE/../../env


echo 'FETCHING LATEST CHANGES...'
git fetch upstream

echo 'MERGING LATEST CHANGES TO DEV...'
git rebase upstream/dev

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
echo 'You can now activate virtualenv and runserver.'
