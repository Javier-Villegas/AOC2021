from timeit import default_timer as timer

if __name__=='__main__':
    start = timer()
    res1 = 0
    res2 = 0
    with open('inputs/day8.txt','r') as f:
        while(line:=f.readline()):
            (signals,output) = line.split(' | ')
            signals = signals.split(' ')
            output = output[:-1].split(' ')
            digits = ['','','','','','',' ','','','']
            out = ''
            for s in signals:
                if len(s)==2:
                    digits[1]=set(s)
                elif len(s)==4:
                    digits[4]=set(s)
                elif len(s)==3:
                    digits[7]=set(s)
                elif len(s)==7:
                    digits[8]=set(s)
            for s in signals:
                s = set(s)
                if len(s) == 6 and len(s.intersection(set(digits[1])))==1:
                    digits[6] = s 
                elif len(s) == 6 and len(s.intersection(set(digits[4])))==3:
                    digits[0] = s 
                elif len(s) == 6 and len(s.intersection(set(digits[4])))==4:
                    digits[9] = s 
                elif len(s) == 5:
                    if len(s.intersection(set(digits[4])))==3:
                        if len(s.intersection(set(digits[1])))==1:
                            digits[5] = s
                        else:
                            digits[3] = s
                    else:
                        digits[2] = s
            for o in output:
                o = set(o)
                if o == digits[0]:
                    out+='0'
                elif o == digits[1]:
                    out+='1'
                    res1+=1
                elif o == digits[2]:
                    out+='2'
                elif o == digits[3]:
                    out+='3'
                elif o == digits[4]:
                    out+='4'
                    res1+=1
                elif o == digits[5]:
                    out+='5'
                elif o == digits[6]:
                    out+='6'
                elif o == digits[7]:
                    out+='7'
                    res1+=1
                elif o == digits[8]:
                    out+='8'
                    res1+=1
                else:
                    out+='9'
            res2 += int(out)

    print(f'Result part 1: {res1}')
    print(f'Result part 2: {res2}')
    end = timer()
    print(f'Elapsed time: {end-start} seconds')
