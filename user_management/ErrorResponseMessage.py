# To get all type of standard response

# creating respons with response code& response message
def createRC_RM(code, msg):
    resp = "{\"responseCode\" : \"" + code + "\", \"responseMessage\" :\"" + msg+ "\"}"
    return resp