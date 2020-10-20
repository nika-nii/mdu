from jsonify import jsonify
from compiler import compiler
def checkSystem(code, file_in):
    dictionary = compiler(code)
    return jsonify(file_in, dictionary)


if __name__ == "__main__":
    data = input()
    language = input()
    file_in = input()
    code = {'file': data,
            'language': language}

    print(checkSystem(code, file_in))

