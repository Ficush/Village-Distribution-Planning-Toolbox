# coding:utf-8

import arcpy
import math
import sys

reload(sys)

sys.setdefaultencoding('utf8')

obj = arcpy.GetParameterAsText(0)

errorCount = 0

# Function: Check the point data's validity ---------------------------------

def pointCheck(row):
    
    def informMessage(message):
        string = ""
        global errorCount
        string += "错误：{0} 中的 {1}".format(row[8],row[3])
        string += "（OBJECTID = {0}）".format(row[2])
        string += message
        arcpy.AddMessage(string)
        errorCount += 1

    if row[3] == "":
        informMessage("缺少自然村名！")

    if row[8] == "":
        informMessage("缺少乡镇名！")

    if row[4] not in [0,1]:
        informMessage("字段 INSIDE 的取值只能是 0、1 ！")

    if row[5] not in [1,2,3]:
        informMessage("字段 CLASS 的取值只能是 1、2、3 ！")

    if row[6] < 0:
        informMessage("字段 BELONG 的取值不能是负数！")

    if row[7] < 0:
        informMessage("字段 PSUM 的取值不能是负数！")

    if row[12] not in [0,1]:
        informMessage("字段 SPECIAL 的取值只能是 0、1 ！")

    if row[10] == 0:
        if row[4] == 0:
            if row[11] == 2:
                informMessage("非已建成集中安置区，预定义不应设为重点村")
        else:
            if row[11] != 1:
                informMessage("在镇区影响区范围内，且非已建成集中安置区，预定义应设为一般村")
    elif row[10] == 1:
        if row[4] == 0:
            if row[11] != 2:
                informMessage("在镇区影响区范围外，且是已建成集中安置区，预定义应设为重点村")
        else:
            if row[11] == 0:
                informMessage("在镇区影响区范围内，且是已建成集中安置区，必须对其进行预定义")
    else:
        informMessage("字段 PREBUILD 的取值只能是 0、1 ！")

    if row[11] == 0:
        if row[12] == 0:
            if row[5] == 3:
                informMessage("未被预定义为特色村，但最终分类为特色村")
        else:
            if row[5] == 1:
                informMessage("已被预定义为特色村，但最终分类为一般村")
    elif row[11] == 1:
        if row[12] == 0:
            if row[5] != 1:
                informMessage("已被预定义为一般村，且没有被定义为特色村，但最终分类不是一般村")
        else:
            if row[5] == 2:
                informMessage("已被预定义为一般村，但最终分类为重点村")
    elif row[11] == 2:
        if row[5] != 2:
                informMessage("已被预定义为重点村，但最终分类不是重点村")
    else:
        informMessage("字段 PREDEFINE 的取值只能是 0、1、2 ！")


    if row[5] == 1:
        if row[4] == 0:
            if row[6] == 0:
                informMessage("在镇区影响区范围外，且最终分类为一般村，应设其将定合并至的重点村")
        else:
            if row[6] != 0:
                informMessage("在镇区影响区范围内，且最终分类为一般村，应合并至镇区而非其他重点村")
    else:
        if row[6] != 0:
            informMessage("是重点村或特色村，不应合并至其他重点村")
        if row[9] == "":
            informMessage("是重点村或特色村，请指定村庄发展类型：一级发展村庄或二级发展村庄")


    if row[6] != 0:
        if row[7] != 0:
            informMessage("非重点村，但具有引力模型合并人口规模")
    else:
        if row[5] == 2:
            if row[7] <= 0:
                informMessage("为重点村，但缺少引力模型合并人口规模")
        else:
            if row[5] == 3:
                if row[7] != 0:
                    informMessage("为特色村，不应具有引力模型合并人口规模")

# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------

field = [
    "SHAPE@X",
    "SHAPE@Y",
    "OBJECTID",
    "ZRCM",
    "INSIDE",
    "CLASS",
    "BELONG",
    "PSUM",
    "XZ",
    "FZCZFJ",
    "PREBUILD",
    "PREDEFINE",
    "SPECIAL"
]

rows = arcpy.da.SearchCursor(obj, field)

for row in rows:

    pointCheck(row)

if errorCount == 0:
    arcpy.AddMessage("成功：本乡镇所有村庄均通过检查！")
else:
    arcpy.AddMessage("警告：本乡镇共发现 {0} 个错误！".format(errorCount))