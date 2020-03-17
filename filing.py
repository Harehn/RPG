from random import *
from pickle import *


def load_dict(file_name):
    in_file = open("Files/"+file_name, 'r+')
    lines = in_file.readlines()
    in_file.close()
    lines = lines[1:]
    dic = {}
    last_key = ""
    for line in lines:
        if line == "":
            pass
        elif line[0] == "#":
            last_key = line[1:].strip()
            dic[last_key] = []
        else:
            if dic[last_key] is None:
                dic[last_key] = [line.strip()]
            else:
                dic[last_key].append(line.strip())
    in_file.close()
    for k in dic.keys():
        dic[k] = restructure(dic[k])
    return dic


def restructure(ll):
    #a = " ".join(ll)
    #a = a.split("|")
    #return [i.split("-") for i in ("".join(ll)).split("|")]
    index = -1
    to_return = []
    for line in ll:
        if line[0] != "-":
            to_return.append([line])
            index += 1
        else:
            to_return[index].append(line[1:])
    return to_return


def save(file_name, dic):
    out_file = open("Files/"+file_name, 'w+')
    out_file.write("Refer to .... for formatting rules\n")
    for k, v in dic.items():
        out_file.write("#" + k + "\n")
        for l in v:
            out_file.write(l + "\n")
        out_file.write("\n")
    out_file.close()
    return True


def save_all(dics):
    for dic in dics:
        save('-'.join(dic.keys()), dic)


def save_to_file(s, file_name):
    out_file = open("Files/"+file_name, 'w+')
    out_file.write(s)
    out_file.close()

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        dump(obj, output, HIGHEST_PROTOCOL)


def load_object(filename):
    with open(filename, 'rb') as input_file:
        company1 = load(input_file)


def makeHtml(lists,  file_name):
    in_file = open("Files/"+"__boiler.txt", 'r+')
    lines = "\n".join(in_file.readlines())
    buttons = [makeTabButton(name) for name, content in lists]
    buttons[0] = makeTabButton((lists[0])[0], "id=\"defaultOpen\"")
    content = [makeTabContent(name, content) for name, content in lists]
    content[0] = makeTabContent((lists[0])[0], (lists[0])[1], " style=\"display: block;\"")
    lines = lines.replace("%t", "\n".join(buttons))
    lines = lines.replace("%l", "\n".join(content))
    save_to_file(lines, file_name)


def makeTabContent(name, content, ids=""):
    in_file = open("Files/"+"__tabContent.txt", 'r+')
    lines = "\n".join(in_file.readlines())
    lines = lines.replace("%n", name)
    lines = lines.replace("%c", content)
    lines = lines.replace("%i", ids)
    return lines


def makeTabButton(name, ids=""):
    in_file = open("Files/"+"__tabButton.txt", 'r+')
    lines = "\n".join(in_file.readlines())
    lines = lines.replace("%n", name)
    lines = lines.replace("%id", ids)
    return lines


#animals = load_dict("_animals2.txt")
#print(animals)
#print(restructure(animals["animals"]))
