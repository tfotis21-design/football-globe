import json


def generate_football_globe():
    # 1. Τα δεδομένα των ομάδων
    teams_data = [
        # Ευρώπη
        {"id": "arsenal", "country": "England", "city": "London", "team_name": "Arsenal", "league": "Premier League",
         "lat": 51.5549, "lng": -0.1084, "stadium": "Emirates Stadium"},
        {"id": "man_city", "country": "England", "city": "Manchester", "team_name": "Manchester City",
         "league": "Premier League", "lat": 53.4831, "lng": -2.2004, "stadium": "Etihad Stadium"},
        {"id": "liverpool", "country": "England", "city": "Liverpool", "team_name": "Liverpool",
         "league": "Premier League", "lat": 53.4308, "lng": -2.9608, "stadium": "Anfield"},
        {"id": "real_madrid", "country": "Spain", "city": "Madrid", "team_name": "Real Madrid", "league": "La Liga",
         "lat": 40.453, "lng": -3.6883, "stadium": "Santiago Bernabéu"},
        {"id": "barcelona", "country": "Spain", "city": "Barcelona", "team_name": "FC Barcelona", "league": "La Liga",
         "lat": 41.3809, "lng": 2.1228, "stadium": "Camp Nou"},
        {"id": "atletico_madrid", "country": "Spain", "city": "Madrid", "team_name": "Atlético Madrid",
         "league": "La Liga", "lat": 40.4361, "lng": -3.5995, "stadium": "Metropolitano Stadium"},
        {"id": "inter", "country": "Italy", "city": "Milan", "team_name": "Inter Milan", "league": "Serie A",
         "lat": 45.4781, "lng": 9.124, "stadium": "San Siro"},
        {"id": "juventus", "country": "Italy", "city": "Turin", "team_name": "Juventus", "league": "Serie A",
         "lat": 45.1096, "lng": 7.6413, "stadium": "Allianz Stadium"},
        {"id": "milan", "country": "Italy", "city": "Milan", "team_name": "AC Milan", "league": "Serie A",
         "lat": 45.4781, "lng": 9.124, "stadium": "San Siro"},
        {"id": "bayern_munich", "country": "Germany", "city": "Munich", "team_name": "Bayern Munich",
         "league": "Bundesliga", "lat": 48.2188, "lng": 11.6247, "stadium": "Allianz Arena"},
        {"id": "dortmund", "country": "Germany", "city": "Dortmund", "team_name": "Borussia Dortmund",
         "league": "Bundesliga", "lat": 51.4926, "lng": 7.4518, "stadium": "Signal Iduna Park"},
        {"id": "leverkusen", "country": "Germany", "city": "Leverkusen", "team_name": "Bayer Leverkusen",
         "league": "Bundesliga", "lat": 51.0383, "lng": 7.0022, "stadium": "BayArena"},
        {"id": "psg", "country": "France", "city": "Paris", "team_name": "Paris Saint-Germain", "league": "Ligue 1",
         "lat": 48.8414, "lng": 2.253, "stadium": "Parc des Princes"},
        {"id": "marseille", "country": "France", "city": "Marseille", "team_name": "Marseille", "league": "Ligue 1",
         "lat": 43.2698, "lng": 5.3959, "stadium": "Stade Vélodrome"},
        {"id": "aek_athens", "country": "Greece", "city": "Athens", "team_name": "AEK Athens",
         "league": "Super League 1", "lat": 38.0361, "lng": 23.7431, "stadium": "OPAP Arena"},
        {"id": "olympiacos", "country": "Greece", "city": "Piraeus", "team_name": "Olympiacos",
         "league": "Super League 1", "lat": 37.9465, "lng": 23.6644, "stadium": "Karaiskakis Stadium"},
        {"id": "paok", "country": "Greece", "city": "Thessaloniki", "team_name": "PAOK", "league": "Super League 1",
         "lat": 40.6136, "lng": 22.9723, "stadium": "Toumba Stadium"},
        {"id": "panathinaikos", "country": "Greece", "city": "Athens", "team_name": "Panathinaikos",
         "league": "Super League 1", "lat": 37.9873, "lng": 23.7544, "stadium": "Apostolos Nikolaidis Stadium"},

        # Λατινική Αμερική
        {"id": "boca_juniors", "country": "Argentina", "city": "Buenos Aires", "team_name": "Boca Juniors",
         "league": "Primera División", "lat": -34.6356, "lng": -58.3646, "stadium": "La Bombonera"},
        {"id": "river_plate", "country": "Argentina", "city": "Buenos Aires", "team_name": "River Plate",
         "league": "Primera División", "lat": -34.5453, "lng": -58.4498, "stadium": "Más Monumental"},
        {"id": "flamengo", "country": "Brazil", "city": "Rio de Janeiro", "team_name": "Flamengo", "league": "Série A",
         "lat": -22.9121, "lng": -43.2302, "stadium": "Maracanã"},
        {"id": "palmeiras", "country": "Brazil", "city": "São Paulo", "team_name": "Palmeiras", "league": "Série A",
         "lat": -23.5275, "lng": -46.6786, "stadium": "Allianz Parque"},
        {"id": "sao_paulo", "country": "Brazil", "city": "São Paulo", "team_name": "São Paulo FC", "league": "Série A",
         "lat": -23.6001, "lng": -46.7202, "stadium": "Morumbi"},
        {"id": "penarol", "country": "Uruguay", "city": "Montevideo", "team_name": "Peñarol",
         "league": "Primera División", "lat": -34.8066, "lng": -56.0697, "stadium": "Campeón del Siglo"},
        {"id": "nacional", "country": "Uruguay", "city": "Montevideo", "team_name": "Nacional",
         "league": "Primera División", "lat": -34.8841, "lng": -56.1585, "stadium": "Gran Parque Central"},
        {"id": "atletico_nacional", "country": "Colombia", "city": "Medellín", "team_name": "Atlético Nacional",
         "league": "Primera A", "lat": 6.2566, "lng": -75.5901, "stadium": "Atanasio Girardot"},
        {"id": "club_america", "country": "Mexico", "city": "Mexico City", "team_name": "Club América",
         "league": "Liga MX", "lat": 19.3029, "lng": -99.1505, "stadium": "Estadio Azteca"}
    ]

    # Μετατροπή της λίστας σε JSON format για να περαστεί στην JavaScript
    teams_json = json.dumps(teams_data)

    # 2. Ο κώδικας HTML/CSS/JS σαν ένα μεγάλο string
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Football Globe</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #000;
            font-family: 'Arial', sans-serif;
            color: #fff;
        }}

        #globeViz {{
            width: 100vw;
            height: 100vh;
        }}

        #teamSidebar {{
            position: absolute;
            top: 0;
            right: -400px;
            width: 350px;
            height: 100vh;
            background: rgba(20, 20, 20, 0.95);
            border-left: 2px solid #333;
            transition: right 0.4s ease-in-out;
            padding: 20px;
            box-sizing: border-box;
            z-index: 10;
            overflow-y: auto;
        }}

        #teamSidebar.active {{
            right: 0;
        }}

        .close-btn {{
            position: absolute;
            top: 15px;
            right: 20px;
            cursor: pointer;
            font-size: 24px;
            color: #aaa;
        }}

        .close-btn:hover {{
            color: #fff;
        }}

        .team-header {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .team-name {{
            font-size: 28px;
            font-weight: bold;
            margin: 10px 0 5px 0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .team-league {{
            font-size: 14px;
            color: #aaa;
            margin: 0;
        }}

        .jersey-container {{
            width: 100%;
            height: 300px;
            background: #2a2a2a;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            position: relative;
            overflow: hidden;
            border: 1px solid #444;
        }}

        .jersey-placeholder-text {{
            color: #777;
            text-align: center;
            padding: 20px;
        }}

        .info-box {{
            background: #1a1a1a;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            border: 1px solid #333;
        }}

        .info-label {{
            font-size: 12px;
            color: #888;
            text-transform: uppercase;
            margin-bottom: 5px;
        }}

        .info-value {{
            font-size: 16px;
            font-weight: bold;
        }}

        #instructions {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.7);
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 14px;
            pointer-events: none;
            border: 1px solid #333;
        }}
    </style>
    <script src="https://unpkg.com/globe.gl"></script>
</head>
<body>

    <div id="globeViz"></div>
    <div id="instructions">Περίστρεψε την υδρόγειο και κάνε κλικ σε μια πινέζα.</div>

    <div id="teamSidebar">
        <div class="close-btn" id="closeSidebar">&times;</div>

        <div class="team-header">
            <h2 class="team-name" id="sidebarTeamName">Ομάδα</h2>
            <p class="team-league" id="sidebarLeague">Πρωτάθλημα, Χώρα</p>
        </div>

        <div class="jersey-container" id="jerseyContainer">
            <div class="jersey-placeholder-text">
                <span style="font-size: 40px; display: block; margin-bottom: 10px;">👕</span>
                Εδώ θα μπει η φανέλα
            </div>
        </div>

        <div class="info-box">
            <div class="info-label">Γήπεδο</div>
            <div class="info-value" id="sidebarStadium">Όνομα Γηπέδου</div>
        </div>

        <div class="info-box">
            <div class="info-label">Τοποθεσία</div>
            <div class="info-value" id="sidebarLocation">Πόλη</div>
        </div>
    </div>

    <script>
        // Τα δεδομένα περνιούνται απευθείας από την Python εδώ
        const teamData = {teams_json};

        const world = Globe()
            (document.getElementById('globeViz'))
            .globeImageUrl('https://unpkg.com/three-globe/example/img/earth-dark.jpg')
            .bumpImageUrl('https://unpkg.com/three-globe/example/img/earth-topology.png')
            .backgroundImageUrl('https://unpkg.com/three-globe/example/img/night-sky.png')
            .pointOfView({{ lat: 20, lng: -20, altitude: 2 }})

            .labelsData(teamData)
            .labelLat(d => d.lat)
            .labelLng(d => d.lng)
            .labelText(d => d.team_name)
            .labelSize(d => 1.5)
            .labelDotRadius(d => 0.6)
            .labelColor(() => 'rgba(255, 255, 255, 0.8)')
            .labelResolution(2)

            .onLabelClick(team => {{
                world.pointOfView({{
                    lat: team.lat,
                    lng: team.lng,
                    altitude: 0.8 
                }}, 1000);

                showSidebar(team);
            }})
            .labelLabel(d => `
                <div style="background: rgba(0,0,0,0.8); padding: 5px 10px; border-radius: 4px; border: 1px solid #444;">
                    <b>${{d.team_name}}</b><br/>
                    <span style="font-size: 12px; color: #aaa;">${{d.city}}, ${{d.country}}</span>
                </div>
            `);

        const sidebar = document.getElementById('teamSidebar');
        const closeBtn = document.getElementById('closeSidebar');

        function showSidebar(team) {{
            document.getElementById('sidebarTeamName').innerText = team.team_name;
            document.getElementById('sidebarLeague').innerText = `${{team.league}}, ${{team.country}}`;
            document.getElementById('sidebarStadium').innerText = team.stadium;
            document.getElementById('sidebarLocation').innerText = team.city;

            if (team.id === 'aek_athens') {{
               document.getElementById('sidebarTeamName').style.color = '#F3D11A';
               document.getElementById('teamSidebar').style.borderLeftColor = '#F3D11A';
            }} else {{
               document.getElementById('sidebarTeamName').style.color = '#fff';
               document.getElementById('teamSidebar').style.borderLeftColor = '#333';
            }}

            sidebar.classList.add('active');
        }}

        closeBtn.addEventListener('click', () => {{
            sidebar.classList.remove('active');
            const currentPov = world.pointOfView();
            world.pointOfView({{ lat: currentPov.lat, lng: currentPov.lng, altitude: 2 }}, 1000);
        }});

        world.controls().autoRotate = true;
        world.controls().autoRotateSpeed = 0.5;

        const controls = world.controls();
        controls.addEventListener('start', () => {{
            controls.autoRotate = false;
        }});
    </script>
</body>
</html>
"""

    # 3. Αποθήκευση του αρχείου HTML
    output_filename = "index.html"

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(html_template)

    print(f"✅ Επιτυχία! Το αρχείο '{output_filename}' δημιουργήθηκε.")
    print("Μπορείς να το ανοίξεις στον browser σου με διπλό κλικ.")


if __name__ == "__main__":
    generate_football_globe()