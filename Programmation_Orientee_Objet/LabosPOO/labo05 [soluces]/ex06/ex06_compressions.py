def to_bin(number):
    result = number.to_bytes(1, byteorder='big', signed=False)
    print(number, '>', result)
    return result


def from_bin(code):
    return int.from_bytes(code, 'big')


class LZW:

    def __generate_dictionary(self):
        return {letter: i for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ \t\r\n')}

    def compress(self, source, destination):
        dictionary = self.__generate_dictionary()
        word = ''
        while True:
            char = source.read(1)
            if len(char) != 1:
                break
            key = word + char
            if key in dictionary:
                word = key
            else:
                dictionary[key] = len(dictionary)
                destination.write(to_bin(dictionary[word]))
                word = char
        destination.write(to_bin(dictionary[word]))

    def decompress(self, source, destination):
        dictionary = self.__generate_dictionary()
        reverse = { value: key for key, value in dictionary.items()}
        code = from_bin(source.read(1))
        saved = reverse[code]
        destination.write(saved)

        while True:
            code = source.read(1)
            if len(code) != 1:
                break
            code = from_bin(code)
            value = reverse[code] if code in reverse else saved + saved[0]
            destination.write(value)
            reverse[len(reverse)] = saved + value[0]
            saved = value


if __name__ == '__main__':
    lzw = LZW()
    with open('data/tobeornottobe.txt') as source:
        with open('data/output.compress.bin', 'wb') as destination:
            lzw.compress(source, destination)

    with open('data/output.compress.bin', 'rb') as source:
        with open('data/decompressed.txt', 'w') as destination:
            lzw.decompress(source, destination)
