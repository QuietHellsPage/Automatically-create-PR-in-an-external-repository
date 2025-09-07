#
#
# def large(nums):
#     def compare(a, b):
#         return -1 if a + b > b + a else 1  # Сортировка в "обратном" порядке
#
#     sorted_strs = sorted(map(str, nums), key=cmp_to_key(compare))
#     return "".join(sorted_strs).lstrip("0") or "0"
#
#
# print(large([3, 30, 34, 5, 9]))
# from  collections import defaultdict
#
# def dubs(nums, k):
#     ds = defaultdict(list)
#     for ind, val in enumerate(nums):
#         ds[val].append(ind)
#     for num, ind in ds.items():
#         if len(ind) >= 2:
#             for i in range(len(ind) - 1):
#                 if ind[i + 1] - ind[i] <= k:
#                     return True
#     return False
#
# print(dubs([3, 30, 34, 5, 9, 3], 3))
from idlelib.tree import TreeItem
from random import shuffle

# def mx(nums):
#     return list(sorted(set(nums), reverse=True))[2] if len(set(sorted(nums))) > 2 else max(nums)
# print(mx([3]))

# a = [3, 30, 34, 5, 9, 3]

# print(list(set(sorted(a, reverse=True)))[2])

# print(list(sorted(set(a), reverse=True))[2])

# def sen(sentence):
#     d = {
#         "a": 0,
#         "e": 0,
#         "i": 0,
#         "o": 0,
#         "u": 0
#     }
#     for i in sentence.lower():
#         if i in d.keys():
#             d[i] += 1
#     return sum(d.values())
#
# print(sen("Hello"))

# a = input()
# spisok = a.split(", ")
# r = []
# s = {}
# for p in spisok:
#     el, c = p.split(": ")
#     s[el] = c
# for elem in spisok:
#     mon = 500
#     count = 0
#     name, price = elem.split(": ")
#     while mon > int(price):
#         count += 1
#         mon -= int(price)
#     r.append(count)
# a = ", ".join([str(i) for i in r])
# print(a)
# print(f"{min(s, key=s.get)}: {min(s.values())}")

# a = input()
# b = input()
# c = input()
#
# tenty = c.split()
# cof = a.split()
# tea = b.split()
# res = []
# for name in cof:
#     if name not in tea and name not in tenty:
#         res.append(name)
# for name in tea:
#     if name not in cof and name not in tenty:
#         res.append(name)
# print(" ".join([i for i in sorted(res)]))

# fav_desserts = {
#     'Ира' : ['Тирамису', 'Марципан', 'Яблочный пирог'],
#     'Марина' : ['Яблочный пирог', 'Мороженое'],
#     'Максим' : ['Марципан', 'Брауни', 'Мидальный торт'],
#     'Карина' : ['Пишмание', 'Брауни', 'Тирамису', 'Марципан'],
#     'Настя' : ['Лимбургский пирог', 'Тирамису', 'Брауни']
# }
# a = input()
# res = []
# for name, val in fav_desserts.items():
#     if a in val:
#         res.append(name)
# print(" ".join(i for i in res))
# a = input()
# b = input()
# ots = b.split()
# namse = a.split(", ")
# slov = {}
# for i, z in zip(namse, ots):
#     ints = list(map(int, z.split("-")))
#     avg = sum(ints) / len(ints)
#     slov[i] = avg
# print(min(slov, key=slov.get))

# with open("data.csv", "r", encoding='utf-8') as f:
#     lin

# ok = 'Подходит'
# not_ok = 'Что-то не так'
#
# # ваш код ниже
# a = input()
# if a.isalnum() or len(a) <= 5:
#     print(not_ok)
# else:
#     print(ok)

# a = input()
# b = input()
#
# words = a.split()
# nums = b.split()
#
# errors = []
# for word, num in zip(words, nums):
#     if any([i.islower() for i in word]) and num == "0":
#         errors.append(word)
#     elif all([o.isupper() for o in word]) and num == "1":
#         errors.append(word)
# print(errors)

