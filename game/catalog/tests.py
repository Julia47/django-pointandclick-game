from django.test import TestCase
import random
import pandas as pd
# import this
# Create your tests here.
# template
# <button onClick="sendAnswer(question={{questionId}})>
#  ...
#    <select>
#       {{ for x in answers }}
#  |
#  | <---- параметри для генерації
#  |           шаблона(наприклад список відповідей)
#  | <---- конфігурацію аджакс для запитів до сервера
#  |
#  V
#  <button id="sendAnswer(question=12)>
#    <select id....>
#        <item> Yes </item>
#        <item> No </item>

# def group_data[data_list]:
#     result_list = []
#     temp_list = []
#     for d in data_list:
#         temp_list.append(d)
#         if d < 0:
#             result_list.append(temp_list)
#             temp_list = []

# grouped_obj = [].groupby(["Class"])
# for key, item in grouped_obj:
#     print("Key is: " + str(key))
#     print(str(item), "\n\n")

test_data = [{'done': True, 'correct': "heyy"}, {'done': False, 'correct': "fine"}]
#print(test_data.pop()['correct'])

def test_func():
    while True:
        print("RETURN__FROM__NEXT")
        t = yield
        print("_____SEND_________")

        if type(t) == str:
            raise StopIteration
            #break
        t['v'] = [1, 2, 3]
        yield t
        print("_____NEXT________-")

        # if t['correct'] == "fine":
        #     print("heyy")

        
        # if t == "fine":
        #     print("YESSS")


test_f = test_func()
test_f.send(None)

print(test_f.send({'done': True, 'correct': "heyy"}))

test_f.send("heyy")

test_f.send({'done': False, 'correct': "fine"})
test_f.send({'done': False, 'correct': "fine"})
#print(next(test_f))


# for t in test_data:
#     test_f.send(t)

test_f.close()











# def count_common_letters(results):
#     letters = {}

#     while True:
#         word = yield
#         word = word.lower()
#         for c in word:
#             if c.isalpha():
#                 if c not in letters:
#                     letters[c] = 0
#                 letters[c] += 1

#         counted = sorted(letters.items(), key=lambda kv: kv[1])
#         counted = counted[::-1]

#         results.clear()
#         for item in counted:
#             results.append(item)


# names = ['Skimpole', 'Sloppy', 'Wopsle', 'Toodle', 'Squeers',
#          'Honeythunder', 'Tulkinghorn', 'Bumble', 'Wegg',
#          'Swiveller', 'Sweedlepipe', 'Jellyby', 'Smike', 'Heep',
#          'Sowerberry', 'Pumblechook', 'Podsnap', 'Tox', 'Wackles',
#          'Scrooge', 'Snodgrass', 'Winkle', 'Pickwick']

# results = []
# counter = count_common_letters(results)
# counter.send(None)  # prime the coroutine

# for name in names:
#     counter.send(name)  # send data to the coroutine

# counter.close()  # manually end the coroutine

# for letter, count in results:
#     print(f'{letter} apppears {count} times.')
