def common_letters(s1,s2):
    common = ""
    for i in range(len(s2)):
        if s2[i] in s1:
            if s2[i] in common:
                continue
            common = common + s2[i] + ", "
    if not common:
        return "No common letters"    

    common = common[0:-2]
    return "\'Common letters: " + common + "\'"

