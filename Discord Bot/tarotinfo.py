# cards? (1/3/5)
# reversals? (y/n)
# if reversals == y, use second dictionary
# dict1 = no reversals
# dict2 = reversals
from code import interact
from tarotcards import *
from random import randint
dict1 = {
    1: the_fool, 2: the_magician, 3: the_high_priestess, 4: the_empress, 5: the_emperor, 
    6: the_hierophant1, 7: the_hierophant2, 8: the_lovers, 9: the_chariot, 10: strength, 
    11: the_hermit, 12: the_wheel, 13: justice, 14: the_hanged_man, 15: death_stubborn, 
    16: death_rebirth, 17: death_fire, 18: death_blood, 19: death_motel, 20: death_dancing,
    21: death_riding, 22: death_sowing, 23: death_shovel, 24: temperance, 25: devil_1, 
    26: devil_2, 27: the_tower, 28: house_of_god, 29: the_horizon, 30: the_star, 
    31: the_moon, 32: the_sun_sigil, 33: the_sun_alpaca, 34: judgement, 35: the_world,
    36: ace_of_cups, 37: two_of_cups, 38: three_of_cups, 39: four_of_cups, 40: five_of_cups,
    41: six_of_cups, 42: seven_of_cups, 43: eight_of_cups, 44: nine_of_cups, 45: ten_of_cups,
    46: page_of_cups, 47: knight_of_cups, 48: queen_of_cups, 49: king_of_cups, 50: ace_of_wands,
    51: two_of_wands, 52: three_of_wands, 53: four_of_wands, 54: five_of_wands, 55: six_of_wands,
    56: seven_of_wands, 57: eight_of_wands, 58: nine_of_wands, 59: ten_of_wands, 60: page_of_wands,
    61: knight_of_wands, 62: queen_of_wands, 63: king_of_wands, 64: ace_of_swords, 65: two_of_swords,
    66: three_of_swords, 67: four_of_swords, 68: five_of_swords, 69: six_of_swords, 70: seven_of_swords,
    71: eight_of_swords, 72: nine_of_swords, 73: ten_of_swords, 74: page_of_swords, 75: knight_of_swords,
    76: queen_of_swords, 77: king_of_swords, 78: ace_of_disks, 79: two_of_disks, 80: three_of_disks,
    81: four_of_disks, 82: five_of_disks, 83: six_of_disks, 84: seven_of_pentacles, 85: eight_of_pentacles,
    86: nine_of_disks, 87: ten_of_disks, 88: page_of_pentacles, 89: knight_of_rings, 90: queen_of_pentacles,
    91: king_of_coins, 92: ace_of_hounds, 93: two_of_whips, 94: three_of_books, 95:four_of_keys, 
    96: five_of_mirrors, 97: six_of_inking, 98: seven_of_bells, 99: eight_of_tentacles, 100: nine_of_clocks,
    101: ten_of_eyes, 102: the_builder, 103: masterless_knight, 104: queen_of_bombs, 105: father_sleep, 
    106: the_fountain, 107: black_candle, 108: white_candle, 109: the_wild_hunt, 110: joker, 
    111: paimon, 112: giuseppe, 113: the_dark_sun, 114: the_black_moon, 115: the_bogeyman, 
    116: fear, 117: the_hole, 118: the_hawkmoth, 119: the_letter, 120: wound_man,
    121: the_comforter, 122: lone_and_level_sands, 123: dagaz, 124: misery, 125: hope, 
    126: weird_mystical_shit, 127: tradition, 128: frost, 129: deconsecration, 130: the_battle,
    131: bone_fire, 132: the_night_owl, 133: the_undaunted, 134: the_empty, 135: the_traitor, 
    136: the_performer, 137: the_thing, 138: final_tarot
}
dict2 = {
    1: the_fool, 2: the_magician, 3: the_high_priestess, 4: the_empress, 5: the_emperor, 
    6: the_hierophant1, 7: the_hierophant2, 8: the_lovers, 9: the_chariot, 10: strength, 
    11: the_hermit, 12: the_wheel, 13: justice, 14: the_hanged_man, 15: death_stubborn, 
    16: death_rebirth, 17: death_fire, 18: death_blood, 19: death_motel, 20: death_dancing,
    21: death_riding, 22: death_sowing, 23: death_shovel, 24: temperance, 25: devil_1, 
    26: devil_2, 27: the_tower, 28: house_of_god, 29: the_horizon, 30: the_star, 
    31: the_moon, 32: the_sun_sigil, 33: the_sun_alpaca, 34: judgement, 35: the_world,
    36: ace_of_cups, 37: two_of_cups, 38: three_of_cups, 39: four_of_cups, 40: five_of_cups,
    41: six_of_cups, 42: seven_of_cups, 43: eight_of_cups, 44: nine_of_cups, 45: ten_of_cups,
    46: page_of_cups, 47: knight_of_cups, 48: queen_of_cups, 49: king_of_cups, 50: ace_of_wands,
    51: two_of_wands, 52: three_of_wands, 53: four_of_wands, 54: five_of_wands, 55: six_of_wands,
    56: seven_of_wands, 57: eight_of_wands, 58: nine_of_wands, 59: ten_of_wands, 60: page_of_wands,
    61: knight_of_wands, 62: queen_of_wands, 63: king_of_wands, 64: ace_of_swords, 65: two_of_swords,
    66: three_of_swords, 67: four_of_swords, 68: five_of_swords, 69: six_of_swords, 70: seven_of_swords,
    71: eight_of_swords, 72: nine_of_swords, 73: ten_of_swords, 74: page_of_swords, 75: knight_of_swords,
    76: queen_of_swords, 77: king_of_swords, 78: ace_of_disks, 79: two_of_disks, 80: three_of_disks,
    81: four_of_disks, 82: five_of_disks, 83: six_of_disks, 84: seven_of_pentacles, 85: eight_of_pentacles,
    86: nine_of_disks, 87: ten_of_disks, 88: page_of_pentacles, 89: knight_of_rings, 90: queen_of_pentacles,
    91: king_of_coins, 92: ace_of_hounds, 93: two_of_whips, 94: three_of_books, 95:four_of_keys, 
    96: five_of_mirrors, 97: six_of_inking, 98: seven_of_bells, 99: eight_of_tentacles, 100: nine_of_clocks,
    101: ten_of_eyes, 102: the_builder, 103: masterless_knight, 104: queen_of_bombs, 105: father_sleep, 
    106: the_fountain, 107: black_candle, 108: white_candle, 109: the_wild_hunt, 110: joker, 
    111: paimon, 112: giuseppe, 113: the_dark_sun, 114: the_black_moon, 115: the_bogeyman, 
    116: fear, 117: the_hole, 118: the_hawkmoth, 119: the_letter, 120: wound_man,
    121: the_comforter, 122: lone_and_level_sands, 123: dagaz, 124: misery, 125: hope, 
    126: weird_mystical_shit, 127: tradition, 128: frost, 129: deconsecration, 130: the_battle,
    131: bone_fire, 132: the_night_owl, 133: the_undaunted, 134: the_empty, 135: the_traitor, 
    136: the_performer, 137: the_thing, 138: final_tarot, 139: the_fool_rev, 140: the_magician_rev,
    141: the_high_priestess_rev, 142: the_empress_rev, 143: the_emperor_rev, 144: the_hierophant1_rev, 145: the_hierophant2_rev,
    146: the_lovers_rev, 147: the_chariot_rev, 148: strength_rev, 149: the_hermit_rev, 150: the_wheel_rev,
    151: justice_rev, 152: the_hanged_man_rev, 153: death_stubborn_rev, 154: death_rebirth_rev, 155: death_fire_rev,
    156: death_blood_rev, 157: death_motel_rev, 158: death_dancing_rev, 159: death_riding_rev, 160: death_sowing_rev, 
    161: death_shovel_rev, 162: temperance_rev, 163: devil_1_rev, 164: devil_2_rev, 165: the_tower_rev, 
    166: house_of_god_rev, 167: the_star_rev, 168: the_moon_rev, 169: the_sun_sigil_rev, 170: the_sun_alpaca_rev,
    171: judgement_rev, 172: the_world_rev, 173: ace_of_cups_rev, 174: two_of_cups_rev, 175: three_of_cups_rev,
    176: four_of_cups_rev, 177: five_of_cups_rev, 178: six_of_cups_rev, 179: seven_of_cups_rev, 180: eight_of_cups_rev,
    181: nine_of_cups_rev, 182: ten_of_cups_rev, 183: page_of_cups_rev, 184: knight_of_cups_rev, 185: queen_of_cups_rev,
    186: king_of_cups_rev, 187:ace_of_wands_rev, 188: two_of_wands_rev, 189: three_of_wands_rev, 190: four_of_wands_rev,
    191: five_of_wands_rev, 192: six_of_wands_rev, 193: seven_of_wands_rev, 194: eight_of_wands_rev, 195: nine_of_wands_rev,
    196: ten_of_wands_rev, 197: page_of_wands_rev, 198: knight_of_wands_rev, 199: queen_of_wands_rev, 200: king_of_wands_rev,
    201: ace_of_swords_rev, 202: two_of_swords_rev, 203: three_of_swords_rev, 204: four_of_swords_rev, 205: five_of_swords_rev,
    206: six_of_swords_rev, 207: seven_of_swords_rev, 208: eight_of_swords_rev, 209: nine_of_swords_rev, 210: ten_of_swords_rev,
    211: page_of_swords_rev, 212: knight_of_swords_rev, 213: queen_of_swords_rev, 214: king_of_swords_rev, 215: ace_of_disks_rev,
    216: two_of_disks_rev, 217: three_of_disks_rev, 218: four_of_disks_rev, 219: five_of_disks_rev, 220: six_of_disks_rev,
    221: seven_of_pentacles_rev, 222: eight_of_pentacles_rev, 223: nine_of_disks_rev, 224: ten_of_disks_rev, 225: page_of_pentacles_rev,
    226: knight_of_rings_rev, 227: queen_of_pentacles_rev, 228: king_of_coins_rev, 229: ace_of_hounds_rev, 230: two_of_whips_rev,
    231: three_of_books_rev, 232: four_of_keys_rev, 233: five_of_mirrors_rev, 234: six_of_inking_rev, 235: seven_of_bells_rev,
    236: eight_of_tentacles_rev, 237: nine_of_clocks_rev, 238: ten_of_eyes_rev, 239: the_builder_rev, 240: masterless_knight_rev,
    241: queen_of_bombs_rev, 242: father_sleep_rev, 243: the_fountain_rev, 244: the_wild_hunt_rev, 245: paimon_rev,
    246: giuseppe_rev, 247: the_dark_sun_rev, 248: the_black_moon_rev, 249: the_bogeyman_rev, 250: fear_rev,
    251: the_hole_rev, 252: the_hawkmoth_rev, 253: the_letter_rev, 254: wound_man_rev, 255: the_comforter_rev,
    256: lone_and_level_sands_rev, 257: misery_rev, 258: hope_rev, 259: weird_mystical_shit_rev, 260: tradition_rev,
    261: deconsecration_rev, 262: the_battle_rev, 263: the_undaunted_rev, 264: the_empty_rev, 265: the_perfomer_rev, 
    266: the_thing_rev, 267: final_tarot_rev
    }
