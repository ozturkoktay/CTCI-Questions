

def compress_string(string):
    compressed_string = ''
    count = 0

    for i in range(len(string)):
        count += 1

        if i + 1 >= len(string) or string[i] != string[i+1]:
            compressed_string += '' + string[i] + str(count)
            count = 0

    return compressed_string


assert compress_string('aabcccccaaa') == 'a2b1c5a3'

