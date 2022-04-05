# print("Hi this is Anshul 🚀")

# print("🌈🌈🌈🌈🌈🌈")

# print('\x1b[13;31;43m' + 'Hello world!' + '\x1b[0m') #https://www.geeksforgeeks.org/formatted-text-linux-terminal-using-python/

#http://www.figlet.org/examples.html
#https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b
#pip install pyfiglet
#pip install termcolor
from pyfiglet import Figlet
from termcolor import colored

f=Figlet(font='starwars') # banner3-D,jerusalem,isometric2,starwars
# print(colored(f.renderText('CV&DL'),'white'))
print(f.renderText('CV&DL'))

# print(Figlet(font='starwars').renderText('CV&DL'))

from termcolor import colored
print(colored("Anshul",color='green', on_color='on_yellow', attrs=None))

'''
Docstring:
Colorize text.

Available text colors:
    red, green, yellow, blue, magenta, cyan, white.

Available text highlights:
    on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

Available attributes:
    bold, dark, underline, blink, reverse, concealed.
'''

'''
['3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner', 'banner3-D', 'banner3', 'banner4',
 'barbwire', 'basic', 'bell', 'big', 'bigchief', 'binary', 'block', 'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk', 'chunky',
 'coinstak', 'colossal', 'computer', 'contessa', 'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 
 'cybersmall', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'drpepper', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic',
 'eftiwall', 'eftiwater', 'epic', 'fender', 'fourtops', 'fuzzy', 'goofy', 'gothic', 'graffiti', 'hollywood', 'invita', 'isometric1', 
 'isometric2', 'isometric3', 'isometric4', 'italic', 'ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban', 'larry3d', 'lcd', 'lean', 
 'letters', 'linux', 'lockergnome', 'madrid', 'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'mnemonic', 'morse', 'moscow', 'nancyj-fancy',
 'nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'o8', 'ogre', 'pawp', 'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid',
 'rectangles', 'relief', 'relief2', 'rev', 'roman', 'rot13', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sblood', 'script',
 'serifcap', 'shadow', 'short', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 
 'smtengwar', 'speed', 'stampatello', 'standard', 'starwars', 'stellar', 'stop', 'straight', 'tanja', 'tengwar', 'term', 'thick', 
 'thin', 'threepoint', 'ticks', 'ticksslant', 'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint', 'univers', 'usaflag', 'wavy', 
 'weird']
'''