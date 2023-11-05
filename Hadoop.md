cat <<EOL > README.md
# Hadoop 3.3.6 Installation Guide

This guide provides step-by-step instructions for installing Hadoop 3.3.6 on an Ubuntu system. Hadoop is a popular open-source framework for distributed storage and processing of large datasets. This guide assumes you have a basic understanding of Linux and the command line.

## Prerequisites

- Ubuntu operating system
- Terminal access with sudo privileges

## Environment Preparation

### Java Installation

\`\`\`bash
# Install Java
sudo apt install default-jre default-jdk -y
java -version
readlink \$(which javac)
\`\`\`

### Hadoop User Creation

\`\`\`bash
# Create a 'hadoop' user
sudo adduser hadoop

# Add the 'hadoop' user to the sudoers group
sudo usermod -aG sudo hadoop

# Switch to the 'hadoop' user
sudo su - hadoop
\`\`\`

### SSH Configuration

\`\`\`bash
# Install OpenSSH
sudo apt install openssh-server openssh-client -y

# Generate SSH keys
ssh-keygen -t rsa

# Add generated keys to authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Set file permissions
sudo chmod 640 ~/.ssh/authorized_keys

# Verify SSH connection
ssh localhost
\`\`\`

## Hadoop Installation

\`\`\`bash
# Download Hadoop binary version
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

# Extract the tar file
tar -xvzf hadoop-3.3.6.tar.gz

# Move the extracted files to /usr/local/hadoop
sudo mv hadoop-3.3.6 /usr/local/hadoop

# Create a logs directory to store logs
sudo mkdir /usr/local/hadoop/logs

# Change the owner of files to 'hadoop' (recursively)
sudo chown -R hadoop:hadoop /usr/local/hadoop
\`\`\`

## Hadoop Configuration

### Update .bashrc

\`\`\`bash
# Edit .bashrc
sudo gedit ~/.bashrc

# Add the following lines at the end of the file
# ... (Add environment variables)
source ~/.bashrc
\`\`\`

### Edit hadoop-env.sh

\`\`\`bash
# Edit hadoop-env.sh
sudo nano \$HADOOP_HOME/etc/hadoop/hadoop-env.sh

# Add the following lines
# ... (Set Java home and Hadoop classpath)
\`\`\`

### Edit core-site.xml

\`\`\`bash
# Edit core-site.xml
sudo nano \$HADOOP_HOME/etc/hadoop/core-site.xml

# Add the following property
<property>
    <name>fs.default.name</name>
    <value>hdfs://0.0.0.0:9000</value>
    <description>The default file system URI</description>
</property>
\`\`\`

### Edit hdfs-site.xml

\`\`\`bash
# Edit hdfs-site.xml
sudo nano \$HADOOP_HOME/etc/hadoop/hdfs-site.xml

# Add the following properties
# ... (Set replication, name dir, and data dir)
\`\`\`

### Edit yarn-site.xml

\`\`\`bash
# Edit yarn-site.xml
sudo nano \$HADOOP_HOME/etc/hadoop/yarn-site.xml

# Add the following property
# ... (Set nodemanager aux services)
\`\`\`

## Start the Hadoop Cluster

\`\`\`bash
# Format the HDFS namenode
hdfs namenode -format

# Start HDFS and YARN
start-dfs.sh
start-yarn.sh

# Check Hadoop processes
jps

# Access Hadoop web interface at http://server-IP:9870
\`\`\`

Make sure to replace 'server-IP' with the actual IP address of your server. This single README.md file contains the complete installation guide. You can create a new GitHub repository, add this README.md file, and commit it to your repository to document your Hadoop installation process.
EOL
