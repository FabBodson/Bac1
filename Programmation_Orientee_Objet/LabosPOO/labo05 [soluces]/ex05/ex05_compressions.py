def to_bin(number):
    result = number.to_bytes(1, byteorder='big', signed=False)
    return result


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


if __name__ == '__main__':
    lzw = LZW()
    with open('data/tobeornottobe.txt') as source:
        with open('data/output.compress.bin', 'wb') as destination:
            lzw.compress(source, destination)
