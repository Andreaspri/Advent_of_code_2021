
import matplotlib.pyplot as plt

def parse_data():
    with open("data.txt") as f:
        data = f.readlines()

    folds = []
    cords = set()
    for line in data:
        if ',' in line:
            x, y = line.split(',')
            cords.add((int(x),int(y)))
        else:
            if 'x' in line:
                folds.append('x'+line.split("fold along x=")[1])
            elif 'y' in line:
                folds.append('y'+line.split("fold along y=")[1])
    return folds, cords




def part_1(folds, cords):

    for fold in folds:
        new_cords = set()
        if 'x' in fold:
            fold_point = int(fold.split("x")[1])
            for cord in cords:
                if cord[0] > fold_point:
                    new_cords.add((fold_point - (cord[0] - fold_point),cord[1]))
                else:
                    new_cords.add(cord)
        else:
            fold_point = int(fold.split("y")[1])
            for cord in cords:
                if cord[1] > fold_point:
                    new_cords.add((cord[0], fold_point - (cord[1] - fold_point)))
                else:
                    new_cords.add(cord)


        break

    return len(new_cords)









def part_2(folds, cords):

    for fold in folds:
        new_cords = set()
        if 'x' in fold:
            fold_point = int(fold.split("x")[1])
            for cord in cords:
                if cord[0] > fold_point:
                    new_cords.add((fold_point - (cord[0] - fold_point), cord[1]))
                else:
                    new_cords.add(cord)
        else:
            fold_point = int(fold.split("y")[1])
            for cord in cords:
                if cord[1] > fold_point:
                    new_cords.add((cord[0], fold_point - (cord[1] - fold_point)))
                else:
                    new_cords.add(cord)

        cords = new_cords

    plt.plot([i[0] for i in new_cords],[[-i[1]] for i in new_cords],'bo')
    plt.axis([-15,50,-20,20])

    plt.show()




if __name__ == '__main__':
    total_folds,coordinates = parse_data()
    print(part_1(total_folds, coordinates))
    part_2(total_folds, coordinates)
