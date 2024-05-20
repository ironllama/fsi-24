def scoreOfStudents(s: str, answers: list[int]) -> int:
    scores = []

    # To generate right answers.
    new_s = [char if char in "*+" else int(char) for char in s]

    while "*" in new_s:
        pos_of_star = new_s.index("*")
        new_num = new_s[pos_of_star - 1] * new_s[pos_of_star + 1]
        new_s = [*new_s[:pos_of_star - 1], new_num, *new_s[pos_of_star + 2:]]
    
    new_s = filter(lambda p: p != "+", new_s)  # Get rid of '+' to use sum

    right_answer = sum(new_s)
    print("RIGHT ANSWER:", right_answer)


    # Change back for to generate wrong answers.
    new_s = [char if char in "*+" else int(char) for char in s]

    # Just going from left to right, no priority
    # wrong_answer = 0
    # curr_op = "+"
    # for x in s:
    #     if x in "*+":
    #         curr_op = x
    #     else:
    #         if curr_op == "+":
    #             wrong_answer += int(x)
    #         else:
    #             wrong_answer *= int(x)

    # Generate all permutations of priority and use that to get
    # all possible final values.
    # Adapted from: https://en.wikipedia.org/wiki/Heap's_algorithm
    all_wrongs = set()
    all_perms = []
    def generate_perms(k, A):  # Initially k = length(A)
        nonlocal all_perms
        if k == 1:
            all_perms.append(A[:])
        else:
            # Generate permutations with k-th unaltered
            generate_perms(k - 1, A)

            # Generate permutations for k-th swapped with each k-1 initial
            for i in range(k-1):
                # Swap choice dependent on parity of k (even or odd)
                if k % 2 == 0:
                    A[i], A[k-1] = A[k-1], A[i]
                else:
                    A[0], A[k-1] = A[k-1], A[0]

                generate_perms(k - 1, A)

    num_of_opers = len(s) // 2
    initial = list(range(num_of_opers))  # Initial list to generate perms
    generate_perms(len(initial), initial)
    print("PERMS:", all_perms)

    for perm in all_perms:  # Get one permutation of order of operations
        copy_s = new_s[:]  # Act on a copy of the original string
        print(">>>:", copy_s, perm)

        # Attach a priority number in front of each operation
        pos_perm = 0
        for i, c in enumerate(new_s):
            if isinstance(c, str) and c in "*+":
                copy_s[i] = str(perm[pos_perm]) + c
                pos_perm += 1
        print("\tOPER PRIORITIES:", copy_s)

        # Use the priority numbers to do operations 
        pos_oper = 0
        while pos_oper < num_of_opers:
            # Get add or mutliply -- gotta be one of the two.
            # try:
            #     pos_oper_combo = copy_s.index(str(pos_oper) + "+")
            #     new_num = copy_s[pos_oper_combo - 1] + copy_s[pos_oper_combo + 1]
            # except ValueError:
            #     pos_oper_combo = copy_s.index(str(pos_oper) + "*")
            #     new_num = copy_s[pos_oper_combo - 1] * copy_s[pos_oper_combo + 1]

            for i, word in enumerate(copy_s):
                if isinstance(word, str):
                    if word == str(pos_oper) + "+":
                        pos_oper_combo = i
                        new_num = copy_s[i - 1] + copy_s[i + 1]
                        break
                    elif word == str(pos_oper) + "*":
                        pos_oper_combo = i
                        new_num = copy_s[i - 1] * copy_s[i + 1]
                        break

            copy_s = [*copy_s[:pos_oper_combo - 1], new_num, *copy_s[pos_oper_combo + 2:]]
            print("\t\tSOFAR:", pos_oper, copy_s)

            pos_oper += 1

        all_wrongs.add(copy_s[0])  # Add final answer to all possible wrongs
    print("ALL WRONGS:", all_wrongs)

    for a in answers:
        if a == right_answer:
            scores.append(5)
        elif a in all_wrongs:
            scores.append(2)
        else:
            scores.append(0)

    # print("ALL SCORES:", scores)
    return sum(scores)

# print(scoreOfStudents("7+3*1*2", [20,13,42]))
# print(scoreOfStudents("1+2*3+4", [13,21,11,15]))
print(scoreOfStudents("6+3*6+2*9+9*4+9*9+5*9+6", [512,210,210,594,210,875,762,210,210,270,342,330,210,168,767,22,462,634,194,210,552,210,210,384,210,348,210,267,553,139,210,389,614,210,825,234,900,435,210,699,454,504,300,210,210,210,215,984,210,522,943,654,793,714,870,693,210,686,210,720,153,210,957,510,210,810,210,846,714,528,942,210,342,974,210,71,906,402,726,924,388,696,210,366,210,888,825,210,210,210,654,996,846,559,210,492,210,698,210,856,576,324,822,894,666,210,935,210,840,45,641,210,210,588,708,966,462,300,210,759,480,210]))
