import pandas as pd
import consts
import game_field
import soldier


def initialize_db():
    bush_location = [[], [], [], [], [], [], [], [], []]
    soldier_location = [[], [], [], [], [], [], [], [], []]
    mine_location = [[], [], [], [], [], [], [], [], []]

    titles = {"bush": bush_location,
              "soldier": soldier_location,
              "mine": mine_location
              }
    df = pd.DataFrame(titles)
    df.to_csv(consts.DATABASE_FILE, index=False, header=True)


def save_game(key):
    df = pd.read_csv(consts.DATABASE_FILE)
    df.loc[key - 1] = consts.BUSH_PLACEMENT, soldier.get_soldier_pos(game_field.game_field_metrics), game_field.mines

    df.to_csv("db.csv", index=False, header=True)
