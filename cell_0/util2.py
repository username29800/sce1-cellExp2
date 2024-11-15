import utils
#section 1. flag
def flag(flagFile):
    rValue = utils.auto_flag(flagFile)
    return rValue

def flagIs(flag, flagFile):
    utils.set_flag(flagFile, flag)
    return 0

def find(findFile, findValue):
    rValue = utils.auto_find(findFile, findValue)
    return rValue

def findIs(findFile, findValue, subValue):
    utils.set_find(findFile, findValue, subValue)
    return 0

def abList(source):
    rValue = utils.get_xll(source)
    return rValue

def addAB(source, addList):
    utils.write_add_all_to_xll(source, addList)
    return 0

def addABlist(source, addList):
    rv = utils.list_add_all_to_xll(source, addList)
    return rv

def delAB(source, delList):
    utils.write_del_all_from_xll(source, delList)

def delABlist(source, delList):
    rv = utils.list_del_all_from_xll(source, delList)
    return rv

def findT(ab, scan):
    rv = utils.xll_find_match(ab, scan)
    return rv

def findTF(ab, scan):
    rv = utils.xll_find_missing(ab, scan)
    return rv

def findF(ab, scan):
    rv = utils.xll_find_unknown(ab, scan)
    return rv