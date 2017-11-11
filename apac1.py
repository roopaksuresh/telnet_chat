N = input()
case_list=[]
for i in range(N):
    case_list.append(raw_input())

string=""
for i in range(N):
    print "Case #"+str(i)+":",
    case_list[i] =  case_list[i].split()[::-1]
    for word in case_list[i]:
        print word,
    print ""
