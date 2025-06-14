#!/usr/bin/env python3
import json
import urllib.request

chat_url = "http://localhost:5001/v1/chat/completions"

llm_msg = ""
usr_msg = ""

print(usr_msg)
print("-" * 50)

for turn in range(20):
    # Prepare request payload
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": usr_msg},
                     {"role": "assistent", "content": llm_msg}]
    }
    data = json.dumps(payload).encode('utf-8')

    # Create and send request
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(chat_url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            response_data = json.loads(response.read().decode('utf-8'))

            # Extract message content from response
            if "choices" in response_data and len(response_data["choices"]) > 0:
                next_message = response_data["choices"][0]["message"]["content"]
            else:
                print(f"Error: Invalid response structure from server")
                break

            print(next_message)
            print("-" * 50)

            llm_msg,usr_msg = usr_msg,next_message

    except Exception as e:
        print(f"Request to server failed: {str(e)}")
        break
