"""
Query questions for Serper API testing
Contains 128 diverse questions for comprehensive search testing
"""
import random

# 128 questions for Serper API testing
SERPER_QUERY_QUESTIONS = [
    # Technology & AI (20 questions)
    "What is artificial intelligence and how does it work?",
    "How to implement machine learning algorithms in Python?",
    "What are the latest developments in ChatGPT and OpenAI?",
    "How does blockchain technology work?",
    "What is quantum computing and its applications?",
    "How to build a REST API with FastAPI?",
    "What are microservices architecture best practices?",
    "How to deploy applications using Docker containers?",
    "What is Kubernetes and how to use it?",
    "How to implement CI/CD pipelines with GitHub Actions?",
    "What are the differences between SQL and NoSQL databases?",
    "How to optimize database performance?",
    "What is cloud computing and AWS services?",
    "How to implement authentication with JWT tokens?",
    "What are the best practices for API security?",
    "How to build real-time applications with WebSockets?",
    "What is GraphQL and how does it compare to REST?",
    "How to implement caching strategies?",
    "What are the latest trends in web development?",
    "How to build scalable applications?",
    
    # Business & Finance (20 questions)
    "What is the current stock market performance?",
    "How to start a successful startup business?",
    "What are the best investment strategies for 2024?",
    "How to analyze financial statements?",
    "What is cryptocurrency and how to invest in it?",
    "How to create a business plan?",
    "What are the latest trends in e-commerce?",
    "How to implement digital marketing strategies?",
    "What is venture capital and how to raise funding?",
    "How to manage cash flow in small businesses?",
    "What are the benefits of remote work?",
    "How to build a strong company culture?",
    "What is supply chain management?",
    "How to implement agile project management?",
    "What are the latest developments in fintech?",
    "How to conduct market research?",
    "What is customer relationship management?",
    "How to optimize business processes?",
    "What are the challenges of global business?",
    "How to implement sustainable business practices?",
    
    # Health & Science (20 questions)
    "What are the benefits of regular exercise?",
    "How to maintain a healthy diet?",
    "What is the latest research on COVID-19 vaccines?",
    "How to manage stress and anxiety?",
    "What are the effects of sleep on health?",
    "How to prevent heart disease?",
    "What is the importance of mental health?",
    "How to build strong immune system?",
    "What are the latest cancer treatment options?",
    "How to maintain healthy skin?",
    "What is the role of genetics in health?",
    "How to manage chronic diseases?",
    "What are the benefits of meditation?",
    "How to improve memory and cognitive function?",
    "What is the impact of pollution on health?",
    "How to maintain healthy relationships?",
    "What are the latest developments in medical technology?",
    "How to prevent diabetes?",
    "What is the importance of hydration?",
    "How to build healthy habits?",
    
    # Education & Learning (20 questions)
    "How to learn programming effectively?",
    "What are the best online learning platforms?",
    "How to improve reading comprehension?",
    "What is the importance of lifelong learning?",
    "How to develop critical thinking skills?",
    "What are effective study techniques?",
    "How to learn a new language quickly?",
    "What is the future of education?",
    "How to prepare for job interviews?",
    "What are the benefits of online education?",
    "How to develop leadership skills?",
    "What is the importance of soft skills?",
    "How to build a professional network?",
    "What are the latest trends in educational technology?",
    "How to improve public speaking skills?",
    "What is the importance of creativity in learning?",
    "How to manage time effectively?",
    "What are the benefits of mentorship?",
    "How to develop problem-solving skills?",
    "What is the importance of continuous improvement?",
    
    # Travel & Lifestyle (20 questions)
    "What are the best travel destinations for 2024?",
    "How to plan a budget-friendly vacation?",
    "What are the essential travel tips?",
    "How to travel sustainably?",
    "What are the best travel apps?",
    "How to overcome travel anxiety?",
    "What are the benefits of solo travel?",
    "How to pack efficiently for travel?",
    "What are the latest travel trends?",
    "How to find cheap flights?",
    "What are the best travel insurance options?",
    "How to stay healthy while traveling?",
    "What are the cultural etiquette tips for travelers?",
    "How to document travel experiences?",
    "What are the benefits of slow travel?",
    "How to travel with children?",
    "What are the best travel photography tips?",
    "How to plan a road trip?",
    "What are the benefits of travel rewards programs?",
    "How to deal with travel delays and cancellations?",
    
    # Environment & Sustainability (20 questions)
    "What are the effects of climate change?",
    "How to reduce carbon footprint?",
    "What are renewable energy sources?",
    "How to implement sustainable living practices?",
    "What is the importance of biodiversity?",
    "How to reduce plastic waste?",
    "What are the benefits of electric vehicles?",
    "How to conserve water at home?",
    "What is the impact of deforestation?",
    "How to support environmental conservation?",
    "What are the benefits of solar energy?",
    "How to reduce food waste?",
    "What is the importance of recycling?",
    "How to create a sustainable garden?",
    "What are the effects of air pollution?",
    "How to support clean energy initiatives?",
    "What is the importance of ocean conservation?",
    "How to reduce energy consumption?",
    "What are the benefits of green building?",
    "How to promote environmental awareness?",
    
    # Entertainment & Culture (8 questions)
    "What are the best movies of 2024?",
    "How to discover new music?",
    "What are the latest trends in gaming?",
    "How to appreciate different art forms?",
    "What are the benefits of reading books?",
    "How to develop creative hobbies?",
    "What is the importance of cultural diversity?",
    "How to support local artists and creators?",
]

# Function to get a random question
def get_random_question():
    """Return a random question from the list."""
    return random.choice(SERPER_QUERY_QUESTIONS)

# Function to get multiple random questions
def get_random_questions(count=10):
    """Return a list of random questions."""
    return random.sample(SERPER_QUERY_QUESTIONS, min(count, len(SERPER_QUERY_QUESTIONS)))

# Function to get questions by category (if needed for future expansion)
def get_questions_by_category(category=None):
    """Return questions filtered by category (placeholder for future use)."""
    # This can be expanded to categorize questions if needed
    return SERPER_QUERY_QUESTIONS

if __name__ == "__main__":
    # Test the functions
    print(f"Total questions: {len(SERPER_QUERY_QUESTIONS)}")
    print(f"Random question: {get_random_question()}")
    print(f"First 5 questions: {SERPER_QUERY_QUESTIONS[:5]}")
