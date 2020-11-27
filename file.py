def main():
    s = ""
    for i in range(1000000):
        s += str(i) + ","
    s += str(-1) + "\n"
    f = open('info.txt', 'wb')
    f.write(s)
    f.close()


main()
