from flask import Flask, request, render_template, jsonify
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from nba_api.stats.endpoints import playerdashboardbyclutch
import json
from operator import itemgetter
import os 
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
   if request.method == 'POST':
      numPlayers = int(request.form['numPlayers'])
      playersArray = []
      for i in range (0, numPlayers):
         playersArray.append(request.form['player ' + str(i)])
      gameScenario = request.form['gameScenario']
      season = request.form['season']
      partOfSeason = request.form['partOfSeason']
      shotClock = request.form['shotClock']
      location = request.form['location']
      headers = {
      'Host': 'stats.nba.com',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Referer': 'https://github.com/',
      'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive',
      }
      arr = []
      indexArray = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 24, 25, 26, 27]
      for player in playersArray:
         player = players.find_players_by_full_name(player)

         ID = player[0].get('id')

         stats = playerdashboardbyclutch.PlayerDashboardByClutch(per_mode_detailed = 'PerGame', player_id = ID, season = season, season_type_playoffs = partOfSeason, shot_clock_range_nullable = shotClock, location_nullable = location, headers = headers)
         if gameScenario == "last10_sec3_point_player_dashboard":
            jsonString = stats.last10_sec3_point_player_dashboard.get_json()
         if gameScenario == "last30_sec3_point_player_dashboard":
            jsonString = stats.last30_sec3_point_player_dashboard.get_json()
         if gameScenario == "last1_min5_point_player_dashboard":
            jsonString = stats.last1_min5_point_player_dashboard.get_json()
         if gameScenario == "last3_min5_point_player_dashboard":
            jsonString = stats.last3_min5_point_player_dashboard.get_json()
         if gameScenario == "last5_min5_point_player_dashboard":
            jsonString = stats.last5_min5_point_player_dashboard.get_json()
         if gameScenario == "last5_min5_point_player_dashboard":
            jsonString = stats.last5_min5_point_player_dashboard.get_json()
         realJSON = json.loads(jsonString)
         longDataArray = realJSON["data"][0]
         shortDataArray = list(itemgetter(*indexArray)(longDataArray)) 
         arr.append(shortDataArray)
      realJSON["data"] = arr
      longLabelsArray = realJSON["headers"]
      shortLabelsArray = list(itemgetter(*indexArray)(longLabelsArray))
      realJSON["headers"] = shortLabelsArray
      return jsonify(realJSON)
if __name__ == '__main__':
   # Bind to PORT if defined, otherwise default to 5000.
    app.run(debug = True)