from chessdotcom import get_leaderboards,get_player_stats,get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()
    for category in categories:
        print('\nCategory - ',category)
        for idx,entry in enumerate(data[category]):
            print(f'Rank: {idx+1} | Username: {entry["username"]} | Rating: {entry["score"]}')
            if idx==4:
                break


def get_player_stat(username):
    data = get_player_stats(username).json
    categories = ['chess_blitz','chess_rapid','chess_bullet']
    for category in categories:
        print('\nCategory:',category)
        print(f'Current Rating: {data[category]["last"]["rating"]}')
        print(f'Best Rating: {data[category]["best"]["rating"]}')
        print(f'Record: Win: {data[category]["record"]["win"]} | Loss: {data[category]["record"]["loss"]} | Draw: {data[category]["record"]["draw"]}')


def get_most_recent_game(username):
    data = get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-1]
    print(f'Last Match: {game["white"]["username"]}({game["white"]["rating"]}) vs {game["black"]["username"]}({game["black"]["rating"]})')
    if game['rated']:
        print(f'Category: {game["time_class"]} - Rated')
    else:
        print(f'Category: {game["time_class"]} - Unrated')
    #printer.pprint(game)


#print_leaderboards()
#get_player_stat('SwarnavaS')
get_most_recent_game('SwarnavaS')