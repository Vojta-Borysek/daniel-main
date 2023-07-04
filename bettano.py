from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pynput.keyboard import Key, Controller


class Bet:

    def __init__(self, path):
        self.path = path

    def bettano(self):

        urls = ["https://www.betano.cz/sport/fotbal/souteze/ceska-republika/11338/",
                "https://www.betano.cz/sport/fotbal/souteze/liga-mistru/188566/",
                "https://www.betano.cz/sport/fotbal/souteze/evropska-konferencni-liga/189602/",
                "https://www.betano.cz/sport/fotbal/souteze/anglie/1/",
                "https://www.betano.cz/sport/fotbal/souteze/spanelsko/2/",
                "https://www.betano.cz/sport/fotbal/souteze/italie/87/",
                "https://www.betano.cz/sport/fotbal/souteze/nemecko/24/",
                "https://www.betano.cz/sport/fotbal/souteze/francie/23/",
                "https://www.betano.cz/sport/fotbal/souteze/portugalsko/11382/",
                "https://www.betano.cz/sport/fotbal/souteze/nizozemsko/11376/",
                "https://www.betano.cz/sport/fotbal/souteze/turecko/11384/",
                "https://www.betano.cz/sport/fotbal/souteze/evropska-liga/188567/",
                "https://www.betano.cz/sport/fotbal/souteze/albanie/11317/",
                "https://www.betano.cz/sport/fotbal/souteze/belgie/11324/",
                "https://www.betano.cz/sport/fotbal/souteze/bosna-a-hercegovina/11478/",
                "https://www.betano.cz/sport/fotbal/souteze/bulharsko/11328/",
                "https://www.betano.cz/sport/fotbal/souteze/chorvatsko/11334/",
                "https://www.betano.cz/sport/fotbal/souteze/dansko/11339/",
                "https://www.betano.cz/sport/fotbal/souteze/estonsko/11411/",
                "https://www.betano.cz/sport/fotbal/souteze/finsko/11355/",
                "https://www.betano.cz/sport/fotbal/souteze/gruzie/11436/",
                "https://www.betano.cz/sport/fotbal/souteze/irsko/11367/",
                "https://www.betano.cz/sport/fotbal/souteze/island/10008/",
                "https://www.betano.cz/sport/fotbal/souteze/izrael/11429/",
                "https://www.betano.cz/sport/fotbal/souteze/kypr/11336/",
                "https://www.betano.cz/sport/fotbal/souteze/madarsko/11363/",
                "https://www.betano.cz/sport/fotbal/souteze/malta/11491/",
                "https://www.betano.cz/sport/fotbal/souteze/moldavsko/11442/",
                "https://www.betano.cz/sport/fotbal/souteze/norsko/11378/",
                "https://www.betano.cz/sport/fotbal/souteze/polsko/11381/",
                "https://www.betano.cz/sport/fotbal/souteze/rakousko/11322/",
                "https://www.betano.cz/sport/fotbal/souteze/recko/90/",
                "https://www.betano.cz/sport/fotbal/souteze/rumunsko/11383/",
                "https://www.betano.cz/sport/fotbal/souteze/severni-irsko/11377/",
                "https://www.betano.cz/sport/fotbal/souteze/skotsko/91/",
                "https://www.betano.cz/sport/fotbal/souteze/slovensko/11392/",
                "https://www.betano.cz/sport/fotbal/souteze/slovinsko/11435/",
                "https://www.betano.cz/sport/fotbal/souteze/srbsko/11389/",
                "https://www.betano.cz/sport/fotbal/souteze/svedsko/11393/",
                "https://www.betano.cz/sport/fotbal/souteze/svycarsko/11394/",
                "https://www.betano.cz/sport/fotbal/souteze/ukrajina/11386/",
                "https://www.betano.cz/sport/fotbal/souteze/wales/11433/"]

        num_of_match = len(urls)*55
        cols, rows = (4, num_of_match)

        matches_arr=[]
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(0)
            matches_arr.append(col)

        team_num = 0
        odds_num_2 = 0
        for url in urls:
            try:
                keyboard = Controller()
                key_esc = Key.esc
                #path = "C:\\Users\\Comfor\\PycharmProjects\\daniel_try\\chromedriver.exe"
                path = self.path
                driver = webdriver.Chrome(path)
                # driver.maximize_window()
                driver.get(url)
                time.sleep(5)

                keyboard.press(key_esc)
                keyboard.release(key_esc)

                time.sleep(1)

                teams = driver.find_elements(By.CLASS_NAME, "events-list__grid__info__main__participants")
                teams_length = len(teams)
                if (teams_length <= 0 or driver.current_url != url):
                    driver.quit()
                    continue
                for p in teams:
                    team_str = p.get_attribute("innerText")
                    # print(p.text)
                    # print("\n")
                    team_str = team_str.replace("\n", "-")
                    matches_arr[team_num][0] = team_str
                    team_num += 1

                odd = driver.find_elements(By.CLASS_NAME, "selections__selection__odd")
                time.sleep(2)
                odds_num = 0
                odds_num_1 = 1
                for o in odd:
                    # print(o.text)
                    matches_arr[odds_num_2][odds_num_1] = o.get_attribute("innerText")
                    if (odds_num_1 % 3 == 0 or odds_num_1 == 3):
                        # print("\n")
                        odds_num_2 += 1
                        odds_num_1 = 0
                    odds_num_1 += 1
                    odds_num += 1
                    if (3 * teams_length == odds_num):
                        break

                driver.quit()
            finally:
                continue

        return [num_of_match, matches_arr]