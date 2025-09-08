#!/usr/bin/env python3
"""
Script to run Locust with environment variables
This script demonstrates how to set environment variables and run the stress test
"""

import os
import subprocess
import sys

def set_env_and_run():
    """Set environment variables and run Locust."""
    
    # Check if API_KEY is already set
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        print("API_KEY environment variable not set.")
        print("Please set it using one of these methods:")
        print()
        print("1. Export in terminal:")
        print("   export API_KEY=your_actual_api_key")
        print()
        print("2. Set in .env file (create .env file with API_KEY=your_key)")
        print()
        print("3. Run with inline environment variable:")
        print("   API_KEY=your_key locust -f locustfile.py")
        print()
        
        # Ask user if they want to set it interactively
        user_input = input("Do you want to set API_KEY now? (y/n): ").lower().strip()
        if user_input == 'y':
            api_key = input("Enter your API key: ").strip()
            if api_key:
                os.environ["API_KEY"] = api_key
                print(f"API_KEY set to: {api_key[:8]}...")
            else:
                print("No API key provided. Using default.")
        else:
            print("Using default API key. Warning will be shown in Locust.")
    
    # Run Locust
    print("\nStarting Locust stress test...")
    print("Open http://localhost:8089 in your browser to control the test.")
    print("Press Ctrl+C to stop the test.")
    print()
    
    try:
        # Run locust with the locustfile
        subprocess.run([
            sys.executable, "-m", "locust", 
            "-f", "locustfile.py",
            "--host", os.getenv("HOST", "https://api-gateway.miromind.site")
        ])
    except KeyboardInterrupt:
        print("\nTest stopped by user.")
    except Exception as e:
        print(f"Error running Locust: {e}")

if __name__ == "__main__":
    set_env_and_run()
