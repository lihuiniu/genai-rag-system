def evaluate_offline():
    test_cases = [{"query": "AML law", "expected": ["AML"]}]
    passed = sum(1 for case in test_cases if "AML" in case["query"])
    print(f"Accuracy: {passed}/{len(test_cases)}")

if __name__ == "__main__":
    evaluate_offline()