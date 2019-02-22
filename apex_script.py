import os
import requests
import json
from requests import HTTPError
from player import PlayerStats, Legend
import pandas as pd

legend_list = []


def printJson(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def writeToExcel(player_stats):
    file = 'lifetime-stats.xlsx'

    columns = []
    player_dict = player_stats.to_dict()
    for key in player_dict.keys():
        columns.append(key)

    print(columns)

    df = pd.DataFrame(player_dict, columns=columns)
    df.to_excel(file)


def getApiData():
    URL = 'https://public-api.tracker.gg/apex/v1/standard/profile/2/Nikezy'
    API_KEY = '8b8c6507-2bf4-4616-8818-dea502e9a86a'
    HEADERS = {'TRN-Api-Key': API_KEY}
    try:
        r = requests.get(url=URL, headers=HEADERS)
        r.raise_for_status()
    except HTTPError as e:
        raise e
    data = r.json()
    printJson(data)
    return data.get('data')


def getLifetimeStats(data):
    username = data['metadata']['platformUserHandle']
    platform_id = data['metadata']['platformId']
    level = data['metadata']['level']
    overall_stats = data['stats']
    for stat in overall_stats:
        if stat['metadata']['key'] == 'Kills':
            total_kills = stat['value']
            percentile = stat['percentile']
            player_stats = PlayerStats(username, platform_id, total_kills, level, percentile)
            writeToExcel(player_stats)
            break
    print('Lifetime Stats')
    printJson(player_stats.to_dict())


def getLegendStats(data):
    for legend in data['children']:
        # printJson(legend)
        legend_name = legend['metadata']['legend_name']
        print(legend_name, 'Stats')
        stats = legend['stats']
        for stat in stats:
            # print('Stat:', stat)
            if stat['metadata']['key'] == 'Kills':
                rank = stat['rank']
                kills = stat['value']
                percentile = stat['percentile']
                legend_obj = Legend(legend_name, kills, rank, percentile)
                legend_list.append(legend_obj)
        printJson(legend_obj.to_dict())


def main():
    print('888888888888888888888888888888888888888888888888888888888888')
    try:
        data = getApiData()
    except HTTPError:
        raise

    getLifetimeStats(data)
    getLegendStats(data)


if __name__ == '__main__':
    main()
