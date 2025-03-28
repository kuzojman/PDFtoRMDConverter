from PDF2RMDConverter import pdf2rmdconverter

while True:
    print('введите путь к файлу / для завершения работы введите N или нажэмите ctr+c')
    l = str(input())
    if l == 'N':
        break
    l = l.replace('\\', '/').replace("\"", "")
    list_l = l.split(" ")

    pdf2rmdconverter.convert(list_l)
    