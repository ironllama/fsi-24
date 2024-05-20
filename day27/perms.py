# def get_perms(curr_perms, pos, limit):
    # if pos < limit:
    #     if len(curr_perms) == pos:
    #         curr_perms.append(pos)
    #         print("CURR:", curr_perms)
    #     get_perms(curr_perms, pos + 1, limit)
    # else:

    #     curr_num = curr_perms[-1]
    #     if curr_num < limit:
    #         new_perms = curr_perms[:]
    #         new_num = curr_num + 1
    #         if str(new_num) not in "".join(curr_perms)
    #         new_perms[-1] = curr_num + 1
    #     # else loop:
    #         # if (digit < len(curr_perms) advance digit
    #     # recurse pos + 1
    # # write curr_perms as a valid combo
# get_perms([], 0, 3)

def generate(k, A):
    global perms
    if k == 1:
        perms.append(A[:])
    else:
        # Generate permutations with k-th unaltered
        # Initially k = length(A)
        generate(k - 1, A)

        # Generate permutations for k-th swapped with each k-1 initial
        for i in range(k-1):
            # Swap choice dependent on parity of k (even or odd)
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]

            generate(k - 1, A)

perms = []
initial = list(range(3))
generate(len(initial), initial)
print(perms)