# data = {
#     'ВШЭ': {'социология': ['Оля', 'Валя', 'Ира'], 'политология': ['Рима', 'Карина', 'Ира']},
#     'МГУ': {'история': ['Варя', 'Оля', 'Марина'], 'социология': ['Максим', 'Ира']},
#     'МГИМО': {'востоковедение': ['Милана', 'Оля', 'Ира'], 'политология': ['Таня', 'Паша']},
#     'РАНХиГС': {'история': ['Милана']}
# }
#
# # ваш код ниже
# a = input()
# res = []
# for i in data.values():
#     for prog, name in i.items():
#         if a in name:
#             res.append(prog)
# print(", ".join([f for f in sorted(set(res))]))


months = [
    'январь', 'февраль', 'март', 'апрель', 'май',
    'июнь', 'июль', 'август', 'сентябрь',
    'октябрь', 'ноябрь', 'декабрь'
]

# ваш код ниже
# a = input()
# traty = a.split(", ")
# res = {}
# for trata in traty:
#     date, summa = trata.split(" - ")
#     day, month = date.split(".")
#     if month not in res.keys():
#         res[month] = int(summa)
#     else:
#         res[month] += int(summa)
# sorted_months = sorted(res.items(), key=lambda x: x[1], reverse=True)
#
# for m, z in zip(months, sorted_months):
#     print(m)

# a = input()
# traty = a.split(", ")
# res = {}
#
# for trata in traty:
#     date, summa = trata.split(" - ")
#     day, month_num = date.split(".")
#     month_index = int(month_num) - 1
#     month_name = months[month_index]
#
#     if month_name not in res:
#         res[month_name] = int(summa)
#     else:
#         res[month_name] += int(summa)
#
# # Сортируем по убыванию суммы и выводим только названия месяцев
# sorted_months = sorted(res.items(), key=lambda x: x[1], reverse=True)
#
# for month_name, amount in sorted_months:
#     print(month_name)

# letters = 'abcdefghijklmnopqrstuvwxyz'
#
#
# # ваш код ниже
# def true_code(lst):
#     res = []
#     rev = letters[::-1]
#     for element in lst:
#         dec_word = ""
#         for char in element.lower():
#             ind = letters.find(char)
#             mew = rev[ind]
#             dec_word += mew
#         res.append(dec_word)
#     return " ".join([i for i in res])
#
#
# print(true_code(['R', 'olEv', 'zORxv']))
# punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# a = open("invitations.txt", "r")
# na = []
# for line in a:
#     words = line.split()
#     for w in words:
#         if w[0].isupper():
#             na.append(w)
# res = []
# for elem in na:
#     cl = elem
#     for p in punctuation:
#         if p in elem:
#             cl = elem.replace(p, "")
#             res.append(cl)
# print(res)

# a = input().split("; ")
# proh = float(input())
# res = []
# for both in a:
#     name, marks = both.split(": ")
#     each_mark = marks.split("-")
#     avg = sum(map(int, each_mark)) / len(each_mark)
#     if avg > proh:
#         res.append(name)
# print(", ".join([i for i in sorted(res)]))

# names = input().split()
# days = input().split()
# m = input()
# res = []
#
# for n, d in zip(names, days):
#     if int(d) <= int(m):
#         res.append(n)
# # print("\n".join([i for i in res]))
#
# shops = {'Монеточка': [6000, 4000, 2300],
#          'Дорожный': [6700, 4000, 2100],
#          'Букварь вкусов' : [10000, 8000, 6000],
#          'СладкоВилл' : [5000, 9000, 4000]}

# ваш код ниже
# res = []
# a = int(input())
# for name, vals in shops.items():
#     for val in vals:
#         if val < a:
#             res.append(name)
# print("\n".join([i for i in res]))


cities = {'Австрия' : ['Вена', 'Гранц', 'Линц'],
          'Испания' : ['Барселона'],
          'Норвегия' : ['Осло', 'Хамар', 'Алта'],
          'Мексика' : ['Мехико', 'Леон']}

# ваш код ниже
# a = input()
# res = []
# for cointry, city in cities.items():
#     if a == cointry:
#         res.append(sorted(city)[0])
# print("".join(res) if res else "Такой страны нет")


internet = {'Мостелеком': [1, 2, 1, 1, 1, 2, 1],
            'Соединение2023': [1, 1, 0, 1, 1, 1, 0],
            'МТТС': [1, 1, 1, 1, 2, 1, 1],
            'Трилайн': [2, 2, 1, 1, 1, 2, 2]}

