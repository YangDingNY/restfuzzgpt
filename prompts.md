# Prompts

## initPrompt

````
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
````

## tsGenPrompt

```
Now you need to generate a request sequence for a test case.
You should return me a string that includes multiple requests with context, each request being represented by the operationId in the Swagger/OpenAPI document it involves, separated by "->".
Here is an example(The response should not contain any other content except for the following format):
operationA -> operationB -> operationC
```

## reqGenPrompt

```
Now, please construct a specific request for the {reqOrder}th operation "{operationId}" in the previously generated test sequence.
During the construction process, please refer to the Swagger/OpenAPI document I sent you earlier.

**Response Format Requirements**
For the convenience of the later stages, you need to return me the requested content in JSON format.
The JSON format request you return should include fields like operation_id, headers, path_variables, params, form_data, json_data, url and http_method.
Note that the different fields in the request are optional and may not be present for all APIs.
Here is a brief description of each field:

- url: (required) The URL required to send the request.
- http_method: (required) Corresponding HTTP methods for APIs, such as post, get, put, etc.
- operation_id: (required) The operation ID in OpenAPI/Swagger documentation.
- path_variables: (optional) Path variables of the request.
- params: (optional) Data to send in the query string for the request.
- form_data: (optional) Data to send in the body of the request as form-data.
- json_data: (optional) Data to send in the body of the request as json-data.
- headers: (optional) Dictionary of HTTP headers to send with the request.

Here is an example of a JSON format request(The response should not contain any other content except for the following format json data):
{{"url":"http://localhost:8080/blog", "http_method":"post", "params":{{"blogId": 1, "content": "abc"}}, "operation_id":"create_new_blog"}}
Don't give me the result in the form of a code block, just give me a JSON formatted string

**Note**
Afterwards, I will send the request you generated to the service under test, and I will return the corresponding response of the request to you.
When constructing specific requests, you need to consider the corresponding successful responses of previous requests in the sequence.
```

