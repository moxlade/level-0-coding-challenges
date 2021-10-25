def common_letters(s1,s2):
    common = ""
    s3 = s1.lower()
    s4 = s2.lower()
    for i in range(len(s4)):
        if s4[i] in s3:
            if s4[i] in common:
                continue
            common = common + s4[i] + ", "
    if not common:
        return "No common letters"    

    common = common[0:-2]
    return "\'Common letters: " + common + "\'"

