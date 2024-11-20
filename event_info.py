# Get todays events in particular. Base weekly events just hard coded in
# Also get time.
# FIXED   - Odd daily events - balls, massage, lottery, swarm, vocabulary
# UPDATED - table weekly - sibling, lottery, gym, bug catching contest
# Return todays events:
import datetime


def get_today_events():
    today = datetime.datetime.now()    
    day= today.weekday()
    date = f"{today.strftime('%A')}s Events ({today.strftime('%m/%d')})"

    events = []

    for i, f in enumerate([get_sibling(), get_rematches(), get_events()]):
        for e in f[day]:
            if i == 0:
                e = ["All Day", f"{e[2]}/{e[1]}", e[0]]
            elif i == 1:
                e = [e[0], e[1], "Gym Rematch"]
            events.append(e)
    return date, events


def get_daily():
    daily = [
    # event_time, event_name, description
        ["All Day", "Ball Seals", "Olivine City"],
        ["All Day", "Pokemon Swarms", "Proffessor Oak's Talk Show"],
        ["All Day", "Vocabulary", "THe house off Route 16. You need Cut."],
        ["3pm - 4pm", "Daisy's Massage", "The only way in HGSS to increase beauty."],
        ["2am, 5am, 8am, 11am, 2pm, 5pm, 8pm, and 11pm", "Buena's Password", "Tune in for the password."]
    ]
    return daily


def get_events():
    # Monday 0 - Sunday 6
    #  [
    #   [ event_time, event_name, description],
    #   \vdots
    #  ]
    events = {
        0: [["All Day","Department Store Lottery", "TM65 (Shadow Claw), Nest Ball, and Cheri Berry"],
            ["All Day", "Bargain Shop", "Goldenrod Underground"],
            ["All Day", "SS Aquatic", "Olivine City"],
            ["All Day", "Rival Rematch", "Indigo Plateau"],
            ["8:00-11:59pm", "Clefairy Dance", "Mt. Moon"]],
        1: [["All Day","Department Store Lottery", "TM91 (Flash Cannon), Repeat Ball, and Chesto Berry"],
            ["All Day", "Bug Catching Contest", "Once a day in the national Park"],
            ["All Day", "Older Hairdresser", "Goldenrod Underground"]],
        2: [["All Day","Department Store Lottery", "TM57 (Charge Beam), Net Ball, and Pecha Berry"],
            ["All Day", "Younger Hairdresser", "Goldenrod Underground"],
            ["All Day", "SS Aquatic", "Vermillion City"],
            ["All Day", "Rival Rematch", "Indigo Plateau"],
            ["All Day", "Hoenn Sound", "Pokegear"],
            ["All Day", "Low Tide", "Lake of Rage"]],
        3: [["All Day","Department Store Lottery", "TM60 (Drain Punch), Quick Ball, and Rawst Berry"],
            ["All Day", "Bug Catching Contest", "Once a day in the national Park"],
            ["All Day", "Older Hairdresser", "Goldenrod Underground"],
            ["All Day", "Sinnoh Sound", "Pokegear"]],
        4: [["All Day","Department Store Lottery", "TM42 (Facade), Dusk Ball, and Aspear Berry"],
            ["All Day", "Younger Hairdresser", "Goldenrod Underground"],
            ["All Day", "SS Aquatic", "Olivine City"],
            ["All Day", "Lapras", "Union Cave"]],
        5: [["All Day","Department Store Lottery", "TM62 (Silver Wind), Timer Ball, and Oran Berry"],
            ["All Day", "Bug Catching Contest", "Once a day in the national Park"],
            ["All Day", "Older Hairdresser", "Goldenrod Underground"],
            ["All Day", "Herb Shop", "Goldenrod Underground"]],
        6: [["All Day","Department Store Lottery", "TM02 (Dragon Claw), Luxury Ball, and Persim Berry"],
            ["All Day", "Younger Hairdresser", "Goldenrod Underground"],
            ["All Day", "Herb Shop", "Goldenrod Underground"],
            ["All Day", "SS Aquatic", "Vermillion City"]],
    }
    return events


def get_sibling():
    sibs = {
        # Location, ribbon, reward
        0: [["Route 40", "Sharp Beak", "Alert Ribbon"]],
        1: [["Route 29", "Twisted Spoon", "Shock Ribbon"]],
        2: [["Lake of Rage", "Black Belt", "Downcast Ribbon"]],
        3: [["Route 36", "Hard Stone", "Careless Ribbon"]],
        4: [["Route 32", "Poison Bard", "Relax Ribbon"]],
        5: [["Blackthorn City", "Soft Sand", "Snooze Ribbon"]],
        6: [["Route 37", "Magnet", "Smile Ribbon"]]
    }
    return sibs


def get_rematches():
    # [
    #  [call_time, leader_name]
    # ]
    rematches = {
        0: # Monday
            [["Morning", "Pryce"],
             ["Daytime", "Janine"]],
        1: # Tuesday
            [["Night", "Morty"]],
        2: # Wednesday
            [["Morning", "Misty"],
             ["Afternoon", "Jasmine"],
             ["Night", "Chuck"]],
        3: # Thursday
            [["Afternoon", "Bugsy"],
             ["Afternoon", "Blaine"]],
        4: # Friday
            [["Morning", "Lt. Surge"],
             ["Night", "Clair"]],
        5: # Saturday
            [["Morning", "Falkner"],
             ["Afternoon", "Whitney"],
             ["Night", "Block"]],
        6: # Sunday
            [["Morning", "Erika"],
             ["Afternoon", "Sabrina"],
             ["Night", "Blue"]],
    }

    return rematches

