import re
import csv

# .     - matches any character.
# /.    - macthes dot character.
# //    - matches back slash character.
# /*    - matches astrick.

# [abcd]    - any character which matches either 'a' or 'b' or 'c' or 'd'.
# [^abcd]   - any character expect 'a' or 'b' or 'c' or 'd'.
# [a - z]   - any character from 'a' to 'z'.

# \w    - Word character which includes [a-zA-Z0-9_]. Matches alphanumericals and underscore.
# \W    - Any character expect word character [a-zA-Z0-9_]. Matches anything expect word character.
# \d    - Matches a digit. Same as [0-9].
# \D    - Matches expect a digit. Same as [^0-9].
# \s    - Matches only white space.
# \S    - Matches only non white space character.

# ^     - Starting of string.
# $     - Ending of string.
# \b    - Word boundry[a-zA-Z0-9_].
# \B    - Not word boundry.
# [ ]   - Matches character in square bracket.
# [^ ]  - Matches character expect in square bracket.

# Meta character that needs to be Escaped
# . ^ $ * + ? { } [ ] \ | ( )

# print(re.findall(r"\bthe\b", "the theory of relativity"))
# print(re.findall(r"cat", "The dragging belly indicates your cat is too fat"))
# print(re.findall(r"python", 'python and java are object oriented'))
# print(re.findall(r"aeiou", 'hello how are you doing anna'))
# print(re.findall(r"aeiou", "hello how are you doing anna, aeiou"))
# print(re.findall(r"[sS]mith", "smith"))
# print(re.findall(r"[sS]mith", "Smith"))
# print(re.findall(r"s[ae]p[ae]rate", "seperate"))
# print(re.findall(r"s[ae]p[ae]rate","saparate"))
# print(re.findall(r"[aeiou]", 'hello how are you doing anna'))
# print(re.findall(r"[abcd]", 'hello world'))
# print(re.findall(r"[aeiou]", 'abcdefghijk'))
# print(re.findall(r"[0123456789]+", 'The cost of the book is Rs.100'))
# print(re.findall(r"<h[123456]>", "<h1>"))
# print(re.findall(r"<h[123456]>", "<h2>"))
# print(re.findall(r"<h[123456]>", "<h3>"))
# print(re.findall(r"<h[123456]>", "<h4>"))
# print(re.findall(r"<h[123456]>", "<h5>"))
# print(re.findall(r"<h[123456]>", "<h6>"))

# print(re.findall(r"[0-9]", 'The cost of the book is Rs.100'))
# print(re.findall(r"[a-z]+", 'hello HOW ARE YOU'))
# print(re.findall(r"[a-zA-Z]+", 'hello HOW ARE YOU'))

# sentence = "Hello World Welcome To Python"
# upper = re.findall(r"[A-Z]", sentence)
# lower = re.findall(r"[a-z]", sentence)
#
# print(len(upper))
# print(len(lower))
# sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"
# count_spaces = re.findall(r" ", sentence)
# print(len(count_spaces))

# sentence = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
# chars = re.findall(r"[a-zA-Z]", sentence)
# d = {char : chars.count(char) for char in chars}
# print(d)

# +     - Accepts one or more character.
# print(re.findall(r"[0-9]+", 'The cost of the book is Rs.100'))
# print(re.findall(r"[abcd]+", 'abcdefg acbdhijkab'))
# print(re.findall(r"an+a", "annnnnnnnnnnnnnnnna"))
# print(re.findall(r"[a-zA-Z]+", "Hello World Welcome To Python Programming Pyt123on"))
# sentence = "Hi there! How are you:) How are you doing today!"
# words = re.findall(r"[a-zA-Z]+", sentence)
# count_words = {word : len(word) for word in words}
# print(count_words)
# word = "Pytho12nReg567exp2"
# nums = re.findall(r"\d", word)
# lis_count = sum([int(num) for num in nums])
# print(lis_count)
# word = "Pytho12nReg567exp2"
# nums = re.findall(r"[0-9]+", word)
# count_ = sum([int(num) for num in nums])
# print(count_)
# total = 0.0
# for num in nums:
#     total += int(num)
# print(total)
# message = "Downloading file archive.zip to downloads folder..."
# image.jpeg
# index.xhtml
# python.py
# extension_match = re.findall(r"[a-zA-Z]+\.[a-zA-Z]{2,3}", message)
# print(extension_match)

