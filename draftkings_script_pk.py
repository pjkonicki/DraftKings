from draftkings_class import DraftKings
import logging

logging.basicConfig(level=logging.DEBUG)

"""
Create a DraftKings class object
"""
dk = DraftKings(league="MLB")

"""
Find all games & their event_ids
"""
# game_ids = dk.get_event_ids()
# for game, event_id in game_ids.items():
#     print(game, event_id)

"""
Set up a stream awaiting odds updates for the Moneyline market
"""
dk.live_odds_stream()

# event_ids=["30878090"],
