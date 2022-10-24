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
    decod_str = ""
    num=''
    for i in range(len(text)):
        if str(text[i]).isdigit():            
            if str(text[i+1]).isdigit():
                num=num+text[i]
                print(num)
            # else:
            #     for j in range(int(num)):
            #         decod_str += text[i + 1]
    
    print(decod_str)

    return decod_str

decoded_string='eeerrrtwwwqquuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuredrrrrrrrrrrrrrrr'

print(rle_encoding(decoded_string))

encoded_string=rle_encoding(decoded_string)

rle_decoding(encoded_string)

a = input()
num_list = []
 
num = ''
for char in a:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))
 
print(num_list)