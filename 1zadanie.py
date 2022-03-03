myfile = open(file="logs.txt", mode='r', encoding="utf-8")

for line in myfile:
                remote_addr = line.split(" - - ")[0]
                type_and_resource = line.split('"')[1]
                request_type = type_and_resource.split()[0]
                requested_resource = type_and_resource.split()[1]
                print(f"'{remote_addr}', '{request_type}', '{requested_resource}'")












myfile.close()