# ?     - One or zero macthes of the previous experssion.
# print(re.findall(r"colou?r", "color"))
# print(re.findall(r"colou?r", "colour"))
# print(re.findall(r"https?://\w{3}\.\w+\.\w{3}", 'https://www.google.com'))
# print(re.findall(r"https?://", 'http://www.google.com'))
# print(re.findall(r"July?", "Jul the 26th day"))
# print(re.findall(r"July?", "July the 26th day"))
# print(re.findall(r"ann?a", "anna"))
# print(re.findall(r"ann?a", "ana"))

# *     - Matches zero or more occurances of the previous expression.
# print(re.findall(r"an*a", "aa"))
# print(re.findall(r"an*a", "annna"))
# print(re.findall(r"an*a", "ana"))

# print(re.findall(r"[a-zA-Z]+\(?\d*\)?", "Index(10)"))
# print(re.findall(r"Index\(?\d*\)?", "Index"))
# print(re.findall(r"[^abcd]", 'abcdefg hijkab'))

# print(re.findall(r"\d+", 'The cost of the book is Rs.100'))
# print(re.findall(r"[0-9]+", 'The cost of the book is Rs.100'))

# print(re.findall(r"[^abcd]+", 'abcdefg hijkab'))
# word = '@hello12world34welcome!123'
# print(re.findall(r"[^0-9]+", word))
# print(re.findall(r"[^0-9]", word))

# sentence = 'hello@world! welcome!!! Python$ hi26 how are you & where are you?'
# print(re.findall(r"[^a-zA-Z0-9_\s]", sentence))
# print(re.findall(r"[^\w\s]", sentence))

# print(re.findall(r"^hello", "hello world"))
# print(re.findall(r"hello world$", "hello world"))

# print(re.findall(r"hello$", "world hello"))
# print(re.findall(r"hello$", "hello world"))
# print(re.findall(r"hello$", 'hello world welcome to python'))

# with open("Datasets\\sample.log")as file:
#     for line in file:
#         match = re.findall(r".*UDP$", line)
#         if match:
#             print("".join(match))

# with open("Datasets\\sample.log") as f:
#     for line in f:
#         match = re.findall(r".*UDP$", line)
#         if match:
#             print("".join(match))

# print(re.findall(r"^hello$", "hello"))
# print(re.findall(r"\d{3}-\d{4}-\d{3}", '456-9832-098'))
# print(re.findall(r"[89]\d{2}-\d{3}-\d{3}", '800-123-123'))
# print(re.findall(r"[89]\d{2}-\d{3}-\d{3}", '900-123-123'))

# print(re.findall(r"\bday\b", "what a beautiful day today is"))
# print(re.findall(r"\bh[\w]+", 'hello world hi hello universe how are you happy birthday'))
# print(re.findall(r"\bh[a-zA-Z0-9_]+", 'hello world hi hello universe how are you happy birthday'))

# print(re.findall(r"[PJ]\w+", 'Python is a programming language. Python is easier than Java'))
# print(re.findall(r"[PJ][a-zA-Z0-9_]+", 'Python is a programming language. Python is easier than Java'))
# print(re.findall(r"\b[a-zA-Z0-9_]+y\b", 'hello world hi hello universe how are you happy birthday feeling very sleepy flying'))

