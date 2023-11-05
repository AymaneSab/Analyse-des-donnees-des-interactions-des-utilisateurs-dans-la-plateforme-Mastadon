# Hadoop 3.3.6 Installation Guide

This guide provides step-by-step instructions for installing Hadoop 3.3.6 on a Linux-based system. Follow these steps to set up your Hadoop environment.

## Table of Contents
- [Environment Preparation](#environment-preparation)
  - [Java Installation](#java-installation)
  - [Hadoop User Creation](#hadoop-user-creation)
  - [SSH Configuration](#ssh-configuration)
- [Hadoop Installation](#hadoop-installation)
- [Hadoop Configuration](#hadoop-configuration)
  - [Environment Variables](#environment-variables)
  - [Java Environment Variables](#java-environment-variables)
  - [Hadoop Configuration Files](#hadoop-configuration-files)
    - [core-site.xml](#core-site-xml)
    - [hdfs-site.xml](#hdfs-site-xml)
    - [mapred-site.xml](#mapred-site-xml)
    - [yarn-site.xml](#yarn-site-xml)
- [Starting the Hadoop Cluster](#starting-the-hadoop-cluster)

## Environment Preparation

### Java Installation

Install Java and configure it:

```shell
sudo apt install default-jre default-jdk -y
java -version
readlink $(which javac)
```

### Hadoop User Creation

To create a dedicated Hadoop user and add it to the sudoers group, follow these steps:

```shell
# Create the Hadoop user:
sudo adduser hadoop

# Add the Hadoop user to the sudoers group:
sudo usermod -aG sudo hadoop

# Switch to the Hadoop user:
sudo su - hadoop
```

### SSH Configuration
```shell

# Install and configure SSH for passwordless login:
sudo apt install openssh-server openssh-client -y
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
sudo chmod 640 ~/.ssh/authorized_keys
ssh localhost
```

## Hadoop Installation
### Hadoop Installation
Download and install Hadoop:

```shell
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xvzf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/hadoop
sudo mkdir /usr/local/hadoop/logs
sudo chown -R hadoop:hadoop /usr/local/hadoop
```
## Hadoop Configuration
### Environment Variables
Edit your .bashrc file to set Hadoop environment variables:

```shell
sudo gedit ~/.bashrc

# Add the following lines:
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"

# Save the file and run:
source ~/.bashrc
```

### Java Environment Variables
Edit hadoop-env.sh to set Java environment variables:

```shell
sudo nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# Add the following lines:
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export HADOOP_CLASSPATH+=" $HADOOP_HOME/lib/*.jar"

# Save the file.
```

### Hadoop Configuration Files
#### core-site.xml
Edit core-site.xml to configure the default file system URI:

```shell
sudo nano $HADOOP_HOME/etc/hadoop/core-site.xml
```
```shell
<property>
    <name>fs.default.name</name>
    <value>hdfs://0.0.0.0:9000</value>
    <description>The default file system URI</description>
</property>
```


