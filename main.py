import requests

def get_scoresaber_leaderboard(pages=1):
    # Base URL for the ScoreSaber API
    base_url = "https://scoresaber.com/api/players?page={}"
    
    # Loop through the desired number of pages
    for page in range(1, pages + 1):
        # Construct the URL for the current page
        url = base_url.format(page)
        
        # Make the GET request to the ScoreSaber API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Print the leaderboard data for the current page
            print(f"--- Page {page} ---")
            for player in data['players']:
                print(f"Rank: {player['rank']}, Name: {player['name']}, Country: {player['country']}, PP: {player['pp']}")
        else:
            print(f"Failed to retrieve data for page {page}: {response.status_code}")

if __name__ == "__main__":
    # Specify the number of pages you want to retrieve
    number_of_pages = 25
    get_scoresaber_leaderboard(pages=number_of_pages)