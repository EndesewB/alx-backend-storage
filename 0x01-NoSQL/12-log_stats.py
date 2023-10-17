#!/usr/bin/env python3
"""Provides stats on Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def print_nginx_stats(db):
    """Prints stats on Nginx logs from a MongoDB collection."""
    
    nginx_col = db.nginx
    
    total_logs = nginx_col.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    pipeline = [{"$group": {"_id": "$method", "count": {"$sum": 1}}}] 
    method_counts = {
        log["_id"]: log["count"] for log in nginx_col.aggregate(pipeline)
    }
    
    for method in methods:
        count = method_counts.get(method, 0)
        print(f"\tmethod {method}: {count}")

    pipeline = [
        {"$match": {"method": "GET", "path": "/status"}},
        {"$count": "count"}
    ]
    
    status_check_count = next(nginx_col.aggregate(pipeline))["count"]
    print(f"{status_check_count} status check")


def main():
    """Connects to MongoDB and prints Nginx stats."""
    
    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    
    print_nginx_stats(db)


if __name__ == "__main__":
    main()
