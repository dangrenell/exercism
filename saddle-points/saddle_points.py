def saddle_points(matrix):
    answers = []
    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError("Invalid matrix")
    else:
        for r_index, row in enumerate(matrix):
            row_max = max(row)
            for c_index, element in enumerate(row):
                col_min = min([row[c_index] for row in matrix])
                if element == row_max and element == col_min:
                    answer = {"row": r_index+1, "column": c_index+1}
                    answers.append(answer)
        return answers
