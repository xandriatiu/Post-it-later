#!/bin/bash

pip --version >/dev/null 2>&1 || {
    echo >&2 -e "\npip is required but it's not installed."
    echo >&2 -e "You can install it by running the following command:\n"
    echo >&2 "wget https://bootstrap.pypa.io/get-pip.py; chmod +x get-pip.py; sudo ./get-pip.py"
    echo >&2 -e "\n"
    echo >&2 -e "\nFor more information, see pip documentation: https://pip.pypa.io/en/latest/"
    exit 1;
}

virtualenv --version >/dev/null 2>&1 || {
    echo >&2 -e "\nvirtualenv is required but it's not installed."
    echo >&2 -e "You can install it by running the following command:\n"
    echo >&2 "sudo pip install virtualenv"
    echo >&2 -e "\n"
    echo >&2 -e "\nFor more information, see virtualenv documentation: https://virtualenv.pypa.io/en/latest/"
    exit 1;
}
