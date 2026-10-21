# Task 9: Intelligent Chatbot using Python
import re

def chatbot_reply(msg, memory):
    msg = msg.lower()
    if any(w in msg for w in ["hi", "hello"]): 
        return f"Hello {memory.get('name', '')}! How can I help you?".strip()
    if m := re.search(r"(?:name is|i am)\s+([a-zA-Z]+)", msg):
        memory['name'] = m.group(1).capitalize()
        return f"Nice to meet you, {memory['name']}!"
    if m := re.search(r"(\d+)\s*([\+\-\*])\s*(\d+)", msg):
        a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
        return f"Result: {a + b if op == '+' else a - b if op == '-' else a * b}"
    if "ai" in msg:
        return "AI stands for Artificial Intelligence: machines simulating human intelligence."
    if "bye" in msg: 
        return "Goodbye! Have a great day!"
    return "I can answer questions on AI or do basic math."

memory = {}
for u in ["Hello", "My name is Alice", "What is AI?", "Calculate 12 * 8", "Bye"]:
    print(f"User: {u} -> Bot: {chatbot_reply(u, memory)}")

# Output:
# User: Hello -> Bot: Hello! How can I help you?
# User: My name is Alice -> Bot: Nice to meet you, Alice!
# User: What is AI? -> Bot: AI stands for Artificial Intelligence: machines simulating human intelligence.
# User: Calculate 12 * 8 -> Bot: Result: 96
# User: Bye -> Bot: Goodbye! Have a great day!
