import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))



# https://www.kitco.com/gold.londonfix.html





# https://www.perthmint.com/investment_invest_in_gold_precious_metal_prices.aspx
filename = "gold-Current.csv"
filepath = os.path.join(SCRIPT_DIR, filename)
with open (filepath) as f:
    content = f.readlines()

# remove whitespace characters like '\n' at the end of each line
content = [x.strip() for x in content]

metadata = content[:5]
content = content[5:]
content = [x for x in content if not x.endswith(',,,,,,,,,,,,,,,,,,,') ]

def format_date(dt_str):
    f0 = dt_str
    f0 = '20'+f0[7:9]+'/'+f0[4:6] + '/' + f0[1:3]
    return f0

print('\n')
for x in metadata:
    print(x)
print('')
for x in content[-20:]:
    fields = x.split(',')
    print(format_date(fields[0]), fields[13])
    #print(x)

filepath = os.path.join(SCRIPT_DIR, "gold-train.csv")
with open (filepath, 'w') as f:
    f.write("Date,Price\n")
    for x in content:
        fields = x.split(',')
        line = "{},{}\n".format(format_date(fields[0]), fields[13])
        f.write(line)
print("\nWrote to file: '%s'" % (filepath))

