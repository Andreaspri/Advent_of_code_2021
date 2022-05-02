def day21_part1(data):
    allergens_dict = {}
    checked = set()
    for obj in data:

        for aller in obj[1]:
            illegal = set(allergens_dict.values())
            current = set()

            for check in data:

                if aller in check[1]:
                    if aller in checked:
                        continue
                    if current:
                        current &= set(check[0])

                    else:
                        current |= set(check[0]) - illegal

            if len(current) == 1:
                try:
                    allergens_dict[aller] = list(current)[0]
                    checked.add(aller)
                except IndexError:
                    pass

    count = 0
    for i in data:
        for p in i[0]:
            if p not in allergens_dict.values():
                count += 1
    return count, allergens_dict



def day21_part2(allergen_dict):
    danger = ""
    for aller, ingre in sorted(allergen_dict.items()):
        danger += f",{ingre}"

    danger = "".join(list(danger)[1:])

    return danger

if __name__ == '__main__':
    with open("data.txt", "r") as f:
        info = f.readlines()
    info = [i.replace("\n", "") for i in info]
    info = [i.replace(")", "") for i in info]
    ingredient_allergen = []
    for line in info:
        ingredients, allergens = line.split(" (contains ")
        ingredient_allergen.append([ingredients.split(" "), allergens.split(", ")])

    safe, aller_dict = day21_part1(ingredient_allergen)

    print("Part 1:",safe)
    print("Part 2:",day21_part2(aller_dict))