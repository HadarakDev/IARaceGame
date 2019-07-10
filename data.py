def declareTiles():
    tilesDic = {}
    
    tilesDic["left"] = []
    tilesDic["right"] = []
    tilesDic["top"] = []
    tilesDic["bot"] = []

    tilesDic["cornerTL"] = {}
    tilesDic["cornerTL"]["symbol"] = "/"
    tilesDic["cornerTL"]["output_left"] = "bot"
    tilesDic["cornerTL"]["output_top"] = "right"

    tilesDic["horizontal"] = {}
    tilesDic["horizontal"]["symbol"] = "="
    tilesDic["horizontal"]["output_left"] = "left"
    tilesDic["horizontal"]["output_right"] = "right"

    tilesDic["vertical"] = {}
    tilesDic["vertical"]["symbol"] = "|"
    tilesDic["vertical"]["output_bot"] = "bot"
    tilesDic["vertical"]["output_top"] = "top"

    tilesDic["cornerTR"] = {}
    tilesDic["cornerTR"]["symbol"] = "\\"
    tilesDic["cornerTR"]["output_right"] = "bot"
    tilesDic["cornerTR"]["output_top"] = "left"

    tilesDic["cornerBL"] = {}
    tilesDic["cornerBL"]["symbol"] = "("
    tilesDic["cornerBL"]["output_bot"] = "right"
    tilesDic["cornerBL"]["output_left"] = "top"

    tilesDic["cornerBR"] = {}
    tilesDic["cornerBR"]["symbol"] = ")"
    tilesDic["cornerBR"]["output_right"] = "top"
    tilesDic["cornerBR"]["output_bot"] = "left"

    tilesDic["left"].extend((tilesDic["cornerTL"], tilesDic["horizontal"], tilesDic["cornerBL"]))
    tilesDic["right"].extend((tilesDic["cornerBR"], tilesDic["horizontal"], tilesDic["cornerTR"]))
    tilesDic["bot"].extend((tilesDic["cornerBR"], tilesDic["vertical"], tilesDic["cornerBL"]))
    tilesDic["top"].extend((tilesDic["cornerTL"], tilesDic["vertical"], tilesDic["cornerTR"]))
    return tilesDic

def declareDirection():
    directionDic = {}
    directionDic["top"] = {}
    directionDic["bot"] = {}
    directionDic["left"] = {}
    directionDic["right"] = {}

    directionDic["top"]["x"] = 0
    directionDic["top"]["y"] = -1
    directionDic["bot"]["x"] = 0
    directionDic["bot"]["y"] = 1
    directionDic["left"]["x"] = -1
    directionDic["left"]["y"] = 0
    directionDic["right"]["x"] = 1
    directionDic["right"]["y"] = 0
    return directionDic