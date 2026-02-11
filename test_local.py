#!/usr/bin/env python3
"""
Local test script for Lambda function
Run: python test_local.py
"""

from app import lambda_handler

# Simulate an API Gateway event
test_event = {"queryStringParameters": {"query": "aws lambda function url"}}

# Simulate Lambda context (can be None for basic testing)
test_context = None

print("=" * 60)
print("Testing Lambda Handler Locally")
print("=" * 60)
print(f"Query: {test_event['queryStringParameters']['query']}")
print("=" * 60)

# Call the lambda handler
result = lambda_handler(test_event, test_context)

print("\n" + "=" * 60)
print("RESULT:")
print("=" * 60)
print(f"Status Code: {result['statusCode']}")
print(f"Response Body:\n{result['body']}")
print("=" * 60)
