#!/usr/bin/env python3
"""
A Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """
    Prints stats about Nginx request logs.
    """
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_counts = {method: nginx_collection.count_documents({'method': method}) for method in methods}
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    status_check_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check_count} status check")


def run():
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)

if __name__ == '__main__':
    run()
