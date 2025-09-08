#!/usr/bin/env python3
"""
Debug script to test API endpoints individually
This helps identify why requests are failing
"""

import os
import requests
import json
from query_questions import get_random_question
from jina_web_links import get_random_web_link, extract_domain

def test_api_endpoints():
    """Test both API endpoints to identify issues."""
    
    # Get API key
    api_key = os.getenv("API_KEY", "foobarbaz")
    base_url = "https://api-gateway.miromind.site"
    
    print(f"Testing API endpoints with base URL: {base_url}")
    print(f"Using API key: {api_key[:8]}...")
    print("-" * 60)
    
    # Test 1: Serper Search Endpoint
    print("1. Testing Serper Search Endpoint")
    print("-" * 30)
    
    serper_headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
    }
    
    query = get_random_question()
    payload = {"q": query}
    
    print(f"Query: {query}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    print(f"Headers: {json.dumps(serper_headers, indent=2)}")
    
    try:
        response = requests.post(
            f"{base_url}/serper/search",
            json=payload,
            headers=serper_headers,
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            print("✅ Serper endpoint working!")
            print(f"Response: {response.text[:200]}...")
        else:
            print("❌ Serper endpoint failed!")
            print(f"Error Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Serper endpoint error: {e}")
    
    print("\n" + "=" * 60 + "\n")
    
    # Test 2: Jina Endpoint
    print("2. Testing Jina Endpoint")
    print("-" * 30)
    
    jina_headers = {
        "Authorization": f"Bearer {api_key}",
    }
    
    web_link = get_random_web_link()
    domain = extract_domain(web_link)
    
    print(f"Web Link: {web_link}")
    print(f"Domain: {domain}")
    print(f"Headers: {json.dumps(jina_headers, indent=2)}")
    
    try:
        response = requests.get(
            f"{base_url}/jina/{domain}",
            headers=jina_headers,
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            print("✅ Jina endpoint working!")
            print(f"Response: {response.text[:200]}...")
        else:
            print("❌ Jina endpoint failed!")
            print(f"Error Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Jina endpoint error: {e}")
    
    print("\n" + "=" * 60 + "\n")
    
    # Test 3: Basic connectivity
    print("3. Testing Basic Connectivity")
    print("-" * 30)
    
    try:
        response = requests.get(base_url, timeout=10)
        print(f"Base URL Status: {response.status_code}")
        print(f"Base URL Response: {response.text[:200]}...")
    except Exception as e:
        print(f"❌ Base URL connectivity error: {e}")

if __name__ == "__main__":
    test_api_endpoints()
