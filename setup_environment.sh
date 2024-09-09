#!/bin/sh

# Update package list
sudo apt-get update

# Install Python 3 and pip
sudo apt install python3-pip -y

# Install core dependencies
sudo pip install apache-airflow pandas s3fs tweepy

# Install MySQL client development files
sudo apt install default-libmysqlclient-dev -y

# Install OpenJDK 11 for PySpark
sudo apt-get install openjdk-11-jdk -y

# Install Python 3.8 and make it default
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update
sudo apt-get install python3.8 -y

# List installed Python versions
ls /usr/bin/python*

# Make Python 3.8 the default version
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 3
# Allow user to select default Python version
sudo update-alternatives --config python

# Install additional required packages
sudo apt-get install pkg-config -y
sudo apt-get install libmysqlclient-dev -y

# Install Airflow providers
pip install apache-airflow-providers-ssh
pip install apache-airflow-providers-mysql
pip install apache-airflow-providers-oracle
pip install apache-airflow-providers-microsoft-mssql
pip install apache-airflow-providers-amazon
pip install apache-airflow-providers-apache-spark
pip install apache-airflow-providers-snowflake

# Upgrade pip and setuptools for compatibility
pip install --upgrade pip setuptools

# Install AWS CLI
sudo apt install awscli -y

# Upgrade OpenSSL and cryptography for security
pip install --upgrade pyOpenSSL cryptography

# Install PySpark (fix potential errors by specifying a compatible version)
pip install pyspark==3.1.2
