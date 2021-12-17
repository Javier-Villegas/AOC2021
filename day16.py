from timeit import default_timer as timer


hex_to_bin =  {
                '0':'0000',
                '1':'0001',
                '2':'0010',
                '3':'0011',
                '4':'0100',
                '5':'0101',
                '6':'0110',
                '7':'0111',
                '8':'1000',
                '9':'1001',
                'A':'1010',
                'B':'1011',
                'C':'1100',
                'D':'1101',
                'E':'1110',
                'F':'1111'

        }

def read_packet(packet:str) -> (int,int,int):
    i = 0
    version = to_dec(packet[i:i+3])
    i+=3
    typeid = to_dec(packet[i:i+3])
    i+=3
    if typeid == 4:
        literal = ''
        while packet[i] == '1':
            literal+= packet[i+1:i+5]
            i+=5
        literal += packet[i+1:i+5]
        i+=5
        output = to_dec(literal)  
    else:
        operators = []
        if packet[i]=='0':
            sub_packet_len = to_dec(packet[i+1:i+16])
            i+=16
            j = 0
            while i < len(packet) and j < sub_packet_len:
                (add_ver,read,op) = read_packet(packet[i:i+sub_packet_len])
                operators.append(op)
                version += add_ver
                j+=read
                i+=read
        else:
            sub_packet_num = to_dec(packet[i+1:i+12])
            i+=12
            for j in range(sub_packet_num):
                (add_ver,read,op) = read_packet(packet[i:])
                operators.append(op)
                version += add_ver
                i += read
        if typeid==0:
            output = sum(operators)
        elif typeid==1:
            output = 1 
            for mul in operators:
                output *= mul
        elif typeid==2:
            output = sorted(operators)[0] 
        elif typeid==3:
            output = sorted(operators)[-1]
        elif typeid==5:
            output = int(operators[0]>operators[1])
        elif typeid==6:
            output = int(operators[0]<operators[1])
        elif typeid==7:
            output = int(operators[0]==operators[1])


    return (version,i,output)

def to_dec(bits:str) -> int:
    return sum([2**i for i,b in enumerate(bits[::-1]) if b == '1'])

if __name__=='__main__':
    start = timer()
    with open('inputs/day16.txt','r') as f:
        packet = f.read()[:-1]
    packet_bits = ''.join([hex_to_bin[key] for key in packet])
    res = read_packet(packet_bits)

    print(f'Result part 1: {res[0]}')
    print(f'Result part 2: {res[2]}')
    print(f'Elapsed time: {timer()-start} seconds')
