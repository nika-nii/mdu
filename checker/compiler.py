import subprocess
def compiler(code):

    handle = open(code['file'])
    data = handle.read()
    handle.close()

    # python language
    if code['language'] == 'python':
        p = subprocess.run(["python", "-m", "py_compile", code['file']], 
                            stderr = subprocess.PIPE)
        data = code['file'][:-2] + 'pyc'

    # c language
    if code['language'] == 'c':
        p = subprocess.run(["gcc", code['file']], stderr = subprocess.PIPE)
        data = 'a.out'

    # c++ language
    if code['language'] == 'c++':
        p = subprocess.run(["g++", code['file']], stderr = subprocess.PIPE)
        data = 'a.out'

    # java language
    if code['language'] == 'java':
        p = subprocess.run(["javac", code['file']], stderr = subprocess.PIPE)
        data = code['file'][:-4] + 'class'
    
    # pascal language
    if code['language'] == 'pascal':
        p = subprocess.run(["fpc", code['file']], stderr = subprocess.PIPE)
        data = code['file'][:-4]
        
    # return dictionary
    if p.returncode == 0:
        dictionary ={"errors": False,
                     "error-message": "",
                     "output_file": data,
                     "language": code['language'] } 
    else:
        dictionary ={"errors": True,
                     "error-message": p.stderr,
                     "output_file": "",
                     "language": code['language'] }
    return dictionary
