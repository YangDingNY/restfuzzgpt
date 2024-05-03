def getMessage():
    tsGenPrompt = '''
    Now you need to generate a request sequence for a test case.
    You should return me a string that includes multiple requests with context, each request being represented by the operationId in the Swagger/OpenAPI document it involves, separated by "->".
    Here is an example(The response should not contain any other content except for the following format):
    operationA -> operationB -> operationC  
    '''
    return tsGenPrompt