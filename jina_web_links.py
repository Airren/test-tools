"""
Real web links for Jina API testing
Contains 128 diverse, real websites for comprehensive web scraping testing
"""

import random

# 128 real web links for Jina API testing
JINA_WEB_LINKS = [
    # Technology & Programming (20 links)
    "https://github.com",
    "https://stackoverflow.com",
    "https://developer.mozilla.org",
    "https://docs.python.org",
    "https://nodejs.org",
    "https://reactjs.org",
    "https://vuejs.org",
    "https://angular.io",
    "https://www.docker.com",
    "https://kubernetes.io",
    "https://aws.amazon.com",
    "https://cloud.google.com",
    "https://azure.microsoft.com",
    "https://www.postgresql.org",
    "https://www.mongodb.com",
    "https://redis.io",
    "https://www.elastic.co",
    "https://kafka.apache.org",
    "https://www.nginx.com",
    "https://www.rabbitmq.com",
    
    # News & Media (20 links)
    "https://www.bbc.com",
    "https://www.cnn.com",
    "https://www.reuters.com",
    "https://www.theguardian.com",
    "https://www.nytimes.com",
    "https://www.washingtonpost.com",
    "https://www.wsj.com",
    "https://www.bloomberg.com",
    "https://techcrunch.com",
    "https://www.theverge.com",
    "https://arstechnica.com",
    "https://www.wired.com",
    "https://www.engadget.com",
    "https://mashable.com",
    "https://www.cnet.com",
    "https://www.pcmag.com",
    "https://www.zdnet.com",
    "https://venturebeat.com",
    "https://www.fastcompany.com",
    "https://www.forbes.com",
    
    # E-commerce & Shopping (15 links)
    "https://www.amazon.com",
    "https://www.ebay.com",
    "https://www.alibaba.com",
    "https://www.shopify.com",
    "https://www.walmart.com",
    "https://www.target.com",
    "https://www.bestbuy.com",
    "https://www.homedepot.com",
    "https://www.lowes.com",
    "https://www.costco.com",
    "https://www.macys.com",
    "https://www.nordstrom.com",
    "https://www.zappos.com",
    "https://www.etsy.com",
    "https://www.wayfair.com",
    
    # Social Media & Communication (15 links)
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.youtube.com",
    "https://www.tiktok.com",
    "https://www.snapchat.com",
    "https://www.pinterest.com",
    "https://www.reddit.com",
    "https://www.discord.com",
    "https://www.slack.com",
    "https://www.zoom.us",
    "https://www.skype.com",
    "https://www.telegram.org",
    "https://www.whatsapp.com",
    
    # Education & Learning (15 links)
    "https://www.coursera.org",
    "https://www.edx.org",
    "https://www.udemy.com",
    "https://www.khanacademy.org",
    "https://www.codecademy.com",
    "https://www.freecodecamp.org",
    "https://www.w3schools.com",
    "https://www.tutorialspoint.com",
    "https://www.udacity.com",
    "https://www.pluralsight.com",
    "https://www.lynda.com",
    "https://www.skillshare.com",
    "https://www.masterclass.com",
    "https://www.britannica.com",
    "https://www.wikipedia.org",
    
    # Finance & Business (15 links)
    "https://www.yahoo.com/finance",
    "https://finance.yahoo.com",
    "https://www.marketwatch.com",
    "https://www.investing.com",
    "https://www.nasdaq.com",
    "https://www.fool.com",
    "https://www.seekingalpha.com",
    "https://www.benzinga.com",
    "https://www.zerohedge.com",
    "https://www.cnbc.com",
    "https://www.businessinsider.com",
    "https://www.entrepreneur.com",
    "https://www.inc.com",
    "https://www.hbr.org",
    "https://www.mckinsey.com",
    
    # Travel & Tourism (10 links)
    "https://www.booking.com",
    "https://www.expedia.com",
    "https://www.airbnb.com",
    "https://www.tripadvisor.com",
    "https://www.kayak.com",
    "https://www.skyscanner.com",
    "https://www.lonelyplanet.com",
    "https://www.nationalgeographic.com",
    "https://www.travelocity.com",
    "https://www.orbitz.com",
    
    # Health & Wellness (8 links)
    "https://www.webmd.com",
    "https://www.mayoclinic.org",
    "https://www.healthline.com",
    "https://www.medlineplus.gov",
    "https://www.cdc.gov",
    "https://www.who.int",
    "https://www.nih.gov",
    "https://www.clevelandclinic.org",
    
    # Entertainment & Sports (10 links)
    "https://www.netflix.com",
    "https://www.hulu.com",
    "https://www.disney.com",
    "https://www.espn.com",
    "https://www.nfl.com",
    "https://www.nba.com",
    "https://www.mlb.com",
    "https://www.fifa.com",
    "https://www.spotify.com",
    "https://www.twitch.tv",
]

# Function to get a random web link
def get_random_web_link():
    """Return a random web link from the list."""
    return random.choice(JINA_WEB_LINKS)

# Function to get multiple random web links
def get_random_web_links(count=10):
    """Return a list of random web links."""
    return random.sample(JINA_WEB_LINKS, min(count, len(JINA_WEB_LINKS)))

# Function to get web links by category (if needed for future expansion)
def get_web_links_by_category(category=None):
    """Return web links filtered by category (placeholder for future use)."""
    # This can be expanded to categorize links if needed
    return JINA_WEB_LINKS

# Function to extract domain from URL
def extract_domain(url):
    """Extract domain from URL for Jina API testing."""
    from urllib.parse import urlparse
    parsed = urlparse(url)
    return parsed.netloc

# Function to get random domains
def get_random_domains(count=10):
    """Return a list of random domains extracted from web links."""
    domains = [extract_domain(link) for link in JINA_WEB_LINKS]
    return random.sample(domains, min(count, len(domains)))

if __name__ == "__main__":
    # Test the functions
    print(f"Total web links: {len(JINA_WEB_LINKS)}")
    print(f"Random web link: {get_random_web_link()}")
    print(f"Random domain: {extract_domain(get_random_web_link())}")
    print(f"First 5 web links: {JINA_WEB_LINKS[:5]}")
    print(f"Sample domains: {get_random_domains(5)}")
