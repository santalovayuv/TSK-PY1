import json

INPUT_FILE = "input.csv"
def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as f:
        head_ = f.readline()
        head_ = head_.split(",")
        head = [elem.rstrip() for elem in head_]
        list_dict = []
        for line in f:
            line = line.split(',')
            line = [x.rstrip() for x in line]
            line = dict(zip(head, line))
            list_dict.append(line)
        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


