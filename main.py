# This locust test script example will simulate a user
# browsing the Locust documentation on https://docs.locust.io

import random

from locust import HttpUser, task

# curl --location "https://api-gateway.miromind.online/serper/search" \
# --header "X-API-KEY: $KEY" \
# --header 'Content-Type: application/json' \
# --data '{"q":"apple inc stock price"}'

# curl --location "https://api-gateway.miromind.online/jina/https://www.example.com" \
# --header "Authorization: Bearer $KEY"


class AwesomeUser(HttpUser):
    host = "https://api-gateway.miromind.online"
