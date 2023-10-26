#!/usr/bin/env python3

import sys
import json

# Initialize a dictionary to store the counts
result_dict = {}

for line in sys.stdin:
    try:
        key, count = line.strip().split('\t')
        count = int(count)

        # Extract the prefix (e.g., "userToots", "Tag") and the identifier (e.g., "427618", "crypto")
        prefix, identifier = key.split('_', 1)

        # Create or update the dictionary entry for the prefix
        if prefix not in result_dict:
            result_dict[prefix] = {}

        # Add the count to the identifier in the dictionary
        if identifier in result_dict[prefix]:
            result_dict[prefix][identifier] += count
        else:
            result_dict[prefix][identifier] = count

    except Exception as e:
        print("Error:", str(e))

# Serialize the result_dict to JSON format
result_json = json.dumps(result_dict, indent=2)


print(result_json)
