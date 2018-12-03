# python中的输入和输出
s = "hello world"
print(str(s))
print(repr(s))

# f = open("module.py")
# io = f.read(1024)
# print(io)
# f.close()
with open("module.py", "rb") as f:
    io = f.read(1024)
    print(io)
    io = f.read()
print(io)

with open("module_import.py", "rb") as f1:
    io_line = f1.readline()
    print(io_line)
    io_line = f1.readline()
    print(io_line)
    io_line = f1.readline()
    print(io_line)
    io_line = f1.readline()
    print(io_line)
    io_line = f1.readline()
    print(io_line)

with open("module_import.py", "rb") as f2:
    io_lines = f2.readlines()
    print(io_lines)
    print(list(f2))


file = open("module_import.py", "rb")
for line in list(file):
    print(line)
file.close()


with open("module_import.py", "w+") as f3:
    # f3.write("print('test_io_write')")
    f3.write(str(123456))


with open("module_import.py", "w") as f4:
    f4.writelines(["print(1234)\n", "print(5678)\n", "print(8975)"])