#! /bin/bash
echo "正在进行适用于中国大陆的本地化设置"
sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list
sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
apt update
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple