from zhipuai import ZhipuAI
import os
import sys
import prompts.initPrompt as initPrompt
import prompts.tsGenPrompt as tsGenPrompt
import prompts.reqGenPrompt as reqGenPrompt
import sendRequests

# init the zhipuAI client
key = os.environ.get('ZHIPUAI_APIKEY')
client = ZhipuAI(api_key = key)

# get the swagger file path
if len(sys.argv) < 2:
    print("Please provide the path of the swagger file.")
    sys.exit(1)
swaggerFilePath = sys.argv[1]
print(f"Swagger File Path: {swaggerFilePath}")

# init the messages
messages = [
    {"role": "user", "content": initPrompt.getInitPrompt(swaggerFilePath)},
    {"role":"assistant","content":"understand"}
]

# Iteratively generate request sequences
testCasesCount = 1
while True:
    print(f"Test Case {testCasesCount}:")
    testCasesCount += 1
    # Step1: generate request sequence
    messages.append({"role":"user","content":tsGenPrompt.getMessage()})
    response = client.chat.completions.create(
        model = "glm-4",
        messages = messages
    )
    ts = response.choices[0].message.content
    messages.append({"role":"assistant","content":ts})
    print(f"Test Sequence: {ts}")
    operationIds = ts.split(" -> ")
    # Step2: construct concrete requests and send them
    for reqOrder,operationId in enumerate(operationIds):
        print(f"    Request {reqOrder+1}: {operationId}")
        messages.append({"role":"user","content":reqGenPrompt.getMessage(reqOrder+1,operationId)})
        response = client.chat.completions.create(
            model = "glm-4",
            messages = messages
        )
        jsonReq = response.choices[0].message.content
        messages.append({"role":"assistant","content":jsonReq})
        print(f"        Request Content: {jsonReq}")
        request_response = sendRequests.send(jsonReq)
        # TODO: generate subsequent requests based on the response instead of sending the response directly
        messages.append({"role":"user","content":request_response})
        print(f"        Response: {request_response}")
