import arcpy
import math

obj = arcpy.GetParameterAsText(0)

arcpy.CalculateField_management(obj, "BELONG","0","PYTHON_9.3")
arcpy.CalculateField_management(obj, "PSUM","0","PYTHON_9.3")

# Function: Calculate the distance between two villages ---------------------

def distance(x1,y1,x2,y2):

    return math.sqrt((x1-x2)**2+(y1-y2)**2)

# ---------------------------------------------------------------------------

# Function: To find the max gravity villages --------------------------------

def findMaxVillage(x1,y1):

    gravity = max_gravity = max_id = 0

    rows = arcpy.da.SearchCursor(obj,["SHAPE@X","SHAPE@Y","SCORE","ID"],'"CLASS" = 2')

    for row in rows:

        x2 = row[0]
        y2 = row[1]

        d = distance(x1,y1,x2,y2)

        if d != 0:
            gravity = row[2] / (d * d)
            if max_gravity <= gravity:
                max_gravity = gravity
                max_id = row[3]

    return max_id

# ---------------------------------------------------------------------------

# Function: Calculate the sum population of village -------------------------

def population(id,pop):

    rows = arcpy.da.SearchCursor(obj,["POP"],'"CLASS" = 1 and BELONG = ' + str(id))

    for row in rows:
        pop += row[0]

    return pop

# ---------------------------------------------------------------------------

rows = arcpy.da.UpdateCursor(obj,["SHAPE@X","SHAPE@Y","BELONG"],'"CLASS" = 1 and "INSIDE" = 0')

for row in rows:

    max_id = findMaxVillage(row[0],row[1])

    if max_id != 0:
        row[2] = max_id
        rows.updateRow(row)
    else:
        pass

rows = arcpy.da.UpdateCursor(obj,["ID","POP","PSUM"],'"CLASS" = 2')

for row in rows:

    pop = population(row[0],row[1])

    if pop != 0:
        row[2] = pop
        rows.updateRow(row)
    else:
        pass