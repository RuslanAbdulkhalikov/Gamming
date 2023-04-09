import random

def _encoding(word):
    binary_code = ''
    temp_result = [bin(int.from_bytes(word[i].encode(), 'big'))[2:] for i in range(len(word))]
    for i in temp_result: binary_code += i + ' '
    bincode_copy = [int(i) for i in binary_code.replace(' ', '')]
    gamma = random.choices(range(0, 2), k = len(bincode_copy))
    print('gamma:', gamma)

    return f'cipher text: {[1 if not a == b else 0 for a, b in zip(bincode_copy, gamma)]}'


def _decoding(gamma, check_sum):
    a, b, one_res = 0, 7, ''
    temp_result = [1 if not a == b else 0 for a, b in zip(check_sum, gamma)]
    for i in range(len(temp_result) // 7):
        result = ''
        for j in temp_result[a:b]: result += str(j)
        one_res += chr(int(result, 2))
        a += 7
        b += 7

    return f'result: {one_res}'

print(_encoding(input('input text: ')))
print(_decoding(input('gamma: ').replace('[', '').replace(']', '').split(", "),
              input('cipher text: ').replace('[', '').replace(']', '').split(", ")))
