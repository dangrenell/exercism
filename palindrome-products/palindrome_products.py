# def smallest(max_factor, min_factor):
#     return palindrome(min_factor, max_factor)


def largest(max_factor, min_factor):
    return palindrome(min_factor, max_factor, smallest=False)


def palindrome(mn, mx, smallest=True):
    if mn > mx:
        raise ValueError("No can do")
    else:
        args = (mn**2, mx**2+1) if smallest else (mx**2, mn**2-1, -1)

        for r in range(*args):
            s = str(r)
            if s == s[::-1] and any(mn <= r//j <= mx
                                    for j in range(mn, mx+1) if r % j == 0):
                return r, ((i, r//i) for i in range(mn, mx + 1)
                           if r % i == 0 and mn <= i <= r//i <= mx)


def smallest(max_factor, min_factor):
    result = None
    factors = []

    if min_factor <= max_factor:
        raise ValueError("No go, bro.")
    else:
        for i in range(min_factor**2, max_factor**2+1):
            if str(i) == str(i)[::-1]:
                if


# def largest(min_factor, max_factor):
#     if max_factor < min_factor:
#         raise ValueError("Max cannot be less than Min")
#     else:
#         products = product_helper(min_factor, max_factor)
#         try:
#             max_palin = max(products.values())
#             results = {k: v for k, v in products.items() if v == max_palin}
#             return max_palin, [list(a) for a in results.keys()]
#         except:
#             return None, []


# def smallest(min_factor, max_factor):
#     if max_factor < min_factor:
#         raise ValueError("Max cannot be less than Min")
#     else:
#         products = product_helper(min_factor, max_factor)
#         try:
#             min_palin = min(products.values())
#             results = {k: v for k, v in products.items() if v == min_palin}
#             return min_palin, [list(a) for a in results.keys()]
#         except:
#             return None, []


# def product_helper(min_factor, max_factor):
#     products = {}
#     for a in range(min_factor, max_factor+1):
#         for b in range(a, max_factor+1):
#             prod = a*b
#             if str(prod) == str(prod)[::-1]:
#                 products[(a, b)] = prod
#     return products


# # def palindrome_helper(min_factor, max_factor):
# #     '''
# #     Test returning only minimax palindromes
# #     '''
# #     palindromes = []

# #     flag = True
# #     if flag:
# #         for i in range(min_factor, max_factor+1):
# #             if flag:
# #                 for j in range(i, max_factor+1):
# #                     prod = i*j
# #                     if str(prod) == str(prod)[::-1]:
# #                         palindromes.append(prod)
# #                         flag = False
# #                         break

# #     flag = True
# #     if flag:
# #         for i in range(max_factor, min_factor-1, -1):
# #             if flag:
# #                 for j in range(i, min_factor-1, -1):
# #                     prod = i*j
# #                     if str(prod) == str(prod)[::-1]:
# #                         palindromes.append(prod)
# #                         flag = False
# #                         break

# #     return palindromes


# # def largest(min_factor, max_factor):
# #     if max_factor < min_factor:
# #         raise ValueError("Max cannot be less than Min")
# #     else:
# #         palindrome = None

# #         flag = True
# #         if flag:
# #             for i in range(max_factor, min_factor-1, -1):
# #                 if flag:
# #                     for j in range(i, min_factor-1, -1):
# #                         prod = i*j
# #                         if str(prod) == str(prod)[::-1]:
# #                             palindrome = prod
# #                             flag = False
# #                             break

# #         factors = find_factors(palindrome, min_factor, max_factor)

# #         return palindrome, factors


# # def find_factors(num, min_factor, max_factor):
# #     factors = []
# #     if num:
# #         for i in range(min_factor, 1 + max_factor):
# #             if num % i == 0:
# #                 if num/i <= max_factor and [int(num/i), i] not in factors:
# #                     factors.append([i, int(num/i)])
# #     return factors


# # I think I can do better. Instead of generating all products and filtering, look at all vals between squares and select.
# # print(palindrome_helper(5, 11))
# # print(product_helper(5, 11))

# # print(find_factors(100, 5, 11))

# print(largest(min_factor=100, max_factor=999))
