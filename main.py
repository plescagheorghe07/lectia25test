import supabase
def sign_in(email, password):
    response = supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password,
        }
    )
    if( response.ok ):
        return True

    return False