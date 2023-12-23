# Data Developer Project README

This repository contains the code and documentation for the Data Developer project, which aims to set up an automated data pipeline to address the following challenges:

## Project Overview

![Alt text](https://www.simplilearn.com/ice9/free_resources_article_thumb/What_is_Hadoop.jpg)

### Data Collection

- Utilize the platform's API with its access tokens.
- Gather raw data from the Mastodon Platform.
- Store raw data in a distributed file system such as HDFS for scalability.
- Define the HDFS Data Lake schema.

### MapReduce Processing

- Mapper: Process input data and generate key-value pairs based on the desired metrics (e.g., user followers, engagement rate, URLs, emojis, etc.).
- Reducer: Aggregate key-value pairs produced by the mapper.

### MapReduce Job Execution

- Use Hadoop Streaming API to execute the MapReduce task.
- Monitor task progress using the Hadoop web interface.

### Results Storage in HBase

- Design the HBase schema based on the information to be extracted.
- Follow best practices for row key design, column family design, compression, bloom filters, batch inserts, etc.
- Create the necessary tables in HBase.
- Insert reducer output into HBase tables using a Python HBase client or a preferred method.

### Apache Airflow Orchestration

- Define a Directed Acyclic Graph (DAG) to orchestrate the workflow.
- Create tasks to execute the MapReduce job and store results in HBase.
- Monitor progress and manage errors or failures.

### Results Analysis

- Query HBase tables to retrieve stored results.

## Analysis Queries

### User Analysis

- Identify users with the highest number of followers.
- Analyze user engagement rates.
- Analyze user growth over time using the `user_created_at` metric.

### Content Analysis

- Identify the most shared external websites (URLs).

### Language and Region Analysis

- Analyze the distribution of posts based on their language.

### Media Engagement Analysis

- Determine the number of posts with multimedia attachments.

### Tags and Mentions Analysis

- Identify the most frequently used tags and mentioned users.

## Workflow Execution

- In the Airflow web interface, activate the DAG.
- Monitor DAG execution progress.
- Check logs for any issues.
- Once the DAG is completed, review the results in HBase.

## Optimization and Monitoring

- Optimize MapReduce scripts for better performance.
- Monitor HBase for storage issues.
- Configure Airflow alerts for task failures.
- Regularly monitor Hadoop using its respective web interface.

## Data Feed Access Permissions

- API Mastodon: Ensure that the API tokens used have the necessary permissions to retrieve data.
- If organizational roles change, update the API tokens accordingly and ensure they have the necessary search permissions.

## Access and Data Sharing Rules Documentation

- Update documentation to include details on roles with specific permissions.
- Explain how to request access and the access granting/revoking process.

## Scheduled Updates and New Automated Feeding Procedures

- Schedule DAGs to run at appropriate intervals for data refresh.

## GDPR Compliance Data Processing Registry Update

- Document all personal data ingested from Mastodon and how it is processed and stored.
- Ensure all data processing activities comply with GDPR regulations.

Feel free to use this README file as a reference for your project's documentation. If you have any questions or need further assistance, please don't hesitate to ask.
