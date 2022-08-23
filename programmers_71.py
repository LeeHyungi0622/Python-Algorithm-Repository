# def solution(phone_book):

#     phone_book_dict = {len(p): [] for p in phone_book}

#     min_len = min(phone_book_dict, key=phone_book_dict.get)

#     for p in phone_book:
#         phone_book_dict[len(p)].append(p)

#     answer = True
#     for m in phone_book_dict[min_len]:
#         for n in list(set(phone_book) - set(phone_book_dict[min_len])):
#             if m == n[:min_len]:
#                 answer = False
#                 return answer

#     return answer


# phone_book = ["119", "97674223", "1195524421"]

# print(solution(phone_book))

import heapq


def solution(phone_book):

    heapq.heapify(phone_book)
    answer = True
    p_num = heapq.heappop(phone_book)
    while phone_book:
        i = len(p_num)
        if p_num == phone_book[0][:i]:
            return False
        p_num = heapq.heappop(phone_book)

    return answer


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     print(list(zip(phone_book, phoneBook[1:])))
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True


# phone_book_1 = ["97674223", "1195524421"]
# phone_book = ["119", "97674223", "1195524421"]

# print(solution(phone_book))

# for number, upper, lower in zip("12345", "ABCDE", "abcde"):
#     print(number, upper, lower)
