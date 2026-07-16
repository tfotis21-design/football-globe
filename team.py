import urllib.request
import csv
import json
import ssl

# για οταν τρωει ακυρα 
ssl._create_default_https_context = ssl._create_unverified_context

GREEK_TEAMS = [
    # aekara prwth ennoeitai
    {
        "id": "aek_athens", "team_name": "AEK Athens", "country": "Greece", "city": "Athens", 
        "stadium": "OPAP Arena", "league": "Super League 1", "lat": 38.0361, "lng": 23.7431, 
        "trophies": "🏆 13x Πρωταθλήματα, 16x Κύπελλα", "jersey_url": "aek.png"
    },
    {
        "id": "panathinaikos", "team_name": "Panathinaikos", "country": "Greece", "city": "Athens",
        "stadium": "Apostolos Nikolaidis", "league": "Super League 1", "lat": 37.9873, "lng": 23.7544,
        "trophies": "🏆 20x Πρωταθλήματα", "jersey_url": "pao.png"
    },
    {
        "id": "olympiacos", "team_name": "Olympiacos", "country": "Greece", "city": "Piraeus",
        "stadium": "Karaiskakis Stadium", "league": "Super League 1", "lat": 37.9465, "lng": 23.6644,
        "trophies": "🏆 47x Πρωταθλήματα", "jersey_url": "oly.png"
    },
    {
        "id": "paok", "team_name": "PAOK", "country": "Greece", "city": "Thessaloniki", "stadium": "Toumba Stadium",
        "league": "Super League 1", "lat": 40.6136, "lng": 22.9723, "trophies": "🏆 4x Πρωταθλήματα",
        "jersey_url": "paok.png"
    }
]

def build_teams_data():
    print("ksekinaei to download tou csv apo github...")
    url = "https://raw.githubusercontent.com/jokecamp/FootballData/master/other/stadiums-with-GPS-coordinates.csv"
    
    # xwnoume prwta tis dikes mas omades sth lista
    data = list(GREEK_TEAMS)
    
    try:
        req = urllib.request.urlopen(url)
        # to kanoume decode giati katevainei se bytes
        decoded = [line.decode('utf-8') for line in req.readlines()]
        reader = csv.DictReader(decoded)
        
        count = 0
        for row in reader:
            name = row.get("Team", "").strip()
            
            # skip an leipei to onoma h an thn exoume hdh sth lista (px PAO, AEK klp)
            if not name or any(t['team_name'] == name for t in data):
                continue

            lat = row.get("Latitude", "").strip()
            lng = row.get("Longitude", "").strip()

            if not lat or not lng:
                continue

            # ftiaxnoume ena id tis prokopis
            t_id = name.lower().replace(" ", "_").replace("fc", "").replace(".", "").strip()

            data.append({
                "id": t_id,
                "team_name": name,
                "country": row.get("Country", "").strip(),
                "city": row.get("City", "").strip(),
                "stadium": row.get("Stadium", "").strip(),
                "league": "First Division", # hardcoded giati den yparxei sto csv
                "lat": float(lat),
                "lng": float(lng),
                "trophies": "",
                "jersey_url": f"assets/jerseys/{t_id}.png"
            })
            count += 1
            
        print(f"mphkan alles {count} omades apo to csv.")
        return data
        
    except Exception as e:
        print("skalwse to download:", e)
        return data # an faei fail gurnaei toulaxiston ta dika mas

if __name__ == "__main__":
    final_list = build_teams_data()
    
    # swsimo arxeiou
    with open('teams.json', 'w', encoding='utf-8') as f:
        json.dump(final_list, f, ensure_ascii=False, indent=4)
        
    print(f"etoimo! swthhkan {len(final_list)} omades sto teams.json.")
