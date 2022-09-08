import numpy as np


def make_matrix(string, k, debug=False):
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


def start_decryption(input_text, width=5):
    input_text = input_text.replace("$", " ")
    input_text = input_text.replace("*", ".")
    matrix = make_matrix(input_text, width, False)
    matrix_np = np.array(matrix)
    transpose_matrix = matrix_np.transpose().tolist()
    encrypted_text = ""
    for words in transpose_matrix:
        encrypted_text += "".join(words)
    encrypted_text = encrypted_text.replace("@", " ")
    decrypted_text = encrypted_text.replace("#", " ")
    return decrypted_text


if __name__ == "__main__":
    input_text = "HSSIO,E@CNN2ABO@@0VEVSJ1EEEPA3NNRAN#@@EC@#HDDE1#AI@@4#"
    res = start_decryption("B,vou$entwreti$dela*rlb#f$a#lnn#yed#")
    print(res)
