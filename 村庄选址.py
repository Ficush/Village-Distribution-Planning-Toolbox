import arcpy
import math

obj    = arcpy.GetParameterAsText(0)
radius = arcpy.GetParameter(1)

# Function: Calculate the distance between two villages ---------------------

def distance(x1,y1,x2,y2):

    return math.sqrt((x1-x2)**2+(y1-y2)**2)

# ---------------------------------------------------------------------------

# Function: Clean the villages in the radius --------------------------------

def cleanVillage(position):

    rows = arcpy.da.UpdateCursor(obj,["SHAPE@X","SHAPE@Y","CLASS","SCORE","ID"],'"CLASS" = 0')

    max_x = position[0]
    max_y = position[1]
    max_score = max_id = 0

    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！
    # ！！！此部分为核心代码，因知识产权原因无法提供！！！

    return max_id

# ---------------------------------------------------------------------------

# Function: To find the max village -----------------------------------------

def findMaxVillage():

    rows = arcpy.da.SearchCursor(obj,["SCORE","ID"],'"CLASS" = 0')

    max_score = max_id = 0

    for row in rows:
        if max_score < row[0]:
            max_score = row[0]
            max_id = row[1]

    return max_id

# ---------------------------------------------------------------------------

# Function: Return the position of the input village ------------------------

def getPosition(id):

    rows = arcpy.da.UpdateCursor(obj,["SHAPE@X","SHAPE@Y","CLASS"],'"ID" = ' + str(id))

    max_x = max_y = 0

    for row in rows:
        max_x = row[0]
        max_y = row[1]
        row[2] = 2
        rows.updateRow(row)

    return (max_x,max_y)

# ---------------------------------------------------------------------------

rows = arcpy.da.SearchCursor(obj,["SHAPE@X","SHAPE@Y"],'"CLASS" = 2')

for row in rows:
    cleanVillage((row[0],row[1]))

max_id = findMaxVillage()

while 1:

    max_id = cleanVillage(getPosition(max_id))

    if max_id == 0:
        max_id = findMaxVillage()
        if max_id == 0:
            break
    else:
        continue