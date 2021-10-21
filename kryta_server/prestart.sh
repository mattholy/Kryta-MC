#! /bin/bash

echo "We are going start"
#do some localization, use zh-cn by default
localize_script_name="${KEYTA_SERVER_LOCATION:-zh-cn}"
eval . ./utils/init_template/localize_scripts/${localize_script_name}.sh

apt install sqlite3
pip install -r requirements.txt

mkdir -p /app/data/logs
mkdir -p /app/data/db
mkdir -p /app/data/server_data
mkdir -p /app/data/user_data