# ваш код ниже
# a = int(input())
# res = []
# for comp, days in internet.items():
#     if 0 not in days and days.count(2) >= a:
#         res.append(comp)
# print("\n".join([i for i in res]))

# schools = {'ЯзыкДляВсех': [45, 67, 30, 24, 82, 12, 91],
#            'Питонисты2023': [32, 14, 29, 100, 21, 70, 25],
#            'EngStart': [105, 48, 22, 74, 53, 90, 12],
#            'NewLang': [83, 200, 0, 44, 12, 54, 19]}
#
# # ваш код ниже
# a = int(input())
# res = []
# for name, z in schools.items():
#     if sum(z) >= len(z):
#         res.append(name)
# print("\n".join([i for i in res]))

# books = input().split(", ")
# res = {}
# for elem in books:
#     name, kolvo = elem.split("-")
#     if int(kolvo) < 200:
#         res[name] = kolvo
# k = sorted(res.items(), key=lambda x: x[1], reverse=True)
# for i in k:
#     print(i[0])

# prods = input().split()
# kals = input().split()
#
# res = {}
#
# for prod, kal in zip(prods, kals):
#     bel, zhir, ugl = kal.split("-")
#     tsen = 0.4 * int(bel) + 0.3 * int(zhir) + 0.3 * int(ugl)
#     res[prod] = tsen
# k = sorted(res.items(), key= lambda x: x[1])
# r = []
# for i in k:
#     for n in i:
#         r.append(n)
#
# print(r[0])


# tovars = input().split("; ")
# res = {}
# for tovar in tovars:
#     name, price = tovar.split(":")
#     frs, sec, thr = price.split(",")
#     avg = (int(frs) + int(sec) + int(thr)) / 3
#     res[name] = avg
# k = sorted(res.items(), key=lambda x: (x[1], x[0]))
# for item in k:
#     print(item[0])

# names = input().split()
# marks = input().split()
#
# res = {}
#
# for name, mark in zip(names, marks):
#     premarks = mark.split("-")
#     mrks = map(int, premarks)
#     sm = sum(mrks)
#     res[name] = sm
# k = sorted(res.items(), key=lambda x: x[1], reverse=True)
#
# r = k[0]
#
# print(r[0])

# a = [
#     (1382, 'победа'),
#     (1390, 'победа'),
#     (1391, 'поражение')
# ]
# res = set()
# for elem in a:
#     res.add(elem[1])
#
# if len(res) > 1:
#     print(False)
# else:
#     print(True)

# def get_contact(sps, inp):
#     c = 0
#
#     for _, names in sps.items():
#         if inp in names:
#             c += 1
#     return c
#
# print(get_contact({
# 'UK': ['Alice', 'Alex', 'Rita'],
# }, 'Alex'))

# f = open("0.txt", "r", encoding="utf-8")
# res = {}
# for i in f:
#     words = i.split()
#     for word in words:
#         if word[0].isupper():
#             if not word in res.keys():
#                 res[word] = 1
#             else:
#                 res[word] += 1
# g = sorted(res.items(), key=lambda x: x[1], reverse=True)
# print(g[0][0])

# f = open("notes.txt", "r", encoding="utf-8")
#
# res = {}
#
# for i in f:
#     words = i.split()
#     for word in words:
#         if word.endswith("*") and (len(word) - 1) >= 7:
#                 proc = word.replace("*", "")
#                 if proc not in res:
#                     res[proc] = 1
#                 else:
#                     res[proc] += 1
#
# print(res)
# print(sorted(res.keys())[0])


# f = open("data.csv", "r", encoding="utf-8")
# res = {}
# prices = {}
#
# for line in f:
#     client, name, price = line.split(";")
#     if name not in res:
#         res[name] = int(price)
#         prices[name] = 1
#     else:
#         res[name] += int(price)
#         prices[name] += 1
#
# fin = {}
#
# for summa, cnt in zip(res.items(), prices.items()):
#     avg = summa[1] / cnt[1]
#     fin[summa[0]] = avg
#
# l = sorted(fin.items(), key=lambda x: x[1], reverse=True)
# print(l[0][0])


