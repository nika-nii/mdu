import multiprocessing
import resource
import json
import subprocess
from subprocess import Popen, PIPE, STDOUT
from threading import Timer
import time

def limit_virtual_memory(memory):
    resource.setrlimit(resource.RLIMIT_AS, 
                      (memory, resource.RLIM_INFINITY))

def checker(code):

    a = []
    handle = open(code['json'])
    data = json.load(handle)
    handle.close()

    # tests
    for i in range(len(data["tests"])):

        # python language
        if code['compiler']['language'] == 'python':
            p = subprocess.Popen(["python", code['compiler']['output_file']], 
                stdout = PIPE, stdin = PIPE, stderr = PIPE, 
                shell = False)

        # java language
        if code['compiler']['language'] == 'java':
            p = subprocess.Popen(["java", code['compiler']['output_file']],
                stdout = PIPE, stdin = PIPE, stderr = PIPE, shell = False)

        # c language
        if code['compiler']['language'] == 'c':
            p = subprocess.Popen(["./" + code['compiler']['output_file']],
                stdout = PIPE, stdin = PIPE, stderr = PIPE, shell = False)

        # c++ language
        if code['compiler']['language'] == 'c++':
            p = subprocess.Popen(["./" + code['compiler']['output_file']],
                stdout = PIPE, stdin = PIPE, stderr = PIPE, shell = False)

        # pascal language
        if code['compiler']['language'] == 'pascal':
            p = subprocess.Popen(["./" + code['compiler']['output_file']],
                stdout = PIPE, stdin = PIPE, stderr = PIPE, shell = False)

        # timer
        timer = Timer(data["time"], p.kill)
        timer.start()
        sTime = time.time()
        out, stderr = p.communicate(input = data["tests"][i][0].encode())
        eTime = time.time()
        timer.cancel()
        print(eTime - sTime)

        # decode
        out = out.decode("utf-8")
        out = out.replace("\n", "")
        
        # check out
        if out == data["tests"][i][1]:
            a.append(True)
        else:
            a.append(False)
            error = p.stderr

            if out == '':
                error = "time limit"
        
            return {"errors": True,
                    "errors_type": error,
                    "test": a, }

    return {"errors": False,
            "errors_type": '',
            "test": a }


if __name__ == '__main__':

    compiler = {"output_file": "test_code/Main.pyc",
                "language": "python" }

    code = { "json": "test1.json",
             "compiler": compiler}

    print(checker(code))

    


