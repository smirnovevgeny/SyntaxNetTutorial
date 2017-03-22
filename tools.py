import sys, os, codecs

def dynamicPrint(str):
    sys.stdout.write('\r{}'.format(str))
    sys.stdout.flush()


def checkDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def getListFromFile(path, encoding="utf-8"):
    with codecs.open(path, encoding=encoding) as input_file:
        return input_file.read().splitlines()

def getSetFromFile(path, encoding="utf-8"):
    return set(getListFromFile(path, encoding=encoding))


def WWconcantenateTrain(path_ww, path_train, path_output):

    with codecs.open(path_ww, encoding="utf-8") as wwFile:
        data_ww = wwFile.read()

    with codecs.open(path_train, encoding="utf-8") as trainFile:
        data_train = trainFile.read()

    with codecs.open(path_output, mode="w", encoding="utf-8") as output:
        print >> output, data_ww + data_train[:-1]