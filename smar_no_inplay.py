from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SNI:
    def __init__(self, path):
        self.path = path

    def s_no_inplay(self):

        urls = ["https://smarkets.com/listing/sport/football/czech-republic-cup",
                "https://smarkets.com/listing/sport/football/czech-republic-premier-league",
                "https://smarkets.com/listing/sport/football/italy-serie-b",
                "https://smarkets.com/listing/sport/football/spain-la-liga-2",
                "https://smarkets.com/listing/sport/football/france-ligue-2",
                "https://smarkets.com/listing/sport/football/france-ligue-national",
                "https://smarkets.com/listing/sport/football/germany-2-bundesliga",
                "https://smarkets.com/listing/sport/football/germany-3-liga",
                "https://smarkets.com/listing/sport/football/uefa-europa-conference-league-qualification",
                "https://smarkets.com/listing/sport/football/uefa-europa-league-qualification",
                "https://smarkets.com/listing/sport/football/uefa-champions-league-qualification",
                "https://smarkets.com/listing/sport/football/england-premier-league",
                "https://smarkets.com/listing/sport/football/england-professional-development-league",
                "https://smarkets.com/listing/sport/football/england-championship",
                "https://smarkets.com/listing/sport/football/england-league-cup",
                "https://smarkets.com/listing/sport/football/england-league-1",
                "https://smarkets.com/listing/sport/football/england-league-2",
                "https://smarkets.com/listing/sport/football/italy-serie-a",
                "https://smarkets.com/listing/sport/football/spain-la-liga",
                "https://smarkets.com/listing/sport/football/france-ligue-1",
                "https://smarkets.com/listing/sport/football/germany-bundesliga",
                "https://smarkets.com/listing/sport/football/netherlands-eredivisie",
                "https://smarkets.com/listing/sport/football/portugal-primeira-liga",
                "https://smarkets.com/listing/sport/football/turkey-1-lig",
                "https://smarkets.com/listing/sport/football/turkey-super-lig",
                "https://smarkets.com/listing/sport/football/england-efl-trophy",
                "https://smarkets.com/listing/sport/football/england-national-league",
                "https://smarkets.com/listing/sport/football/scotland-championship",
                "https://smarkets.com/listing/sport/football/scotland-league-one",
                "https://smarkets.com/listing/sport/football/scotland-league-two",
                "https://smarkets.com/listing/sport/football/scotland-premiership",
                "https://smarkets.com/listing/sport/football/wales-premier-league",
                "https://smarkets.com/listing/sport/football/england-premier-league-2-division-2",
                "https://smarkets.com/listing/sport/football/austria-ofb-cup",
                "https://smarkets.com/listing/sport/football/belgium-first-division-a",
                "https://smarkets.com/listing/sport/football/bulgaria-first-division",
                "https://smarkets.com/listing/sport/football/croatia-hnl",
                "https://smarkets.com/listing/sport/football/denmark-1-division",
                "https://smarkets.com/listing/sport/football/denmark-superliga",
                "https://smarkets.com/listing/sport/football/denmark-landspokal",
                "https://smarkets.com/listing/sport/football/estonia-meistriliiga",
                "https://smarkets.com/listing/sport/football/finland-veikkausliiga",
                "https://smarkets.com/listing/sport/football/germany-regionalliga-nord",
                "https://smarkets.com/listing/sport/football/germany-regionalliga-nordost",
                "https://smarkets.com/listing/sport/football/greece-cup",
                "https://smarkets.com/listing/sport/football/greece-super-league",
                "https://smarkets.com/listing/sport/football/hungary-nb-i",
                "https://smarkets.com/listing/sport/football/iceland-premier-league",
                "https://smarkets.com/listing/sport/football/ireland-premier-division",
                "https://smarkets.com/listing/sport/football/israel-ligat-al",
                "https://smarkets.com/listing/sport/football/israel-state-cup",
                "https://smarkets.com/listing/sport/football/norway-premier-league",
                "https://smarkets.com/listing/sport/football/poland-ekstraklasa",
                "https://smarkets.com/listing/sport/football/portugal-liga-2",
                "https://smarkets.com/listing/sport/football/romania-cup",
                "https://smarkets.com/listing/sport/football/romania-liga-1",
                "https://smarkets.com/listing/sport/football/serbia-superliga",
                "https://smarkets.com/listing/sport/football/slovakia-super-liga",
                "https://smarkets.com/listing/sport/football/slovakia-republic-cup",
                "https://smarkets.com/listing/sport/football/slovenia-prva-liga",
                "https://smarkets.com/listing/sport/football/germany-dfb-pokal",
                "https://smarkets.com/listing/sport/football/sweden-allsvenskan",
                "https://smarkets.com/listing/sport/football/sweden-superettan",
                "https://smarkets.com/listing/sport/football/sweden-svenska-cupen",
                "https://smarkets.com/listing/sport/football/switzerland-super-league",
                "https://smarkets.com/listing/sport/football/switzerland-super-league",
                "https://smarkets.com/listing/sport/football/ukraine-premier-league"]

        num_of_match = len(urls)*11
        cols, rows = (4, num_of_match)
        league = 0
        matches = 0

        matches_arr=[]
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(0)
            matches_arr.append(col)

        team_num = 0
        odds_num_2_1 = 0
        for url in urls:
            try:
                #path = "C:\\Users\\Comfor\\PycharmProjects\\daniel_try\\chromedriver.exe"
                path = self.path
                driver = webdriver.Chrome(path)
                driver.get(url)
                time.sleep(5)
                if (driver.current_url!=url):
                    driver.quit()
                    continue
                odds_num_2_2 = 1

                inplay = driver.find_elements(By.CLASS_NAME, "minutes-text")
                time.sleep(0.5)
                teams = driver.find_elements(By.CLASS_NAME, "teams")
                time.sleep(0.5)
                lenght = len(teams) - len(inplay)
                begin = 0
                teamm = []
                for team in reversed(teams):
                    if (lenght <= begin):
                        break
                    team_str = team.text
                    team_str = team_str.replace("\n", "-")
                    teamm.append(team_str)
                    begin += 1
                    if (league>=9):
                        matches+=1

                for t in teamm:
                    matches_arr[team_num][0] = t
                    team_num += 1

                odds_2 = driver.find_elements(By.CLASS_NAME, "bid")
                time.sleep(0.5)
                odds_3 = []

                begin_2 = 0
                for o in odds_2:
                    strm = o.text
                    strm = strm.split('\n', 1)[0]
                    odds_3.append(strm)
                    begin_2 += 1

                for i in range(0, len(inplay) * 3):
                    odds_3.pop(0)

                odds = []
                for p in reversed(odds_3):
                    odds.append(p)

                for od in range(0, len(odds), 3):
                    matches_arr[odds_num_2_1][odds_num_2_2] = odds[od+2]
                    matches_arr[odds_num_2_1][odds_num_2_2 + 1] = odds[od+1]
                    matches_arr[odds_num_2_1][odds_num_2_2 + 2] = odds[od]
                    odds_num_2_2 = 1
                    odds_num_2_1 += 1

                time.sleep(2)
                driver.quit()
                time.sleep(0.1)
                league+=1

            finally:
                continue

        return [matches, matches_arr, num_of_match]
