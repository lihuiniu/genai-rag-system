import requests

def evaluate_online():
    queries = ["what is AML compliance?", "how to file tax?"]
    for q in queries:
        res = requests.post("http://localhost:8000/chat", params={"query": q, "user_id": "user123"})
        print("Query:", q, "Response:", res.json())

if __name__ == "__main__":
    evaluate_online()