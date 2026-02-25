from pyscript import display, document

teams = {
    "7_Ruby": "Red Dragons",
    "7_Emerald": "Green Falcons",
    "7_Sapphire": "Blue Lions",
    "7_Diamond": "Yellow Tigers",
    "8_Ruby": "Red Tigers",
    "8_Emerald": "Green Phoenix",
    "8_Sapphire": "Blue Eagles",
    "8_Diamond": "Yellow Panthers",
    "9_Ruby": "Red Warriors",
    "9_Emerald": "Green Spartans",
    "9_Sapphire": "Blue Giants",
    "9_Diamond": "Yellow Titans",
    "10_Ruby": "Red Champions",
    "10_Emerald": "Green Legend",
    "10_Sapphire": "Blue Elite",
    "10_Diamond": "Yellow Crown",
}

players_list = [
    "Escudero",
    "Estrada",
    "Tolentino",
    "Pimentel",
    "Binay",
    "Cayetano",
    "Dela Rosa",
    "Ejercito",
    "Gatchalian",
    "Go",
    "Hontiveros",
    "Lapid",
    "Legarda",
    "Marcos",
    "Padilla",
    "Poe",
    "Revilla",
    "Tulfo",
    "Villanueva",
    "Villar",
    "Zubiri"
]

def hide_all_sections():
    document.getElementById('signup_section').style.display = 'none'
    document.getElementById('teamchecker_section').style.display = 'none'
    document.getElementById('players_section').style.display = 'none'

def show_signup(e):
    hide_all_sections()
    document.getElementById('signup_section').style.display = 'block'

def show_teamchecker(e):
    hide_all_sections()
    document.getElementById('teamchecker_section').style.display = 'block'

def show_players(e):
    hide_all_sections()
    document.getElementById('players_section').style.display = 'block'

def signup_form(e):
    username = document.getElementById('username').value
    password = document.getElementById('password').value
    
    if username and password:
        document.getElementById('signup_output').innerHTML = 'Account created. You may now log in using your credentials.'
    else:
        document.getElementById('signup_output').innerHTML = 'Please fill in all fields'

def team_checker_form(e):
    grade = document.getElementById('grade').value
    section = document.getElementById('section').value
    
    if grade and section:
        team_key = f"{grade}_{section}"
        team_name = teams.get(team_key, "Unknown Team")
        document.getElementById('teamchecker_output').innerHTML = f'Congratulations! You are part of the {team_name}'
    else:
        document.getElementById('teamchecker_output').innerHTML = 'Please select your grade and section'

def show_players_list(e):
    document.getElementById('players_output').innerHTML = ''
    players_text = '<br>'.join([f'{i}) {player}' for i, player in enumerate(players_list, 1)])
    document.getElementById('players_output').innerHTML = players_text

