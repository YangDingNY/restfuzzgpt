class TestSequence:
    def __init__(self, sequenceID, requests):
        self.sequenceID = sequenceID
        self.requests = requests

    def addRequest(self, request):
        self.requests.append(request)

    def getSequenceString(self):
        sequenceString = ""
        for request in self.requests:
            sequenceString += request
            sequenceString += " -> "
        sequenceString += "end"
        return sequenceString