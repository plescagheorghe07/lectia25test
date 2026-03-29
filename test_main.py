from main import get_user_token, verify_token
token = ""
def test_get_token():
    global token
    token = get_user_token("jora@cacta.md", "joracacta")
    return token != None

def test_valid_token():
    global token
    return verify_token(token)