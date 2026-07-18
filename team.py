import requests
import json
import time
import os


API_KEY = ""
SEASON = 2024
MAX_COUNTRIES = 15  # Το όριο  15 χώρες γιati einai tzampa
DELAY_BETWEEN_REQUESTS = 7

HEADERS = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "v3.football.api-sports.io"
}

# Μνήμη για να μην ρωτάμε το OpenStreetMap για την ίδια πόλη 2 φορές
CITY_CACHE = {}



def get_city_coordinates(city, country):
    """
    Βρίσκει τις συντεταγμένες της πόλης OpenStreetMap API.
    """
    if not city or not country:
        return None, None

    cache_key = f"{city}_{country}".lower()

    
    if cache_key in CITY_CACHE:
        return CITY_CACHE[cache_key]

    url = f"https://nominatim.openstreetmap.org/search?city={city}&country={country}&format=json"


    headers = {"User-Agent": "FootballGlobeProject/1.0"}

    try:
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            if len(data) > 0:
                lat = float(data[0]['lat'])
                lng = float(data[0]['lon'])
                CITY_CACHE[cache_key] = (lat, lng)

                # Αναμονή 1.2s γιατί το Nominatim έχει όριο 1 request / δευτερόλεπτο....γιατί τα βρήκα σκούρα
                time.sleep(1.2)
                return lat, lng
    except Exception:
        pass

    return None, None


def get_trophies_data(team_name):
    if "AEK" in team_name:
        return " 13x Πρωταθλήματα, 16x Κύπελλα"
    return ""


def get_jersey_local_path(team_id):
    return f"assets/jerseys/team_{team_id}.png"


def get_first_division_leagues():
    print("-> Αναζήτηση όλων των πρωταθλημάτων παγκοσμίως...")
    url = "https://v3.football.api-sports.io/leagues"

    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 429:
            print("[!] Rate Limit κατά την αναζήτηση πρωταθλημάτων.")
            return []

        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Σφάλμα σύνδεσης στο API: {e}")
        return []

    if not data or 'response' not in data:
        return []

    country_to_league = {}

    for item in data['response']:
        country = item['country']['name']
        league = item['league']

        if league['type'] == 'League':
            if country not in country_to_league:
                country_to_league[country] = league['id']
            else:
                if league['id'] < country_to_league[country]:
                    country_to_league[country] = league['id']

    all_leagues = list(country_to_league.values())
    return all_leagues[:MAX_COUNTRIES]



def build_teams_data():
    all_league_ids = get_first_division_leagues()

    if not all_league_ids:
        print("-> Η διαδικασία ακυρώθηκε.")
        return []

    print(f"-> Βρέθηκαν {len(all_league_ids)} χώρες. Ξεκινάει η λήψη ομάδων και η γεωεντοπισμός...\n")

    all_teams = []

    for idx, league_id in enumerate(all_league_ids):
        print(f"[{idx + 1}/{len(all_league_ids)}] Αντλούνται ομάδες για League ID: {league_id}...")
        url = f"https://v3.football.api-sports.io/teams?league={league_id}&season={SEASON}"

        try:
            response = requests.get(url, headers=HEADERS)

            if response.status_code == 429:
                print("\n[!] Πιάσαμε το όριο του API (HTTP 429). Διακοπή λούπας.")
                break

            response.raise_for_status()
            data = response.json()

            if 'errors' in data and data['errors']:
                print(f"[!] API Error: {data['errors']}")
                continue

            teams_added = 0
            for item in data.get('response', []):
                team = item['team']
                venue = item['venue']

                team_name = team['name']
                country = team['country']
                city = venue.get('city', 'Unknown')
                stadium = venue.get('name', 'Unknown Stadium')

           
                lat, lng = get_city_coordinates(city, country)

                if lat is None or lng is None:
                    continue

                team_id_str = str(team['id'])

                team_data = {
                    "id": team_id_str,
                    "team_name": team_name,
                    "country": country,
                    "city": city,
                    "stadium": stadium,
                    "league": f"League {league_id}",
                    "lat": float(lat),
                    "lng": float(lng),
                    "founded": team.get('founded', '-'),
                    "logo_url": team.get('logo', ''),
                    "trophies": get_trophies_data(team_name),
                    "jersey_url": get_jersey_local_path(team_id_str)
                }
                all_teams.append(team_data)
                teams_added += 1

            print(f"   -> Εντοπίστηκαν στο χάρτη και προστέθηκαν {teams_added} ομάδες.")

         
            time.sleep(DELAY_BETWEEN_REQUESTS)

        except Exception as e:
            print(f"[!] Σφάλμα στο league {league_id}: {e}")

    return all_teams



if __name__ == "__main__":
    start_time = time.time()

    final_list = build_teams_data()

    if len(final_list) > 0:
        output_file = 'teams.json'

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(final_list, f, ensure_ascii=False, indent=4)

        execution_time = round(time.time() - start_time, 2)
        print(f"\n[✓] ΕΠΙΤΥΧΙΑ! Αποθηκεύτηκαν {len(final_list)} ομάδες στο '{output_file}'.")
        print(f"[i] Χρόνος εκτέλεσης: {execution_time} δευτερόλεπτα.")
    else:
        print("\n[x] Δεν βρέθηκαν δεδομένα για αποθήκευση.")
