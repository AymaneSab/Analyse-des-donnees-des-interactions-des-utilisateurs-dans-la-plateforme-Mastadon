#!/usr/bin/env python3

import sys
import json
import re

for line in sys.stdin:

    try:
    
        # Charger les données JSON
        data = json.loads(line)
        
        # Toots related information : 
        toot_data = data
        toot_id = toot_data["id"]
        
        # User related information : 
        account = data.get('account')
        user_id = account.get('id')
        

        if toot_id is not None:
            
            sensitive = toot_data.get('sensitive')
            visibility = toot_data.get('visibility')
            language = toot_data.get('language')

	    
            print(f"TootsSensibility_{sensitive}\t1")
            print(f"Tootsvisibility_{visibility}\t1")
            
            if language:
                print(f"Tootslanguage_{language}\t1")
            
            if toot_data.get('media_attachments') != []: 
                print(f"HasMediaAttachments_{toot_id}\t1")
            
            # regular expression pattern for matching URLs
            url_pattern = r'https?://\S+'

            # Extract all matching URLs from the content
            content = toot_data.get('content', '')
            
            if content:
                urls = re.findall(url_pattern, content)
                for url in urls:
                    print(f"Url_{url}\t1")
            
            # Extract mentions
            mentions = toot_data.get('mentions', [])
            for mention in mentions:
                print(f"Mention_{mention}\t1")
            
            # Extract  tags
            tags = toot_data.get('tags', [])
            for tag in tags:
                if tag:
                    print(f"Tag_{tag}\t1")
                
        # Extract user related information : 
        if user_id is not None:
            
            followers_count = account.get('followers_count', 0) 
            reblogs_count = account.get('reblogs_count' , 0)
            favourites_count = account.get('favourites_count' , 0)

            
            if followers_count != 0 :
            
            	print(f"UserFollowerCount_{user_id}\t{followers_count}")
            	
            	user_engagment = int((reblogs_count + favourites_count ) / followers_count)
            	print(f"UserEngagementRate_{user_id}\t{user_engagment}")
	
            account_creation_date = account.get('created_at' , '')[:10]
            
            if account_creation_date:
            
                Year  =  account_creation_date[:4]
                Month =  account_creation_date[5:7]
                Day   =  account_creation_date[8:10]
                
                # get the full account creation date 
                
                print(f"UserDate_{account_creation_date}\t1")
            
                # Get the year 
                print(f"DateYear_{Year}\t1")

            
    except Exception as e:
        print("Error at mapper :", str(e))
        
