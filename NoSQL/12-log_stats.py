#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def main():
    """Display stats about the logs.nginx collection"""

    # MongoDB-ə qoşuluruq (checker localhost istifadə edir)
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Ümumi log sayı
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # HTTP metodlarına görə say
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET /status sorğularının sayı
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    main()
