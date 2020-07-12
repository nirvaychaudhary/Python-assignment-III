def write(file, content):
    file = open(file, 'w+')
    file.write(content)
    file.close()