def error_message():
    print("Sorry, I didn't recognize that input. Please enter one of the given options: ")
tarotdeck = dict1
def reverse():
    reversals = input('Would you like to use reversals in your pull? \n(y/n) \n ')
    if reversals == 'y':
        tarotdeck = dict2
    elif reversals == 'n':
        tarotdeck = dict1
    else:
        error_message()
        return reverse()
    return tarotdeck
x = len(tarotdeck)
def tarot_reader():
    reverse()
    cards = input('Would you like to pull 1 card, 3 cards, or 5 cards? \n[a] 1 \n[b] 3 \n[c] 5 \n')
    if cards == 'a':
        verify = input('You would like a single card pull, is that correct? \n(y/n) \n')
        if verify == 'y':
            return single_card()
        elif verify == 'n':
            return tarot_reader()
        else:
            error_message()
            return tarot_reader()
    elif cards == 'b':
        verify = input('You would like a three card pull, is that correct? \n(y/n) \n')
        if verify == 'y':
            return three_card()
        elif verify == 'n':
            return tarot_reader()
        else:
            error_message()
            return tarot_reader()
    elif cards == 'c':
        verify = input('You would like a five card pull, is that correct? \n(y/n) \n')
        if verify == 'y':
            return five_card()
        elif verify == 'n':
            return tarot_reader()
        else:
            error_message()
            return tarot_reader()
    else:
        error_message()
        return tarot_reader()
