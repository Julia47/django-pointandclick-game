import random


def get_random_answers(data_list):
    return random.sample(data_list, len(data_list))

print(get_random_answers(["heyy", "aaa", "ff"]))

print(type(eval("[\"a\", \"b\"]")))
