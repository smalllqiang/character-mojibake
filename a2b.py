# -*- coding: utf-8 -*-


import codecs
import sys

codes = ["ASCII", "UTF-8", "UTF-16", "UTF-32", "ISO-8859-1", "ISO-8859-15", "GB2312", "GBK", "GB18030", "Big5", "Shift_JIS", "EUC-JP", "Punycode", "Windows-1252", "KOI8-R"]
unsupportedcodes = ["MIME", "URL encoding", "Huffman coding", "LZW", "Run-length encoding", "Morse code", "Braille", "Binary code", "Hexadecimal", "BCD", "Gray code", "ASCII-8BIT", "TSCII"]
othercodes = ["Base64", "Quoted-printable"]


# 检查是否安装了...
for i in codes:
    try:
        codecs.lookup(i)
        print(f"支持 {i}")
    except LookupError:
        print(f"\n***不支持 {i} \n")

for i in unsupportedcodes:
    try:
        codecs.lookup(i)
        print(f"支持 {i}")
    except LookupError:
        print(f"\n***不支持 {i} \n")






encode_string_dict = {}
input_string = input("请输入一串字符串: ")
for i in codes:
    try:
        encode_string = input_string.encode(i)
        print(f"{i} 的編碼結果爲 {encode_string}")
        encode_string_dict[i] = encode_string
    except UnicodeEncodeError:
        print(f"不能被 {i} 編碼")

#print(encode_string_list)
ablecode_list = list(encode_string_dict.keys())
result = []
for i in ablecode_list:
    #print(f"使用 {i} 編碼得到 {encode_string}")
    for j in codes:
        try:
            decode_string = encode_string_dict[i].decode(j)
            result.append(decode_string)
            print(f"使用 {i} 編碼, {j}解碼, 得到的結果爲 ***{decode_string}***")
        except UnicodeDecodeError:
            #print(f"使用 {j} 解碼失敗")
            continue

for i in result:
    print(i)


input("")