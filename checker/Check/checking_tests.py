import multiprocessing
import json
import subprocess
from subprocess import Popen, PIPE, STDOUT
from threading import Timer
def checker(code):

    a = []
    handle = open(code['json'])
    data = json.load(handle)
    handle.close()

    # tests
    for i in range(len(data["tests"])):
        
        # in test
        p = subprocess.Popen(["python", code['compiler']], 
            stdout = PIPE, stdin = PIPE, stderr = PIPE, shell = False)

        timer = Timer(1, p.kill)
        timer.start()
        out, stderr = p.communicate(input = data["tests"][i][0].encode())
        timer.cancel()

        # decode
        out = out.decode("utf-8")
        out = out.replace("\n", "")
        
        # check test
        if out == data["tests"][i][1]:
            a.append(True)
        else:
            a.append(False)
            return {"errors": True,
                    "errors_type": p.stderr,
                    "test": a }

    return {"errors": False,
            "errors_type": '',
            "test": a }


if __name__ == '__main__':

    code = { "json": "test1.json",
             "compiler": "test_code/Main.pyc"}
    print(checker(code))

    


