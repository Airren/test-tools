import random

from locust import HttpUser, constant_throughput, task

# Sample queries for the search endpoint
SEARCH_QUERIES_PREFIX = [
    "apple inc stock price",
    "tesla market cap",
    "bitcoin price",
    "amazon revenue 2023",
    "microsoft cloud services",
    "google ai developments",
    "meta quarterly earnings",
    "nvidia gpu demand",
]

SEARCH_QUERIES_SUFFIX = [
    "stock price",
    "market cap",
    "revenue",
    "earnings",
    "gpu demand",
    "ai research",
    "quantum computing",
    "blockchain technology",
    "cryptocurrency market",
    "space exploration",
    "deep learning",
    "machine learning",
]

SEARCH_QUERIES = [
    f"{prefix} {suffix}"
    for prefix in SEARCH_QUERIES_PREFIX
    for suffix in SEARCH_QUERIES_SUFFIX
]

# Sample domains for the Jina endpoint
TARGET_DOMAINS = [
    "www.example.com",
    "www.google.com",
    "www.github.com",
    "www.microsoft.com",
    "www.amazon.com",
    "www.apple.com",
    "news.ycombinator.com",
    "www.reddit.com",
]


class APIUser(HttpUser):
    # Target 100 QPS total across all users
    # With task weights 2:1 (search:jina), we get ~67 search + ~33 jina requests per second
    # Each user should execute 1 task per second to achieve 100 QPS with 100 users
    wait_time = constant_throughput(1)

    def on_start(self):
        """Initialize the user with required headers."""
        # Replace with your actual API key
        self.api_key = "foobarbaz"
        self.serper_headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
        }
        self.jina_headers = {
            "Authorization": f"Bearer {self.api_key}",
        }

    @task(2)  # Weight of 2 means this task runs twice as often
    def test_search_endpoint(self):
        """Test the Serper search endpoint with random queries."""
        query = random.choice(SEARCH_QUERIES)
        payload = {"q": query}

        with self.client.post(
            "/serper/search",
            json=payload,
            headers=self.serper_headers,
            name="/serper/search",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(
                    f"Search failed with status code: {response.status_code}"
                )

    @task(1)  # Weight of 1 means this task runs at normal frequency
    def test_jina_endpoint(self):
        """Test the Jina endpoint with random domains."""
        domain = random.choice(TARGET_DOMAINS)

        with self.client.get(
            f"/jina/{domain}",
            headers=self.jina_headers,
            name="/jina/{domain}",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(
                    f"Jina request failed with status code: {response.status_code}"
                )
