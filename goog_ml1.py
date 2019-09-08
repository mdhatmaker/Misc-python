#import sklearn
from sklearn import tree

# Example of using enum function:
# Color = enum(RED='red', GREEN='green', BLUE='blue')
# print Color.RED
def enum(**named_values):
    return type('Enum', (), named_values)

###############################################################################

#features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
#labels = ["apple", "apple", "orange", "orange"]
features = [[140, 0], [130, 0], [150, 1], [170, 1]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[160,1]])


Outlook = enum(SUNNY=0, OVERCAST=1, RAINY=2)

features = [[Outlook.SUNNY,85,85,0], [Outlook.SUNNY,80,90,1], [Outlook.OVERCAST,83,86,0],
[Outlook.RAINY,70,96,0], [Outlook.RAINY,68,80,0], [Outlook.RAINY,65,70,1],
[Outlook.OVERCAST,64,65,1], [Outlook.SUNNY,72,95,0], [Outlook.SUNNY,69,70,0],
[Outlook.RAINY,75,80,0], [Outlook.SUNNY,75,70,1], [Outlook.OVERCAST,72,90,1],
[Outlook.OVERCAST,81,75,0], [Outlook.RAINY,71,91,1]]

labels = [0,0,1,1,1,0,1,0,1,1,1,1,1,0]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[Outlook.RAINY,55,75,1]])
print clf.predict([[Outlook.RAINY,71,91,1]])


"""
@attribute outlook {sunny, overcast, rainy}
@attribute temperature numeric
@attribute humidity numeric
@attribute windy {TRUE, FALSE}
@attribute play {yes, no}

@data
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,72,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no
"""

print "Done."


