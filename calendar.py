# Get todays events in particular. Base weekly events just hard coded in
# Also get time.
# FIXED   - Odd daily events - balls, massage, lottery, swarm, vocabulary
# UPDATED - table weekly - sibling, lottery, gym, bug catching contest
# Return todays events:
import datetime


def get_events():
    # Monday 0 - Sunday 6
    #  [
    #   [ event_time, event_name, description],
    #   \vdots
    #  ]
    events = {
        0: [["All Day","Department Store Lottery", "TM65 (Shadow Claw), Nest Ball, and Cheri Berry"],
            []],
        1: [["All Day","Department Store Lottery", "TM91 (Flash Cannon), Repeat Ball, and Chesto Berry"],
            ["All Day", "Bug Catching Contest", "Once a day in the national Park"],
            []],
        2: [["All Day","Department Store Lottery", "TM57 (Charge Beam), Net Ball, and Pecha Berry"],
            []],
        3: [["All Day","Department Store Lottery", "TM60 (Drain Punch), Quick Ball, and Rawst Berry"],
            ["All Day", "Bug Catching Contest", "Once a day in the national Park"],
            []],
        4: [["All Day","Department Store Lottery", "TM42 (Facade), Dusk Ball, and Aspear Berry"],
            []],
        5: [["All Day","Department Store Lottery", "TM62 (Silver Wind), Timer Ball, and Oran Berry"],
            ["All Day", "Bug Catching Contest", "Once a day in the national Park"],
            []],
        6: [["All Day","Department Store Lottery", "TM02 (Dragon Claw), Luxury Ball, and Persim Berry"],
            []],
    }
    return events[datetime.datetime.today().weekday()]


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

    return rematches[datetime.datetime.today().weekday()]