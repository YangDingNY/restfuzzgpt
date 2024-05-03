from zhipuai import ZhipuAI
import os

# init the zhipuAI client
key = os.environ.get('ZHIPUAI_APIKEY')
client = ZhipuAI(api_key = key)

swagger_file = open("E:\\y1\\api test\\code\\requests-send\\swagger_blog.txt")
swagger_doc = swagger_file.read()

initPrompt = f'''
As a software test developer, your task is to write a test case based on the following swagger/OpenAPI document delimited by triple backticks.
```
{swagger_doc}
```

**Knowledge about REST API Testing**
The specific form of a test case for testing a REST API is to send a series of HTTP requests(test sequence), where the last request involves the target test interface for this test, and the previous requests are all prepared for this request.
There should be a correlation between requests in a test case, such as the previous request creating a required resource for subsequent requests, and the previous request generating a parent resource to prepare for the creation of subsequent child resources.

**Steps for Designing a Test Case**
You should follow these two steps to create a test case:
1. Design a request sequence, where the last request in the sequence involves the interface under test, and the previous requests are necessary prerequisite requests for testing the interface under test;
2. According to the specifications in the Swagger/OpenAPI document, design specific JSON format request for each request in the request sequence.

**Generate Requirements**
1. The test cases you generate should trigger 20X or 50X status codes as much as possible, rather than 40X status codes. Minimize the number of bad requests in test cases as much as possible. 
2. Do not include any explanation or description in your response, except for the required output content.

After understanding the above information, you need to reply to me "understand", and then I will give you further instructions.
'''

tsGenPrompt = '''
Now you need to generate a request sequence for a test case.
You should return me a string that includes multiple requests with context, each request being represented by the operationId in the Swagger/OpenAPI document it involves, separated by "->".
Here is an example(The response should not contain any other content except for the following format):
operationA -> operationB -> operationC
'''

response = client.chat.completions.create(
    model = "glm-4",
    messages = [
        {"role": "user", "content": initPrompt},
        {"role":"assistant","content":"understand"},
        {"role":"user","content":tsGenPrompt}
    ]
)

answer = response.choices[0].message.content
operationIds = answer.split(" -> ")

for operationId in operationIds:
    print(operationId)