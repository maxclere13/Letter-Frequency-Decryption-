
# English letter Frequency reference
lst = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327,	0.09056, 0.02758, 0.00978, 0.02360,	0.00150, 0.01974,	0.00074]

ctFreqList = []


ciphertext='lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb'


def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
  
  # Using min() method we apply a key that finds the absolute difference of each element with K, and returns the element having minimum difference. 

def letterCount():

  cipherText='lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb'

  letterA="a"

  countA = cipherText.count(letterA)

  print("The letter" ,letterA, "appears" ,countA, "times.")

  letterB="b"

  countB = cipherText.count(letterB)

  print("The letter" ,letterB, "appears" ,countB, "times.")

  letterC="c"

  countC = cipherText.count(letterC)

  print("The letter" ,letterC, "appears" ,countC, "times.")

  letterD="d"

  countD = cipherText.count(letterD)

  print("The letter" ,letterD, "appears" ,countD, "times.")

  letterE="E"

  countE = cipherText.count(letterE)

  print("The letter" ,letterE, "appears" ,countE, "times.")

  letterF="f"

  countF = cipherText.count(letterF)

  print("The letter" ,letterF, "appears" ,countF, "times.")

  letterG="g"

  countG = cipherText.count(letterG)

  print("The letter" ,letterG, "appears" ,countG, "times.")

  letterH="h"

  countH = cipherText.count(letterH)

  print("The letter" ,letterH, "appears" ,countH, "times.")

  letterI="i"

  countI = cipherText.count(letterI)

  print("The letter" ,letterI, "appears" ,countI, "times.")

  letterJ="j"

  countJ = cipherText.count(letterJ)

  print("The letter" ,letterJ, "appears" ,countJ, "times.")

  letterK="k"

  countK = ciphertext.count(letterK)

  print("The letter" ,letterK, "appears" ,countK, "times.")

  letterL="l"

  countL = cipherText.count(letterL)

  print("The letter" ,letterL, "appears" ,countL, "times.")

  letterM="m"

  countM = cipherText.count(letterM)

  print("The letter" ,letterM, "appears" ,countM, "times.")

  letterN="n"

  countN = cipherText.count(letterN)

  print("The letter" ,letterN, "appears" ,countN, "times.")

  letterO="O"

  countO = cipherText.count(letterO)

  print("The letter" ,letterO, "appears" ,countO, "times.")

  letterP="p"

  countP = cipherText.count(letterP)

  print("The letter" ,letterP, "appears" ,countP, "times.")

  letterQ="q"

  countQ = cipherText.count(letterQ)

  print("The letter" ,letterQ, "appears" ,countQ, "times.")

  letterR="r"

  countR = cipherText.count(letterR)

  print("The letter" ,letterR, "appears" ,countR, "times.")

  letterS="s"

  countS = cipherText.count(letterS)

  print("The letter" ,letterS, "appears" ,countS, "times.")

  letterT="t"

  countT = cipherText.count(letterT)

  print("The letter" ,letterT, "appears" ,countT, "times.")

  letterU="u"

  countU = cipherText.count(letterU)

  print("The letter" ,letterU, "appears" ,countU, "times.")

  letterV="v"

  countV = cipherText.count(letterV)

  print("The letter" ,letterV, "appears" ,countV, "times.")

  letterW="w"

  countW = cipherText.count(letterW)

  print("The letter" ,letterW, "appears" ,countW, "times.")

  letterX="x"

  countX = cipherText.count(letterX)

  print("The letter" ,letterX, "appears" ,countX, "times.")

  letterY="y"

  countY = cipherText.count(letterY)

  print("The letter" ,letterY, "appears" ,countY, "times.")

  letterZ="z"

  countZ = cipherText.count(letterZ)

  print("The letter" ,letterZ, "appears" ,countZ, "times.")

  totalCount= countA + countB + countC + countD + countE + countF + countG+ countH + countI + countJ + countK + countL + countM + countN + countO+ countP + countQ + countR + countS + countT + countU + countV + countW+ countX + countY + countZ 
  
  # totalCount of all letters in the cipherText

  print("")

  print("Letter a frequency:" ,countA/totalCount)
  ctFreqList.insert(1, countA/totalCount)

  print("Letter b frequency:" ,countB/totalCount)
  ctFreqList.insert(2, countB/totalCount)

  print("Letter c frequency:" ,countC/totalCount)
  ctFreqList.insert(3, countC/totalCount)

  print("Letter d frequency:" ,countD/totalCount)
  ctFreqList.insert(4, countD/totalCount)

  print("Letter e frequency:" ,countE/totalCount)
  ctFreqList.insert(5, countE/totalCount)

  print("Letter f frequency:" ,countF/totalCount)
  ctFreqList.insert(6, countF/totalCount)

  print("Letter g frequency:" ,countG/totalCount)
  ctFreqList.insert(7, countG/totalCount)

  print("Letter h frequency:" ,countH/totalCount)
  ctFreqList.insert(8, countH/totalCount)

  print("Letter i frequency:" ,countI/totalCount)
  ctFreqList.insert(9, countI/totalCount)

  print("Letter j frequency:" ,countJ/totalCount)
  ctFreqList.insert(10, countJ/totalCount)

  print("Letter k frequency:" ,countK/totalCount)
  ctFreqList.insert(11, countK/totalCount)

  print("Letter l frequency:" ,countL/totalCount)
  ctFreqList.insert(12, countL/totalCount)

  print("Letter m frequency:" ,countM/totalCount)
  ctFreqList.insert(13, countM/totalCount)

  print("Letter n frequency:" ,countN/totalCount)
  ctFreqList.insert(14, countN/totalCount)

  print("Letter o frequency:" ,countO/totalCount)
  ctFreqList.insert(15, countO/totalCount)

  print("Letter p frequency:" ,countP/totalCount)
  ctFreqList.insert(16, countP/totalCount)

  print("Letter q frequency:" ,countQ/totalCount)
  ctFreqList.insert(17, countQ/totalCount)

  print("Letter r frequency:" ,countR/totalCount)
  ctFreqList.insert(18, countR/totalCount)

  print("Letter s frequency:" ,countS/totalCount)
  ctFreqList.insert(19, countS/totalCount)

  print("Letter t frequency:" ,countT/totalCount)
  ctFreqList.insert(20, countT/totalCount)

  print("Letter u frequency:" ,countU/totalCount)
  ctFreqList.insert(21, countU/totalCount)

  print("Letter v frequency:" ,countV/totalCount)
  ctFreqList.insert(22, countV/totalCount)

  print("Letter w frequency:" ,countW/totalCount)
  ctFreqList.insert(23, countW/totalCount)

  print("Letter x frequency:" ,countX/totalCount)
  ctFreqList.insert(24, countX/totalCount)

  print("Letter y frequency:" ,countY/totalCount)
  ctFreqList.insert(25, countY/totalCount)

  print("Letter z frequency:" ,countZ/totalCount)
  ctFreqList.insert(26, countZ/totalCount)

#main function
letterCount()

cipherText='lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb'

print("")
##decryption dictionary based on freq analysis
decryptDict ={'r': 'e',
            'b': 't',
            'm': 'a',
            'j': 'o',
            'w': 'i',
            'i': 's',
            'p': 'h',
            'u': 'r',
            'v': 'c',
            'x': 'f',
            's': 'p',
            'q': 'k',
            'k': 'n',
            'l': 'b',
            'n': 'u',
            'o': 'g',
            'y': 'm',
            't': 'y',
            'h': 'l',
            'e': 'v',
            'a': 'x',
            'c': 'w',
            'f': 'q',
            'g': 'z'}

x = "" 


for i in cipherText:   #for loop to print out the decrypted text
  if i in decryptDict: 
    x += decryptDict[i] 
  else: 
    x += i  # if no  add the regular character 
print("The resulting decryption is: \n")
print(x) # prints the resulting string after the loops above
