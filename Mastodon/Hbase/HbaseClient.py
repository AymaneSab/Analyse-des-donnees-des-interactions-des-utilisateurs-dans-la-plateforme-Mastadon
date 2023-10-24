#!/usr/bin/env python3

import happybase
import json
from hdfs import InsecureClient

# HBase and HDFS connection parameters
hbase_host = 'localhost'  # HBase host
hbase_port = 9090         # HBase port

hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

#  The input data 
hdfs_file = '/output/ReducerResult43/part-00000'

with hdfs_client.read(hdfs_file) as hdfs_file:
    hdfs_file_contents = hdfs_file.read() # 

try:
    # Initialize a connection to HBase
    connection = happybase.Connection(host=hbase_host, port=hbase_port)
    print("Connected to HBase")

    # Open the 'User' table
    user_table_name = 'User'
    user_table = connection.table(user_table_name) # set a connection to the hbase table 
    print(f"Connected to table: {user_table_name}")
    
    # Read and process User data 
    try:
        data = json.loads(hdfs_file_contents)
        userFollowerCount = data.get('UserFollowerCount')
        userEngagementRate = data.get('UserEngagementRate')

        if userFollowerCount and userEngagementRate:
            for user_id, follower_count in userFollowerCount.items():
                if user_id in userEngagementRate:
                    engagement_rate = userEngagementRate[user_id]

                    user_table.put(
                        user_id.encode('utf-8'),
                        {
                            'UserInfo:FollowerCount': str(follower_count).encode('utf-8'),
                            'UserInfo:EngagementRate': str(engagement_rate).encode('utf-8'),
                        }
                    )
        else:
            print("User Data is not enough in the JSON")      
    except json.JSONDecodeError as e:
    
        print(f"JSON parsing error in user table:  {e}")
    
    # Open the table for Toots language data
    toots_language_table_name = 'Language'
    toots_language_table = connection.table(toots_language_table_name)
    print(f"Connected to table: {toots_language_table_name}")
    
    # Read and process Toots language data from HDFS
    try:
        data = json.loads(hdfs_file_contents)
        toots_language = data.get('Tootslanguage')

        if toots_language:
            for language, count in toots_language.items():
                toots_language_table.put(
                    language.encode('utf-8'),
                    {'Language:Count': str(count).encode('utf-8')}
                )
        else:
            print("No 'Tootslanguage' data in the JSON")
    except json.JSONDecodeError as e:
        print(f"JSON parsing error in language table:  {e}")


    # Open the table for URLShare data
    urlshare_table_name = 'URLShare'
    urlshare_table = connection.table(urlshare_table_name)
    print(f"Connected to table: {urlshare_table_name}")

    # Read and process URLShare data from HDFS
    try:
        data = json.loads(hdfs_file_contents)
        url_content = data.get('Url')

        if url_content:
            for url, share_count in url_content.items():
                urlshare_table.put(
                    url.encode('utf-8'),
                    {
                        'URLInfo:Url': str(url).encode('utf-8'),
                        'ShareCount:Count': str(share_count).encode('utf-8')
                    }
                )
        else:
            print("No 'Url' data in the JSON")
    except json.JSONDecodeError as e:
        print(f"JSON parsing error in url table :  {e}")
        
    # Open the table for tag data
    Mention_table_name = 'Mentions'
    Mention_table = connection.table(Mention_table_name)
    print(f"Connected to table: {Mention_table_name}")
        
    # Read and process Mention data from HDFS
    try:
        data = json.loads(hdfs_file_contents)
        mention_content = data.get('Mention')

        if mention_content:
            for mention, mention_count in mention_content.items():
                Mention_table.put(
                    mention.encode('utf-8'),
                    {
                        'MentionsInfo:Count': str(mention_count).encode('utf-8'),
                    }
                )
        else:
            print("No 'Mention' data in the JSON")     
    except json.JSONDecodeError as e:
        print(f"JSON parsing error in mentions table :  {e}")

    # Open the table for tag data
    Tag_table_name = 'Tags'
    Tag_table = connection.table(Tag_table_name)
    print(f"Connected to table: {Tag_table_name}")
    
    #Read and process URLShare data from HDFS
    try:
        data = json.loads(hdfs_file_contents)
        Tag_content = data.get('Tag')

        if Tag_content:
            for tag, tag_count in Tag_content.items():
                Tag_table.put(
                    tag.encode('utf-8'),
                    {
                        'TagsInfo:Count': str(tag_count).encode('utf-8'),
                    }
                )
        else:
            print("No 'tag' data in the JSON")  
    except json.JSONDecodeError as e:
        print(f"JSON parsing error in tag tables :  {e}")

    # Open the table for tag data
    MastodonGrowth_table_name = 'MastodonGrowth'
    MastodonGrowth_table = connection.table(MastodonGrowth_table_name)
    print(f"Connected to table: {MastodonGrowth_table_name}")
    
    #Read and process URLShare data from HDFS
    try:
        data = json.loads(hdfs_file_contents)
        MastodonGrowth = data.get('UserDate')

        if MastodonGrowth:
            for date, number_count in MastodonGrowth.items():
                MastodonGrowth_table.put(
                    date.encode('utf-8'),
                    {
                        'DateMetrics:Count': str(number_count).encode('utf-8'),
                    }
                )
        else:
            print("No 'Date' data in the JSON")  
            
    except json.JSONDecodeError as e:
        print(f"JSON parsing error in date metrics tables :  {e}")


    # Close the connection
    connection.close()
    print("Connection closed")
    
except Exception as ex:
    print(f"An error occurred: {ex}")
    
