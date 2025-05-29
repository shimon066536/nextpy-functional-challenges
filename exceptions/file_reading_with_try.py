def read_file(file_name):
    try:
        f = open(file_name)
    except IOError:
        text = "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"
    else:
        text = "__CONTENT_START__\n " + f.read() + "\n__CONTENT_END__"
    finally:
        return text

# def read_file(file_name):
#     try:
#         f = open(file_name)
#         try:
#             text = "__CONTENT_START__\n " + f.read() + "\n__CONTENT_END__"
#         finally:
#             f.close()
#             return text
#     except IOError:
#         text = "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"
#         return text

print(read_file("one_lined_file.txt"))
print(read_file("file_does_not_exist.txt"))

print(read_file("one_lined_file.txt"))
print(read_file("file_does_not_exist.txt"))