def single_card():
    print('Drawing your card...')
    cardpull = randint(1, x)
    pulled_card = tarotdeck[cardpull]
    print("Here is what you've pulled: ")
    print(pulled_card)
def three_card():
    card1 = ''
    card2 = ''
    card3 = ''
    print('Drawing your cards...')
    card1 = tarotdeck[randint(1, x)]
    card2 = tarotdeck[randint(1, x)]
    while card2 == card1:
        card2 = tarotdeck[randint(1, x)]
    card3 = tarotdeck[randint(1, x)]
    while card3 == card2 or card3 == card1:
        card3 = tarotdeck[randint(1, x)]
    print('This was your first card: \n ')
    print(card1, '\n ')
    print('This was your second card: \n ')
    print(card2, '\n ')
    print('And this was your third card: \n ')
    print(card3, '\n ')
def five_card():
    card1 = ''
    card2 = ''
    card3 = ''
    card4 = ''
    card5 = ''
    print('Drawing your cards...')
    card1 = tarotdeck[randint(range(x))]
    card2 = tarotdeck[randint(1, x)]
    while card2 == card1:
        card2 = tarotdeck[randint(1, x)]
    card3 = tarotdeck[randint(1, x)]
    while card3 == card2 or card3 == card1:
        card3 = tarotdeck[randint(1, x)]
    card4 = tarotdeck[randint(1, x)]
    while card4 == card3 or card4 == card2 or card4 == card1:
        card4 = tarotdeck[randint(1, x)]
    card5 = tarotdeck[randint(1, x)]
    while card5 == card4 or card5 == card3 or card5 == card2 or card5 == card1:
        card5 = tarotdeck[randint(1, x)]
    print('Your first card:')
    print(card1)
    print('Your second card:')
    print(card2)
    print('Your third card:')
    print(card3)
    print('Your fourth card:')
    print(card4)
    print('And your fifth card:')
    print(card5)
# tarot_reader()