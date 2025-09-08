import os
import random

from locust import HttpUser, constant_throughput, task
from query_questions import SERPER_QUERY_QUESTIONS, get_random_question
from jina_web_links import get_random_web_link, extract_domain


class APIUser(HttpUser):
    # Target 100 QPS total across all users
    # With task weights 2:1 (search:jina), we get ~67 search + ~33 jina requests per second
    # Each user should execute 1 task per second to achieve 100 QPS with 100 users
    wait_time = constant_throughput(1)

    def on_start(self):
        """Initialize the user with required headers."""
        # Get API key from environment variable
        self.api_key = os.getenv("API_KEY", "foobarbaz")
        
        if self.api_key == "foobarbaz":
            print("Warning: Using default API key. Please set API_KEY environment variable.")
        
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
        query = get_random_question()
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
        # Get a random web link and extract domain
        domain = get_random_web_link()

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
