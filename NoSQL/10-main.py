#!/usr/bin/env python3
"""
Python script to provide some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def main():
    """Display stats about Nginx logs"""
    client = MongoClient()  # Default connection to localhost:27017
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET /status requests
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    main()
