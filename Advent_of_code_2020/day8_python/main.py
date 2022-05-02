import multiprocessing as mp



def day8(f,change):
    acc = 0
    pos = 0
    vpu = []
    count1 = 0
    while pos != len(f):
        action,number = f[pos].split(" ")
        if action == 'jmp' and change == count1:
            action = 'nop'
            count1+=1
        if action == 'acc':
            vpu.insert(len(vpu),pos)
            acc += int(number)
            pos += 1
        elif action == 'jmp':
            vpu.insert(len(vpu),pos)
            count1+=1
            pos += int(number)
            if change == -1 and pos in vpu:
                print("Part 1:",acc)
                break
        else:
            vpu.insert(len(vpu),pos)
            pos += 1
            continue
    if change != -1:
        print('Part 2:', acc)



if __name__ == '__main__':
    with open("data.txt", "r") as f:
        f = f.readlines()
    i = 0

    for i in range(-1,1000):
        process = mp.Process(target=day8,name='Day8',args=(f,i))
        process.start()
        process.join(0.01)
        if process.is_alive():
            process.kill()
        if str(process).rfind('exitcode=0') != -1 and i != -1:
            break