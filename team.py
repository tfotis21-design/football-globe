import urllib.request
import csv
import json
import ssl

# Παράκαμψη του ελέγχου SSL
ssl._create_default_https_context = ssl._create_unverified_context


def fetch_teams_from_github():
    print("🌍 Κατεβάζουμε δεδομένα από το GitHub (Open Source Dataset)...")

    # Το επίσημο URL του CSV με τις ευρωπαϊκές ομάδες
    url = "https://raw.githubusercontent.com/jokecamp/FootballData/master/other/stadiums-with-GPS-coordinates.csv"

    # Οι δικές σου ελληνικές ομάδες που θέλουμε να διατηρηθούν ακριβώς όπως τις είχες
    greek_teams = [
        {"id": "aek_athens", "team_name": "AEK Athens", "country": "Greece", "city": "Athens", "stadium": "OPAP Arena",
         "league": "Super League 1", "lat": 38.0361, "lng": 23.7431, "trophies": "🏆 13x Πρωταθλήματα, 16x Κύπελλα",
         "jersey_url": "aek.png"},
        {"id": "panathinaikos", "team_name": "Panathinaikos", "country": "Greece", "city": "Athens",
         "stadium": "Apostolos Nikolaidis", "league": "Super League 1", "lat": 37.9873, "lng": 23.7544,
         "trophies": "🏆 20x Πρωταθλήματα", "jersey_url": "pao.png"},
        {"id": "olympiacos", "team_name": "Olympiacos", "country": "Greece", "city": "Piraeus",
         "stadium": "Karaiskakis Stadium", "league": "Super League 1", "lat": 37.9465, "lng": 23.6644,
         "trophies": "🏆 47x Πρωταθλήματα", "jersey_url": "oly.png"},
        {"id": "paok", "team_name": "PAOK", "country": "Greece", "city": "Thessaloniki", "stadium": "Toumba Stadium",
         "league": "Super League 1", "lat": 40.6136, "lng": 22.9723, "trophies": "🏆 4x Πρωταθλήματα",
         "jersey_url": "paok.png"}
    ]

    teams_data = []
    # Προσθέτουμε πρώτα τις δικές σου
    teams_data.extend(greek_teams)

    try:
        # Διαβάζουμε το αρχείο κατευθείαν από το internet
        response = urllib.request.urlopen(url)
        lines = [l.decode('utf-8') for l in response.readlines()]
        reader = csv.DictReader(lines)

        for row in reader:
            team_name = row.get("Team", "").strip()
            if not team_name:
                continue

            country = row.get("Country", "").strip()
            city = row.get("City", "").strip()
            stadium = row.get("Stadium", "").strip()
            lat = row.get("Latitude", "").strip()
            lng = row.get("Longitude", "").strip()

            # Αν λείπουν οι συντεταγμένες, το προσπερνάμε
            if not lat or not lng:
                continue

            # Δημιουργία ID (π.χ. Arsenal -> arsenal)
            team_id = team_name.lower().replace(" ", "_").replace("fc", "").replace(".", "").strip()

            # Έλεγχος: Αν η ομάδα υπάρχει ήδη (π.χ. κάποια ελληνική), δεν την ξαναβάζουμε
            if not any(t['team_name'] == team_name for t in teams_data):
                teams_data.append({
                    "id": team_id,
                    "team_name": team_name,
                    "country": country,
                    "city": city,
                    "stadium": stadium,
                    "league": "First Division",
                    "lat": float(lat),
                    "lng": float(lng),
                    "trophies": "",
                    "jersey_url": f"assets/jerseys/{team_id}.png"
                })

        return teams_data
    except Exception as e:
        print(f"❌ Σφάλμα κατά τη λήψη: {e}")
        return []


if __name__ == "__main__":
    teams = fetch_teams_from_github()

    if teams:
        print(f"✅ Βρέθηκαν {len(teams)} ομάδες συνολικά!")
        with open('teams.json', 'w', encoding='utf-8') as f:
            json.dump(teams, f, ensure_ascii=False, indent=4)
        print("🚀 Το αρχείο teams.json δημιουργήθηκε επιτυχώς χωρίς να μπλέξουμε με τα Wikidata!")
    else:
        print("❌ Το αρχείο δεν αποθηκεύτηκε.")