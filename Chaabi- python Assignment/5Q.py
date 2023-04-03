def CompareLists(list1, list2):
    intersection = list(set(list1).intersection(set(list2)))
    symmetric_difference = list(set(list1).symmetric_difference(set(list2)))
    return intersection, symmetric_difference

mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]


SetIntersection, SetSymmetricDifference = CompareLists(mainstream, must_watch)
print(SetIntersection)
print(SetSymmetricDifference)

