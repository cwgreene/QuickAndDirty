import sys

word_dict= {}

def read_files():
    for filename in sys.argv[1:]:
        for line in open(filename):
            for word in line.strip().split(" "):
                if word == '':
                    continue
                if word not in word_dict:
                    word_dict[word] = 0
                word_dict[word] +=1
def read_stdin():
    while True:
        line = raw_input()
        for word in line.strip().split(" "):
            if word == '':
                continue
            if word not in word_dict:
                word_dict[word] = 0
            word_dict[word] +=1
if len(sys.argv )==1:
    try:
        read_stdin()
    except Exception:
        pass
else:
    read_files()

for line in sorted([(word_dict[k],k) for k in word_dict]):
    print line