# print(re.findall(r"[\w]+y$", 'hello world hi hello universe how are you happy birthday feeling very sleepy flying'))
# sentence = "hello hi american engieers and indian writers officers united states"
# print(re.findall(r"[aeiou][a-zA-Z0-9_]+", sentence))
# print(re.findall(r"[aeiou]\w+", sentence))

# print(re.findall(r"\b[A-Z]+\b", "This is PYTHON programming LANGUAGE and REGEX"))
# print(re.findall(r"\b[a-z]+\b","This is PYTHON programming LANGUAGE and REGEX"))

# print(re.findall(r"\b[a-zA-Z0-9_]+\.pdf\b", "downloading apple.pdf to downloads folder"))
# print(re.findall(r"\b\w+\.pdf\b", "downloading apple.pdf to downloads folder"))

# sentence = "hello hi how are you what is your name he is older than me how old are you"
# print(re.findall(r"\b\w{3}\b", sentence))
# print(re.findall(r"\b[a-zA-Z0-9_]{3}\b", sentence))

# print(re.findall(r"\b\d{4}\b", "Copyright 1998. All rights reserved"))
# print(re.findall(r"\b[0-9]{4}\b", "Copyright 1998. All rights reserved"))

# (?:he|se)     -- Non group capturing.
# (he|se)       -- Group capturing.
# sentence = "he helps the community and he is the hero of the day she sells sea shells on the sea shore"
# print(re.findall(r"(?:he|se)[a-zA-Z0-9_]+", sentence))
# print(re.findall(r"(he|se)[a-zA-Z0-9_]+", sentence))

# line = "03/22 08:51:06 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available."
# print(re.findall(r"[A-Z]+", line))
# print(re.findall(r"\b[A-Z]+", line))
# print(re.findall(r"[A-Z]+\b", line))
# print(re.findall(r"\b[A-Z]+\b", line))

# print(re.findall(r"\d", "654 this string is starting with 12 and ending with numbers 289423784612 890"))
# print(re.findall(r"\d+", "654 this string is starting with 12 and ending with numbers 289423784612 890"))
# print(re.findall(r"\d{3}", "654 this string is starting with 12 and ending with numbers 289423784612 890"))
# print(re.findall(r"\b\d{3}\b", "654 this string is starting with 12 and ending with numbers 289423784612 890"))
# print(re.findall(r"\b\d{3}\b$", "4632746327 this string is ending with 235"))
# print(re.findall(r"^\b\d{3}\b","654 this string is starting with and ending with numbers 289423784612"))
# print(re.findall(r"^\b\d{3}\b$","654 this string is starting with and ending with numbers 289423784612"))

# ^     -- starts of the string or sentence.
# $     -- ends of the string or sentence.

# def count_spaces():
#     count = 0
#     with open("Datasets\\sample.log") as file:
#         for line in file:
#             if line.strip():
#                 matches = re.findall(r"\s", line)
#                 count += len(matches)
#     return count

# print(count_spaces())

# def count_caps():
#     caps_count = 0
#     with open("Datasets\\sample.log") as file:
#         for line in file:
#             matches = re.findall(r"\b[A-Z]+\b", line)
#             caps_count += len(matches)
#     return caps_count

# print(count_caps())

# def count_cap_char():
#     cap_char = 0
#     with open("Datasets\\sample.log")as file:
#         for line in file:
#             matches = re.findall(r"[A-Z]", line)
#             cap_char += len(matches)
#     return cap_char

# print(count_cap_char())

# def count_messgaes(messages):
#     count_messages = 0
#     with open("Datasets\\sample.log")as file:
#         for line in file:
#             matches = re.findall(messages, line)
#             count_messages += len(matches)
#     return count_messages

# def count_messgaes(message):
#     total_messages = 0
#     with open("Datasets\\sample.log")as file:
#         for line in file:
#             matches = re.findall(message, line)
#             total_messages += len(matches)
#     return total_messages

