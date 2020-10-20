import json
from checking_tests import checker

def jsonify(file_in, compiler):

    handle = open(file_in)
    d_in = json.load(handle)
    handle.close()
    d_out = checker(compiler, d_in)
    file_out = json.dumps(d_out)
    return file_out


