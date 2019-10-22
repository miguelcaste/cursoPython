# cursoPython
Pasos para instalar Python 3.7.4 (última versión estable) en Ubuntu
1. sudo apt-get install build-essential checkinstall
2. sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
3. cd /usr/src
4. sudo wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
5. sudo tar xzf Python-3.7.4.tgz
6. cd Python-3.7.4
7. sudo ./configure --enable-optimizations
8. sudo make altinstall
9. Lo podemos comprobar con: python3.7 -V