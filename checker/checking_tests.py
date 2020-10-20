import subprocess
from subprocess import PIPE
from threading import Timer
import time

def checker(compiler, data):

    a = []
    # test
    for i in range(len(data["tests"])):
        
        # python language
        if compiler['language'] == 'python':
            p = subprocess.Popen(["python", compiler['output_file']],
                stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=False)

        # java language
        if compiler['language'] == 'java':
            p = subprocess.Popen(["java", compiler['output_file']],
                stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=False)

        # c language
        if compiler['language'] == 'c':
            p = subprocess.Popen(["./" + compiler['output_file']],
                stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=False)

        # c++ language
        if compiler['language'] == 'c++':
            p = subprocess.Popen(["./" + compiler['output_file']],
                stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=False)

        # pascal language
        if compiler['language'] == 'pascal':
            p = subprocess.Popen(["./" + compiler['output_file']],
                stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=False)

        b = {"passed": 0,
             "time": 0,
             "mem": 0}

        # timer
        timer = Timer(data["time"], p.kill)
        timer.start()
        sTime = time.time()

        out, stderr = p.communicate(input=data["tests"][i][0].encode())

        eTime = time.time()
        timer.cancel()

        b['time'] = round(eTime - sTime, 2)

        # decode
        out = out.decode("utf-8")
        out = out.replace("\n", "")
        
        # check out
        if out == data["tests"][i][1]:
            b['passed'] = True
            a.append(b)
        else:
            b['passed'] = False
            a.append(b)
            error = p.stderr

            if out == '':
                error = "time limit"
        
            return {"errors": True,
                    "errors_type": error,
                    "test": a}

    return {"errors": False,
            "errors_type": '',
            "test": a}
    


