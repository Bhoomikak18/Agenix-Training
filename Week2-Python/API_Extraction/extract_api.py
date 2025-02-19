import requests
from api_config import API_URL
from database import Database, DB_CONFIG  

class CatFactFetcher:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_cat_fact(self):
        #Fetching a fact from the API
        try:
            response = requests.get(self.api_url)

            # Debugging prints for better clarity
            print("Response Status Code:", response.status_code)
            print("Response Content:", response.text)

            if response.status_code == 200:
                data = response.json()
                fact = data.get("fact")
                if fact:
                    return fact
                else:
                    print("No 'fact' key found in API response.")
                    return None
            else:
                print("Failed to fetch data. Status code:", response.status_code)
                return None
        except Exception as e:
            print("Error fetching data:", e)
            return None

class App:
    def __init__(self, db_config, api_url):
        self.db = Database(db_config)  
        self.api_fetcher = CatFactFetcher(api_url)
         
    def run(self):
        self.db.create_table()  
        fact = self.api_fetcher.fetch_cat_fact()
        if fact:
            fact_length = len(fact)
            print("Fetched Cat Fact:", fact)
            print("Length of Fact:", fact_length)
            self.db.store_fact(fact, fact_length)  # Store 
        else:
            print("No fact fetched.")

if __name__ == "__main__":
    app = App(DB_CONFIG , API_URL)
    app.run()
