import subprocess
def compile(code):

    handle = open(code['file'])
    data = handle.read()
    handle.close()

    # python language
    if code['language'] == 'python':
        p = subprocess.run(["python3", code['file']], stderr=subprocess.PIPE)
    
    # c language
    if code['language'] == 'c':
        if subprocess.run(["gcc", code['file']], stderr=subprocess.PIPE) == 0:
            p1 = subprocess.run(["gcc", code['file']], stderr=subprocess.PIPE)
            p = subprocess.run(["./a.out"], stderr=subprocess.PIPE)
        else:
            p = subprocess.run(["gcc", code['file']], stderr=subprocess.PIPE)

    # c++ language
    if code['language'] == 'c++':
        if subprocess.run(["g++", code['file']], stderr=subprocess.PIPE) == 0:
            p1 = subprocess.run(["g++", code['file']], stderr=subprocess.PIPE)
            p = subprocess.run(["./a.out"], stderr=subprocess.PIPE)
        else:
            p = subprocess.run(["g++", code['file']], stderr=subprocess.PIPE)

    # java language
    if code['language'] == 'java':
        if subprocess.run(["javac", code['file']], stderr=subprocess.PIPE) == 0:
            p1 = subprocess.run(["javac", code['file']], stderr=subprocess.PIPE)
            p = subprocess.run(["java", p1], stderr=subprocess.PIPE)
        else:
            p = subprocess.run(["javac", code['file']], stderr=subprocess.PIPE)

    # pascal language
    if code['language'] == 'pascal':
        if subprocess.run(["fpc", code['file']], stderr=subprocess.PIPE) == 0:
            p1 = subprocess.run(["fpc", code['file']], stderr=subprocess.PIPE)
            p = subprocess.run(["./Main"], stderr=subprocess.PIPE)
        else:
            p = subprocess.run(["fpc", code['file']], stderr=subprocess.PIPE)

    # return dictionary
    if p.returncode == 0:
        dictionary ={"errors": True,
                     "error-message": ''}
    else:
        dictionary ={"errors": False,
                     "error-message": p.stderr}
    return dictionary

code = {'file': 'Main.pas',
        'language': 'pascal'}
dictionary = compile(code)
print(dictionary)
