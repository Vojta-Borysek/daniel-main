from bettano_no_inplay import Bet_nip
from smar_no_inplay import SNI
from difflib import SequenceMatcher


class Foot:
    def __init__(self, path):
        self.path = path

    def football(self):

        #print("Import path: ")
        #path = str(input()+"\\chromedriver.exe")
        #path = "C:\\Users\\Comfor\\PycharmProjects\\daniel_try"
        path = self.path
        x = Bet_nip(path)
        bets = x.bettano_nip()
        y = SNI(path)
        exch = y.s_no_inplay()

        value = []

        num_e = 0
        for exc in exch[1]:
            if (exch[1][num_e][0] == 0):
                break
            num_b = 0
            for bet in bets[1]:
                if(bets[1][num_b][0] == 0):
                    continue
                if (SequenceMatcher(None, exch[1][num_e][0], bets[1][num_b][0]).ratio() > 0.75):
                    for i in range(1, 4):
                        if (exch[1][num_e][i] == 'ASK'):
                            continue
                        try:
                            if (float(exch[1][num_e][i]) <= float(bets[1][num_b][i])):
                                print(exch[1][num_e][0], "||", bets[1][num_b][0], "\n")
                                value.append(exch[1][num_e][0]+" || "+bets[1][num_b][0])
                                if (i == 1):
                                    print("HOME: ", exch[1][num_e][i], "-", bets[1][num_b][i], "\n")
                                    value.append("HOME: "+exch[1][num_e][i]+"-"+bets[1][num_b][i])
                                if (i == 2):
                                    print("DRAW: ", exch[1][num_e][i], "-", bets[1][num_b][i], "\n")
                                    value.append("DRAW: "+exch[1][num_e][i]+"-"+bets[1][num_b][i])
                                if(i == 3):
                                    print("AWAY: ", exch[1][num_e][i], "-", bets[1][num_b][i], "\n")
                                    value.append("AWAY: "+exch[1][num_e][i]+"-"+bets[1][num_b][i])
                        except:
                            continue

                num_b+=1
            num_e+=1

        #z = TONET(value)
        #z.to_net()

        print("Success")