# f = open("cakes.csv", "r")
#
# prices = {}
# counts = {}
#
# for line in f:
#     name, price, cof, glut = line.split(";")
#     if name not in prices:
#         prices[name] = int(price)
#         counts[name] = 1
#     else:
#         prices[name] += int(price)
#         counts[name] += 1
#
# fin = {}
#
# for p, c in zip(prices.items(), counts.items()):
#     avg = p[1] / c[1]
#     fin[p[0]] = avg
# k = sorted(fin.items(), key=lambda x: x[1], reverse=True)
# print(k[0][0])

# a = input()
# fem = []
# male = []
# while a != "СТОП":
#     name, age, sex = a.split(", ")
#     if int(age) > 20:
#         if sex == "женский":
#             fem.append(name)
#         elif sex == "мужской":
#             male.append(name)
#
# print(fem)
# print(male)

# word = "word"
# for char in word:
#     if char.isupper()
# print(word.islower())


# words = input().split()
# inxs = input().split()
# res = []
# for word, ind in zip(words, inxs):
#     if any([i.islower() for i in word]) and int(ind) == 0:
#         res.append(word)
#     elif word.isupper() and int(ind) == 1:
#         res.append(word)
# print(res)

# data = {
#     'ВШЭ': {'социология': ['Оля', 'Валя', 'Ира'], 'политология': ['Рима', 'Карина', 'Ира']},
#     'МГУ': {'история': ['Варя', 'Оля', 'Марина'], 'социология': ['Максим', 'Ира']},
#     'МГИМО': {'востоковедение': ['Милана', 'Оля', 'Ира'], 'политология': ['Таня', 'Паша']},
#     'РАНХиГС': {'история': ['Милана']}
# }

# a = input()
#
# res = []
#
# for unik, val in data.items():
#     for napr, names in val.items():
#         if a in names:
#             res.append(napr)
#
# s = set(res)
# print(", ".join(sorted(s)))

# letters = 'abcdefghijklmnopqrstuvwxyz'
#
# def true_code(sps):
#     reversed = letters[::-1]
#     res = []
#     for elem in sps:
#         proc_word = []
#         for char in elem.lower():
#             ind = letters.find(char)
#             proc_ind = reversed[ind]
#             proc_word.append(proc_ind)
#         r = "".join(proc_word)
#         res.append(r)
#     return " ".join(res)
# print(true_code(['R', 'olEv', 'zORxv']))

# with open("invitations.txt", "r", encoding="utf-8") as file:
#     res = []
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word[0].isupper():
#                 clean = word
#                 for char in punctuation:
#                     clean = clean.replace(char, "")
#                 res.append(clean)
#     r = {}
#     for item in res:
#         if item not in r.keys():
#             r[item] = 1
#         elif item in r.keys():
#             r[item] += 1
#     freq = sorted(r.items(), key=lambda x: x[1], reverse=True)
#     print(", ".join(sorted(set(res))))
#     print(f"Чаще всего упоминается {freq[0][0]}")





# ms = [
#     'январь', 'февраль', 'март', 'апрель', 'май',
#     'июнь', 'июль', 'август', 'сентябрь',
#     'октябрь', 'ноябрь', 'декабрь'
# ]
# notes = input().split(", ")
# r = {}
# for elem in notes:
#     d, s = elem.split(" - ")
#     day, mon = d.split(".")
#     if mon not in r.keys():
#         r[mon] = int(s)
#     elif mon in r.keys():
#         r[mon] += int(s)
# k = sorted(r.items(), key=lambda x: x[1], reverse=True)
# re = []
# for f in k:
#     re.append(f[0])
#
# mmms = []
# for v in re:
#     n = ms[int(v) - 1]
#     mmms.append(n)
# print("\n".join(mmms))


# with open("0.txt", "r", encoding="utf-8") as file:
#     res = {}
#     for elem in file:
#         words = elem.split()
#         for word in words:
#             if word[0].isupper():
#                 if word not in res.keys():
#                     res[word] = 1
#                 elif word in res.keys():
#                     res[word] += 1
#
# k = dict(sorted(res.items(), key=lambda x: x[0]))
#
# with open("final.txt", "w", encoding="utf-8") as f:
#     for city, colvo in k.items():
#         f.write(f"Название: {city}, посещений: {colvo}")
#         f.write("


