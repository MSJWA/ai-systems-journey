from week3_llm_agents.langgraph_agent import app
from langchain_core.messages import HumanMessage

test_cases = [
    {
        "question": "Can you find Ali's info?",
        "expected_contains": "21"
    },
    {
        "question": "What is 15 plus 27?",
        "expected_contains": "42"
    },
    {
        "question": "What's the capital of Japan?",
        "expected_contains": "Tokyo"
    },
    {
        "question": "Find info for someone named Zzzznotreal",
        "expected_contains": "not found"
    }
]

def run_eval(test_cases, app):
    passed = 0
    failed = 0

    for case in test_cases:
        result = app.invoke({"messages": [HumanMessage(content=case["question"])]})
        response_text = result["messages"][-1].content

        if case["expected_contains"] in response_text:
            print(f"PASS: {case['question']}")
            passed += 1
        else:
            print(f"FAIL: {case['question']} -> got: {response_text}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed out of {len(test_cases)}")

if __name__ == "__main__":
    run_eval(test_cases, app)