# print(count_messgaes("INFO"))
# print(count_messgaes("TRACE"))
# print(count_messgaes("EVENT"))

# def get_ip():
#     ip = set()
#     with open("Datasets\\sample.log")as file:
#         for line in file:
#             if line.strip():
#                 line_split = line.split()
#                 ip.add(line_split[1])
#     return ip

# print(get_ip())

# def get_ip_regex():
#     ips = set()
#     with open("Datasets\\sample.log")as file:
#         for line in file:
#             matches = re.findall(r"\d{2}:\d{2}:\d{2}", line)
#             if matches:
#                 ips.add(matches[0])
#     return ips

# print(get_ip_regex())

# def get_all_ips():
#     ip = set()
#     with open("Datasets\\sample.log")as file:
#         for line in file:
#             matches = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
#             if matches:
#                 ip.add(matches[0])
#     return ip

# print(get_all_ips())

# def get_all_ip():
#     """Extract all the ip addresses in the sample log file"""
#     ips = [ ]
#     with open('Datasets\\sample.log') as f:
#         for line in f:
#             ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
#             if ip:
#                 for item in ip:
#                     ips.append(item)
#     return ips

# print(get_all_ip())

# def count_word():
#     word_count = 0
#     with open("Datasets\\sample.log")as file:
#         for line in file:
#             matches = re.findall(r"\b[a-zA-Z]+\b", line)
#             if matches:
#                 word_count += len(matches)
#     return word_count

# print(count_word())

# def count_number_letter():
#     letter_count = 0
#     with open("Datasets\\sample.log")as file:
#         for line in file:
#             matches = re.findall(r"[a-zA-Z]", line)
#             if matches:
#                 letter_count += len(matches)
#     return letter_count

# print(count_number_letter())

# with open("Datasets//sample.log")as file:
#     for line in file:
#         print(line)

# def regex_strip(line):
#     new_line = re.sub(r"(^\s*|\s*$)", "", line)
#     return new_line

# sen = "              jai sri ram          "
# print(regex_strip(sen))
# print(regex_strip("     jai sri ram"))
# print(regex_strip("jai sri ram           "))

# def count_start_end_spacs(line):
#     start_spaces = re.findall(r"^\s*", line)
#     end_spaces = re.findall(r"\s*$", line)
#     str_staring = len("".join(start_spaces))
#     str_ending = len("".join(end_spaces))
#     return str_staring, str_ending

# print(count_start_end_spacs(sen))

# print(re.findall(r"(python | java)", 'python and java are object oriented'))

# sentence = 'The meeting is between 9:00 am and 12:30 pm'
# print(re.findall(r"[0-9]?[0-9]:[0-9][0-9]\s(?:am|pm)", sentence))

# _dates = ['2019-01-02', '2019-12-02', '2019-12-26', '26-08-2019', '20-19-20', '2019-12-31', '2019-12-32']

# for date in _dates:
    # print(re.findall(r"\d{2,4}-\d{2}-\d{2}", date))
    # print(re.findall(r'\d{4}-(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|[12][0-9]|3[01])', date))


# r"\d{4}-(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[12])"
# print(re.findall(r"\d{4}-(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])", "2012-31-12"))

# for date in _dates:
#     print(re.findall(r"\d{2,4}-(?:0[0-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])", date))

# sentence = "Hello world welcome to python"
# print(re.sub(r"\s", "\n", sentence))

# sentence = 'hello123world welcome456to python012'
# print(re.sub(r"\d", "*", sentence))

# sentence = 'hello#$%world welcome@!#$%to python*&^%'
# print(re.sub(r"[^a-zA-Z0-9\s]", "*", sentence))

# sentence = "Java and Python are programming languages"
# print(re.sub(r"\sand\s", " & ", sentence))

# with open("Datasets\\sample_python.txt", "w")as file:
#     fw = csv.writer(file)
#     fw.writerow(["Python is very easy"])
#     fw.writerow(["Python is not difficult"])
#     fw.writerow(["Any one can learn python"])

