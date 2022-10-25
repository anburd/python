def rle_encoding(incom_str):

    encod_str = ""
    prev_char = incom_str[0]
    count = 0

    for i in incom_str:
        if i == prev_char:
            count += 1
        else:
            encod_str += str(count) + prev_char
            prev_char = i
            count = 1
    encod_str += str(count) + prev_char

    return encod_str

def rle_decoding(text):
    decod_str = ''
    num=0
    digit =''
    for i in range(len(text)):
        if str(text[i]).isdigit():
            digit  = digit  + str(text[i])
        else: 
            if digit != '':
                for j in range(int(digit)):
                    decod_str += text[i]                  
                print(digit)
                digit =''
        
    return decod_str

my_string='uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuredrrrrrrrrrrrrrrreeerrrtwwwq'


print(my_string)
coded_string=rle_encoding(my_string)
print(coded_string)

print(rle_decoding(coded_string))

