import os.path as op

FILE_BLACK_LIST = "black_list.txt"

def detect_fake(event_name):

    list_name = event_name.split()

    fileName = op.dirname(op.abspath(__file__)) + "\\" + FILE_BLACK_LIST
    fileList = [line.rstrip('\n') for line in open(fileName, 'r')]

    matching = [s for s in fileList if any(xs == s for xs in list_name)]
    
    if len(matching) > 0:
        print("Evento fake detectado! (Palavras: " + str(matching) + ')')
        return True
    else:
        print("Não detectado como fake...")
        return False


