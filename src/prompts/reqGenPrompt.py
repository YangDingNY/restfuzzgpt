def getMessage(reqOrder, operationId):
    reqGenPrompt = f'''
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

    **Note**
    1. Afterwards, I will send the request you generated to the service under test, and I will return the corresponding response of the request to you.
       When constructing specific requests, you need to consider the corresponding successful responses of previous requests in the sequence.
    2. Don't give me the result in the form of a code block wrapped in backquotes, just give me a JSON formatted string
    '''
    return reqGenPrompt