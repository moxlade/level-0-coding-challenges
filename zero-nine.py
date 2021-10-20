def vowel_check(s):
    
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    output = " "
    c = s.lower() 
    
    for j in range(len(c)):
            if c[j] in vowels:
                if  c[j] in output:
                    continue
                else:
                    output = output + c[j] + ", "

    output = output[0:-2]

    return "Vowels: " + output






                
