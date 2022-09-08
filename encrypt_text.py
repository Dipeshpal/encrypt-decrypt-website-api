import numpy as np


def make_matrix(string, k=9, debug=False):
    matrix = []
    for i in range(len(string)):
        if i % k == 0:
            sub = string[i:i + k]
            lst = []
            for j in sub:
                lst.append(j)
            if len(lst) != k:
                current_len = len(lst)
                remaining_char = k - current_len
                for i in range(remaining_char):
                    lst.append("#")
            matrix.append(lst)
    if debug:
        for i in matrix:
            print(i)
    return matrix


def start_encryption(input_text="Hello\nHi"):
    input_text = input_text.replace(" ", "$")
    input_text = input_text.replace(".", "*")
    matrix = make_matrix(input_text, 9, False)
    matrix_np = np.array(matrix)
    transpose_matrix = matrix_np.transpose().tolist()
    encrypted_text = ""
    for words in transpose_matrix:
        encrypted_text += "".join(words)
    # print(input_text)
    # print(encrypted_text, "Width should be: ", matrix_np.shape[0])
    return encrypted_text, matrix_np.shape[0]


if __name__ == "__main__":
    input_text = """Butterfly, will never abandoned."""
    print(start_encryption(input_text))