# with open("Datasets\\sample_python.txt") as fr:
#     with open("Datasets\\sample_java.txt", "w") as fw:
#         for row in fr:
#             new_line = re.sub(r"(python|Python)", "Java", row)
#             fw.write(new_line)


# matches = re.finditer(r"hello", 'hello world welcome to python hello world')
# # print(list(matches))
#
# val_start_end = [(match.start(), match.end(), match.group()) for match in matches]
# print(val_start_end)

# for match in matches:
#     print(match.group())

# print(re.findall(r".", "hello world"))
# print(re.findall(r"h.", "hellho worhld"))
# print(re.findall(r"h.", "hello world hi how how are you"))
# print(re.findall(r"a.c", "agc"))
# print(re.findall(r"a.b", "a b"))
# print(re.findall(r"a.b", "ab"))
# print(re.findall(r"a.b", "abbde"))
# print(re.findall(r"a.b", "a*b a?b"))
# print(re.findall(r"a.a","ana"))
# print(re.findall(r"a..a", "anna"))
# print(re.findall(r"a.*a", "ananannnnna"))
# print(re.findall(r"a.*a", "aa"))
# print(re.findall(r"^a.*a$", "annnnnnnna"))
# print(re.findall(r"^a.*a$", "ana"))
# print(re.findall(r"a.+a", "aa"))
# print(re.findall(r"a.+a", "aa"))
# print(re.findall(r"(world)\1", "thethe python world hello worldworld the"))
# print(re.findall(r"(the)\1", "the the python hello world world the"))
# print(re.findall(r"([a-z]+\s)\1", "the the python the hello world world the"))
# m = re.finditer(r"([a-z]+\s)\1{2}", "the the python hello world world the the the ")
# print(list(m))
# print(re.findall(r"([a-z]+\s)\1{2}", "the the python hello world world the the the "))
# print(list(re.finditer(r"([a-z])\1", "hello hurry programming")))
# print(list(re.finditer(r"([0-9])\1", "hello 123345, welcome to 001 98799")))
# print(list(re.finditer(r"([0-9]+\s)\1", "hello 12345 12345 , welcome to 001 98799")))
# print(list(re.finditer(r"([0-9]+\s)\1", "hello 12345 12345 , welcome to 001 98799")))
# print(re.findall(r"([0-9])+", "hello 1234512345 , welcome to 00198799"))

# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def move(self, dx, dy):
#         self.a = self.a + dx
#         self.b = self.b + dy
#
#     def reset(self):
#         self.a = 0
#         self.b = 0
#
#     def sort(self):
#         if self.a < self.b:
#             return (self.a, self.b)
#         return (self.b, self.b)
#
#     def swap(self):
#         temp = self.a
#         self.a = self.b
#         self.b = temp
#         return (self.a, self.b)
#
#     def total(self):
#         return self.a + self.b
#
# class Arithmetic:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         if self.a < self.b:
#             return self.b - self.a
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
# class Employee:
#     def __init__(self, fname, lname, age, pay):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.pay = pay
#
#     def email(self, company):
#         return f"{self.fname}.{self.lname}@{company}.com"
#
#     def pay_hike(self, percentage):
#         hike = self.pay * percentage
#         self.pay = self.pay + hike
#         return self.pay
#
# class Point:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __init__(self, a = 0, b = 0):
#         self.a = a
#         self.b = b
#
#
# class Players:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.health = 100
#
#     def attack(self, points):
#         self.health -= points
#
#
# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __len__(self):
#         return 2
#
#     def __contains__(self, item):
#         if self.a == item or self.b == item:
#             return True
#         return False
#
#     def __getitem__(self, index):
#         if index == 0:
#             return self.a
#         elif index == 1:
#             return self.b
#         else:
#             raise IndexError("Index out of range")
#
#     def __setitem__(self, index, value):
#         if index == 0:
#             self.a = value
#         elif index == 1:
#             self.b = value
#         else:
#             raise IndexError("Index out of range")
#
# class PositivePoint(Point):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#
#     def __setitem__(self, index, value):
#         if not isinstance(value, (int, float)):
#             raise Exception("Value should be number")
#         if value < 0:
#             raise Exception("Negative value cannot be updated")
#         super().__setitem__(index, value)
#
# class RangePoint(Point):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#
#     def __setitem__(self, index, value):
#         if index == 0:
#             if value in range(0, 101):
#                 super().__setitem__(index, value)
#             else:
#                 raise Exception("Value should be between 0 to 100")
#         elif index == 1:
#             if value in range(0, 51):
#                 super().__setitem__(index, value)
#             else:
#                 raise Exception("Value should be between 0 to 50")
#
# class Points:
#     def __init__(self, *values):
#         self.points = [*values]
#
#     def __len__(self):
#         return len(self.points)
#
#     def __contains__(self, item):
#         return True if item in self.points else False
#
#     def __setitem__(self, index, value):
#         self.points[index] = value
#
#     def __getitem__(self, index):
#         return self.points[index]
#
# class Point2:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __eq__(self, other):
#         return True if self.a == other.a and self.b == other.b else False
#
#     def __lt__(self, other):
#         return True if self.a < other.a else False
#
#     def __gt__(self, other):
#         return True if self.a > other.a else False

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return True if self.age == other.age else False

    def __lt__(self, other):
        return True if self.age < other.age else False

    def __gt__(self, other):
        return True if self.age > other.age else False

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        n1 = self.a + other.a
        n2 = self.b + other.b
        return Point(n1, n2)

    def __sub__(self, other):
        n1 = self.a - other.a
        n2 = self.b - other.b
        return Point(n1, n2)

    def __mul__(self, other):
        n1 = self.a * other.a
        n2 = self.b * other.b
        return Point(n1, n2)


class Point2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, name, value):
        if value < 0:
            raise Exception("Negative values are not allowed")
        if not isinstance(value, (int, float)):
            raise Exception("Only int and float values are allowed")
        super().__setattr__(name, value)

class Person2:
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname

    def __setattr__(self, name, value):
        super().__setattr__(name, value.upper())

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise Exception("Only numbers are allowed")
        super().__setattr__(name, value)

    def __add__(self, other):
        return self.a + self.b

    def __sub__(self, other):
        return self.a - self.b

    def __mul__(self, other):
        return self.a * self.b

class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def __setattr__(self, name, value):
        if name == "fname" or name == "lname":
            if len(name) > 5:
                raise Exception("Length should not be more then 5")
            super().__setattr__(name, value)
        elif name == "pay":
            if not isinstance(value, (int, float)):
                raise Exception("Only numbers are allowed")
            super().__setattr__(name, value)

    def hike_salary(self, percentage_hike):
        hike_amount = self.pay * percentage_hike
        self.pay = self.pay + hike_amount

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self, age):
        return True if self.age > 18 else False

    def __len__(self, name):
        return 1 if len(name) > 5 else 0

class Point3:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __bool__(self):
        return False if self.a < 0 and self.b < 0 else True

class Greeting:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"hello {self.name}")


class Squares:
    def __init__(self, numbers):
        self.numbers = numbers

    def __call__(self):
        squares = [ ]
        for number in self.numbers:
            squares.append(number ** 2)
        return squares

class Time:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        from time import time
        start = time()
        result = self.func(*args, **kwargs)
        end = time()
        print(f"The execution time of the function {self.func.__name__} : {end - start}")
        return result

class RecordCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs), self.count


@RecordCalls
@Time
def add(a, b):
    return a + b

items = ['bv', 'aw', 'dt', 'cu']

def get_last_char(item):
    return item[-1]

class get_char_last:
    def __call__(self, item):
        return item[-1]

temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]

def get_temp(item):
    return item[-1]

class GetTemp:
    def __call__(self, item):
        return item[-1]

portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

def by_name(item):
    return item['name']

def by_shares(item):
    return item['shares']

def by_price(item):
    return item['price']

class By:
    def __init__(self, by_what):
        self.by_what = by_what

    def __call__(self, item):
        if self.by_what == "name":
            return item["name"]
        elif self.by_what == "shares":
            return item["shares"]
        elif self.by_what == "price":
            return item['price']
        else:
            raise Exception("Unknown key or field name")

class Parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print("This is new addition")
        print(f"Executing parent class apple method : {self.value}")

    def google(self):
        print("Executing parent class google method")
        self.apple()

class Child1(Parent):
    def __init__(self, value):
        # super().__init__(value)
        Parent.__init__(self, value)

    def yahoo(self):
        print("executing child1 yahoo")

class Child2(Parent):
    def __init__(self, value):
        super().__init__(value)

    def apple(self):
        print("Executing child2 apple method")

class Child3(Parent):
    def __init__(self, value):
        super().__init__(value)

    def apple(self):
        print("some extra stuff in child3")
        super().apple()

class Child4(Parent):
    def __init__(self, value, extra_value):
        super().__init__(value)
        self.extra_value = extra_value

    def facebook(self):
        print(f"some extra thing : {self.extra_value}")

class Parent2:
    def __init__(self, extra_value):
        self.extra_value = extra_value

    def facebook(self):
        print(f"Parent2 facebook : {self.extra_value}")

class Child5(Parent, Parent2):
    def __init__(self, value, extra_value):
        Parent.__init__(self, value)
        Parent2.__init__(self, extra_value)

    def instagram(self):
        print("Child5 instagram is executing")

class A:
    def demo(self):
        print("A")

class B(A):
    def demo(self):
        print("B")
        super().demo()

class C(B):
    def demo(self):
        print("C")
        super().demo()

class Spam:
    a = 10
    def apple(self):
        print(f"Executing spam apple {self.__class__.a}")

class Demo(Spam):
    a = 20
    def google(self):
        print(f"Demo google {self.__class__.a}")
        print(f"Demo google {Spam.a}")
        print(f"Demo google {Demo.a}")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise Exception("Only Numbers are allowed")
        super().__setattr__(name, value)

    def circumference(self):
        return 2 * 3.14 * self.radius

class Circle2:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Only numbers are allowed")
        self._radius = value

    def circumference(self):
        return self._radius * 2 * 3.14

class Person2:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __setattr__(self, name, value):
        if name == "fname":
            if not isinstance(value, str):
                raise Exception("Value should be string")
            if len(value) < 5:
                raise Exception("Length of fname should be more then 5")
            super().__setattr__(name, value)
        elif name == "lname":
            if not isinstance(value, str):
                raise Exception("Value should be string")
            if len(value) < 5:
                raise Exception("Length of lname should be more then 5")
            super().__setattr__(name, value)
        elif name == "age":
            if not isinstance(value, (int, float)):
                raise Exception("Value should be integer or float")
            if value > 100:
                raise ValueError("Value cannot be more then 100")
            super().__setattr__(name, value)

class Person3:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    @property
    def fname(self):
        print("getter is running")
        return self._fname

    @fname.setter
    def fname(self, value):
        if not isinstance(value, str):
            raise Exception("Value should be string")
        if len(value) > 5:
            raise Exception("Value should be more then 5")
        print("settter running")
        self._fname = value

    @property
    def lname(self):
        print("getter is running")
        return self._lname

    @lname.setter
    def lname(self, value):
        if not isinstance(value, str):
            raise Exception("Value should be string")
        if len(value) > 5:
            raise Exception("Value should be more then 5")
        print("settter running")
        self._lname = value

    @property
    def age(self):
        print("getter is running")
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Only numbers are allowed")
        if value > 100:
            raise ValueError("Value should not be more then 100")
        print("settter running")
        self._age = value

    def email(self):
        # return f"{self._fname}.{self._lname}@company.com"
        return f"{self.fname}.{self.lname}@company.com"