lst = ["aaa, 86", "R, 52", "A, 86", "T, -11", "AaA, 46", "tres, 20", "Y, -11"]
#
# a = sorted(lst, key=lambda x: x.split(", ")[0])
#
# k = sorted(a, key=lambda x: int(x.split(", ")[1]))
#
# print(k)


# d = {
#     "a": 124,
#     "b": 52,
#     "c": 4654,
#     "d": 5
# }
#
# def max_two(item):
#     res = []
#     l = sorted(item.items(), key=lambda x: x[1], reverse=True)
#     for elem in l:
#         res.append(elem[0])
#     return res[:2]
#
# print(max_two(d))
#

# def limiter(limit):
#     def outer(func):
#         last_call = 0
#         def inner(*args, **kwargs):
#             nonlocal last_call
#             current_time = time.time()
#             left = current_time - last_call
#             if left < limit:
#                 waiting_time = limit - left
#                 print(F"Подождите {round(waiting_time)} секунд")
#                 return ""
#             last_call = current_time
#             return func(*args, **kwargs)
#         return inner
#     return outer
#
# @limiter(10)
# def s(a, b):
#     res = a + b
#     return res
#
# print(s(432, 765))
# time.sleep(6)
# print(s(4, 3))
# def inter(a):
#     sq = a ** 0.5
#     return True if sq == int(sq) else False

# print(inter(16))

# def search(nums, target):
#     first = nums[0]
#     last = nums[-1]
#     res = []
#
#     while first <= last:
#         mid = first + (last - first) / 2
#         if mid == target:
#             res.append(nums[mid])
#             first = mid
#         elif mid > target:
#             last = mid
#     return res
#
# print(search([5,7,7,8,8,10], 8))




# def c(nums1, nums2):
#     res = []
#     n1 = set(nums1).difference(set(nums2))
#     n2 = set(nums2).difference((set(nums1)))
#     res.append(list(n1))
#     res.append(list(n2))
#     return res
#
#
# print(c([1,2,3], [2, 4, 6]))

# def rev(num):
#     frst = str(abs(num))[::-1]
#     res = int(frst) * (1 if num > 0 else -1)
#     if res < -2 ** 31 or res > 2 ** 31 + 1:
#         return 0
#     return res
#
# print(rev(-124))
# s = " the sky is blue "
# sl = []
# for char in s.split():
#     sl.append(char)
# print(" ".join(sl[::-1]))

# l = [1234, 2, 5, 3, 8, 9, 7]
# a = l.pop()
# l.insert(0, a)
# print(l)


# def repl(nums, k):
#     c = k % len(nums)
#     sec, frst = nums[-c:], nums[:-c]
#     return sec + frst
# print(repl([1,2,3,4,5,6,7], 3))


# def find(nums):
#     cand = None
#     c = 0
#     for num in nums:
#         if c == 0:
#             cand = num
#         c += 1 if num == cand else -1
#     return cand
#
# print(find([3,2,3]))

# def cakes(rec, ava):
#     res = []
#     for name, val in rec.items():
#         if name not in ava.keys():
#             return 0
#         else:
#             res.append(ava[name] // val)
#     return min(res)
#
#
# print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))


# letters = 'abcdefghijklmnopqrstuvwxyz'
#
# def true_code(sps):
#     res = []
#     for word in sps:
#         clean = []
#         for char in word.lower():
#             if char == "c":
#                 clean.append("z")
#             elif char == "b":
#                 clean.append("y")
#             elif char == "a":
#                 clean.append("x")
#             else:
#                 i = letters.index(char)
#                 clean.append(letters[i-3])
#         res.append("".join(clean))
#     return " ".join(res)
#
#
# print(true_code(['L', 'mxvw', 'zdqw','brx', 'wr', 'nqrz','wkdw', 'L', 'dp','uhdgb', 'wr', 'jr']))

b = list(range(2000000))

def binat(lst, tar):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == tar:
            return lst[mid]
        elif lst[mid] < tar:
            left = mid + 1
        elif lst[mid] > tar:
            right = mid - 1
    return -1

c = b.index(5436)


