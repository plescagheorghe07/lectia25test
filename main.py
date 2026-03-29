from supabase import create_client, Client

url = "https://erebgboucnhebiijetec.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVyZWJnYm91Y25oZWJpaWpldGVjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ3MzcyOTcsImV4cCI6MjA5MDMxMzI5N30.Uyxy9H7UmQbfHDjrIvSbrfhymiSLn52ab66sW1mKbzE"  # Cheia ta anon/public
supabase: Client = create_client(url, key)


def verify_token(access_token):
    try:
        # Supabase verifică dacă acest JWT (token) este valid și aparține unui user
        response = supabase.auth.get_user(access_token)

        if response.user:
            return True
    except Exception:
        # Dacă token-ul e expirat sau fals, intră aici
        return False

    return False


def get_user_token(email, password):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        # Aici extragi access_token-ul generat pentru această sesiune
        token = response.session.access_token
        print(f"Token-ul tău este: {token}")
        return token
    except Exception as e:
        print(f"Eroare: {e}")
        return None
