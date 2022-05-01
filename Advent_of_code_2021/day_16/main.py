





def literal_number(binary):

    current_binary_number = '1'
    full_binary_number = ""
    while current_binary_number[0] == '1':
        current_binary_number = binary[:5]
        binary = binary[5:]
        full_binary_number += current_binary_number[1:]

    return binary, int(full_binary_number,2)


def part_1():
    with open("data.txt") as f:
        data = f.read()


    binary = bin(int(data,16))[2:]
    if len(binary) % 4 != 0:
        binary = '0' * (4 - (len(binary) % 4)) + binary


    version_count = 0

    while True:
        version = binary[:3]
        version_count += int(version,2)
        binary = binary[3:]
        pack_id = binary[:3]
        binary = binary[3:]


        if int(pack_id,2) == 4:
            binary, number = literal_number(binary)
        else:
            length_id = binary[:1]
            binary = binary[1:]
            if length_id == '1':
                binary = binary[11:]
            else:
                binary = binary[15:]


        if all(i == '0' for i in binary):
            return version_count


def part_2(binary, sub_packets=None, sub_length=None):
    with open("data.txt") as f:
        data = f.read()


    binary = bin(int(data,16))[2:]
    if len(binary) % 4 != 0:
        binary = '0' * (4 - (len(binary) % 4)) + binary


    while True:

        binary = binary[3:]
        pack_id = binary[:3]
        binary = binary[3:]


        if pack_id == 0:
            length_id = binary[:1]
            binary = binary[1:]
            if length_id == '1':
                new_sub_packets = int(binary[:11],2)
                binary = binary[11:]
            return sum(part_2(binary))

        if int(pack_id,2) == 4:
            binary, number = literal_number(binary)
        else:
            length_id = binary[:1]
            binary = binary[1:]
            if length_id == '1':
                binary = binary[11:]
            else:
                binary = binary[15:]






if __name__ == '__main__':
    print(part_1())
