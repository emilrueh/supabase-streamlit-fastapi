from dotenv import load_dotenv
import os


load_dotenv()


server = os.getenv("SERVER_URL")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")
