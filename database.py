import pandas as pd
import consts
import game_field
import guard
import soldier
import teleport


def initialize_db():
    bush_location = [[], [], [], [], [], [], [], [], []]
    soldier_location = [[], [], [], [], [], [], [], [], []]
    mine_location = [[], [], [], [], [], [], [], [], []]
    tp_location = [[], [], [], [], [], [], [], [], []]

    titles = {"bush": bush_location,
              "soldier": soldier_location,
              "mine": mine_location,
              "tp": tp_location
              }
    df = pd.DataFrame(titles)
    df.to_csv(consts.DATABASE_FILE, index=False, header=True)


def save_game(key):
    df = pd.read_csv(consts.DATABASE_FILE)
    df.loc[key - 1] = ((consts.BUSH_PLACEMENT, soldier.get_soldier_pos(game_field.game_field_metrics)
                        , game_field.mines
                       , teleport.teleports))

    df.to_csv("db.csv", index=False, header=True)


def read_db(key, var):
    df = pd.read_csv(consts.DATABASE_FILE)
    # gives you the value you want based on the key you inserted and the type of var you want
    if var == consts.VAR_BUSH:
        return df["bush"][key - 1]
    if var == consts.VAR_SOLDIER:
        return df["soldier"][key - 1]
    if var == consts.VAR_MINE:
        return df["mine"][key - 1]
    if var == consts.VAR_TELEPORT:
        return df["tp"][key - 1]


def clear_database():
    f = open(consts.DATABASE_FILE, "w+")
    f.close()
