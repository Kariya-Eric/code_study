try:
    source_file = open("./data.txt", "rb")
    dest_file = open("./data_copy.txt", "ab")
    for line in source_file.readlines():
        dest_file.write(line)
except Exception as e:
    print(e)
finally:
    dest_file.close()
    source_file.close()
