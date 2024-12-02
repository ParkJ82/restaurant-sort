import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)
base_url = "https://map.naver.com/p/entry/place/"



reponse = (supabase.table("restaurants").upsert({
                    "name": "hi", 
                    "rating": 3.0, 
                    "category": "hi", 
                    "address": "hi", 
                    "url":"hi"
                }, on_conflict="url").execute())

