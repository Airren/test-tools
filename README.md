# API Load Testing with Locust

This project contains Locust load testing scripts for testing two API endpoints:
1. Serper Search API
2. Jina API

## Setup

1. Install dependencies:
```bash
pip install -e .
```

2. Configure your API key:
Edit `locustfile.py` and replace `YOUR_API_KEY` with your actual API key.

## Running the Tests

### Using Web UI

1. Start Locust with the web interface:
```bash
locust
```

2. Open http://localhost:8089 in your browser

3. Configure your test:
   - Host: https://api-gateway.miromind.online
   - Number of users
   - Spawn rate
   - Click "Start swarming"

### Command Line Mode

To run without the web UI:
```bash
locust --headless -H https://api-gateway.miromind.online -u 10 -r 1 --run-time 1m
```

**For 100 QPS stress testing:**
```bash
locust --headless -H https://api-gateway.miromind.online -u 100 -r 10 --run-time 5m
```

Where:
- `-u 100`: Simulates 100 users (each user executes 1 task per second = 100 QPS total)
- `-r 10`: Spawn rate of 10 users per second (reaches full load in 10 seconds)
- `--run-time 5m`: Run for 5 minutes

**Note:** The locustfile uses `constant_throughput(1)` which ensures each user executes exactly 1 task per second, achieving the target 100 QPS with 100 users.

## Test Scenarios

The load test simulates two types of requests at 100 QPS:

1. Search Queries (`/serper/search`):
   - Makes POST requests with random search queries (combinations of prefixes and suffixes)
   - Runs twice as frequently as the Jina endpoint tests (~67 QPS)
   - Validates response status codes

2. Jina Requests (`/jina/{domain}`):
   - Makes GET requests with random domain names
   - Runs at normal frequency (~33 QPS)
   - Validates response status codes

**Throughput Distribution:**
- With task weights 2:1 (search:jina) and 100 total QPS:
  - Search endpoint: ~67 requests per second
  - Jina endpoint: ~33 requests per second

## Customization

You can modify the test scenarios by:
1. Adding more search queries to `SEARCH_QUERIES` list
2. Adding more domains to `TARGET_DOMAINS` list
3. Adjusting the task weights (currently 2:1 ratio)
4. Modifying the wait time between requests (currently 1-5 seconds)