class Calculator2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, name, value):
        if name == "a" or name == "b":
            if not isinstance(value, (int, float)):
                raise TypeError("Value should be integer or float")
            if value < 0:
                raise ValueError("value should be greater then 0")
            super().__setattr__(name, value)

class Calculator3:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def _is_number(self, value):
        if not isinstance(value, (int, float)):
            return False
        if value < 0:
            return False
        return True

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not self._is_number(value):
            raise Exception("Value should and number and should be greater then zero")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not self._is_number(value):
            raise Exception("Value should and number and should be greater then zero")
        self._b = value

class BankAccount:
    interest_rate = 0.04
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = [ ]
        self.transactions.append(f"Initial amount deposited ${balance}")

    def withdrawn(self, amount):
        if self.balance < amount:
            raise ValueError(f"Amount present in your account is not suff")
        self.balance -= amount
        self.transactions.append(f"Amount withdrawn from account {self.name} of rs ${amount}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Amount deposited to account {self.name} of rs ${amount}")

    def statement(self):
        for lis in self.transactions:
            print(lis)
        print("*" * 20)
        print(f"The current balance in your account is {self.balance}")

    def transfer(self, from_account, to_account, amount):
        if from_account.balance < amount:
            raise ValueError(f"Not having sufficeint amount in {from_account}")
        to_account.balance += amount
        from_account.balance -= amount
        from_account.transactions.append(f"Amount transfered to account {to_account} and ${amount}")
        to_account.transactions.append(f"Amount deposited from {from_account} and ${amount}")

    def roi(self):
        int_amount = self.balance * self.__class__.interest_rate
        self.balance += int_amount

# steve = BankAccount("Steve", 10000)
# mark = BankAccount("Mark", 20000)
#
# steve.deposit(2000)
# mark.withdrawn(2000)
# steve.transfer(steve, mark, 2000)
# mark.statement()
# steve.statement()

from json import loads

class Employee3:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay  = pay

    @classmethod
    def from_string(cls, emp_details):
        words = emp_details.split(",")
        fname, lname, pay = words
        return cls(fname, lname, pay)

    @classmethod
    def from_json(cls, response):
        json_obj = loads(response)
        fname = json_obj["firstname"]
        lname = json_obj["lastname"]
        pay = json_obj["pay"]
        return cls(fname, lname, pay)

    def email(self):
        return f"{self.fname}.{self.lname}@company.com"

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class SBIBank(Bank):
    def deposit(self):
        print(f"Depositing amount in SBIBank")

    def withdraw(self):
        print(f"Withdrawing amount in SBIBank")



































# #############################################################################################

# Operator
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x < y:
#     print("x is less then y")
# if y < x:
#     print("y is less then x")
# if x == y:
#     print("x and y are equal")

# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x < y:
#     print("x is less then y")
# elif y < x:
#     print("y is less then x")
# elif x == y:
#     print("x and y are equal")

# or    --

# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x < y or y < x:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# if x == y: print("x is equal to y")
# else : print("x is not equal to y")


# score = int(input("Score: "))
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
#
#
# score = int(input("Score: "))
# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")
#
#
# score = int(input("Score: "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# def main():
#     x = int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("odd")

# def is_even(n):
#     return True if n % 2 == 0 else False

# def is_even(n):
#     return n % 2 == 0
#
# main()

# name = input("What's your name? ")
#
# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor")
#     # case "Hermione":
#     #     print("Gryffindor")
#     # case "Ron":
#     #     print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")

# Loops     --


print(re.findall(r"^a.*a$", "ana"))
print(re.findall(r"a.+a", "aa"))



















































