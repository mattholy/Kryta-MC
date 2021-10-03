#! /bin/bash
echo "给我也整一个"
sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list
sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
apt update
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

apt install sqlite3
pip install -r requirements.txt