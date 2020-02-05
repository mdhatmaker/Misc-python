import pyperclip
import sys


# take clipboard contents in format "xxxxxx,yyyyyyyyyyy\nqqqqqq,rrrr\n..."
# and format this text in Python dictionary format (placed BACK into the clipboard)
def format_clipboard_as_python_dict():
    clip = pyperclip.paste()
    lines = clip.split('\n')
    output = "{\n"
    for pair in lines:
        symdesc = pair.split(',')
        output += '"{0}":"{1}",\n'.format(symdesc[0], symdesc[1])
    output += "}"
    pyperclip.copy(output)
    return output



coinTrans = {
    "zec":"Zcash",
    "xmr":"Monero",
    "dsh":"Dash",
    "bcu":"BitConnect",
    "btc":"Bitcoin",
    "ltc":"Litecoin",
    "eth":"Ethereum",
    "etc":"EthereumClassic",
    "xrp":"Ripple",
    "iot":"IOTA",
    "eos":"EOS",
    "omg":"OmiseGO",
    "bch":"BitcoinCash",
    "neo":"NEO",
    "etp":"MetaverseETP",
    "qtm":"Qtum",
    "edo":"Eidoo",
}

currencyTrans = {
    "usd":"USDollar", "gbp":"Pound", "cny":"ChineseYuan", "jpy":"Yen"
}

#print format_clipboard_as_python_dict()
#sys.exit()



f = open("/Users/michael/Dropbox/alvin/data/MISC/BitfinexSymbols.txt", 'r')


start = False
for line in f:
    line = line.strip()
    for k in coinTrans:
        found = False
        if k in line:
            found = True
            
    if found == True: continue
    
    if line[0:6] == "avtusd":
        start = True
    if start == False:
        continue
    
    if len(line) == 0:
        continue
    elif len(line) == 6:
        print line,
    elif line[:5] == '"mid"' or line[:5] == '"low"':
        print line,
    elif line[:6] == '"high"':
        print line
    
