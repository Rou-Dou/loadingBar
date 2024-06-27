from loadingBar import *

some_list: list[str] = []
some_other_list: list[str] = []

for i in 'thehappycowsdfasdfasdfsdf':
    some_list.append(i)

for j in 'jal;sdjasdjfsjdfjasdf;jaslkdfjdjfdjfkdfjdkfdkfjf':
    some_other_list.append(j)

the_list_list = [some_list, some_other_list]


for list in the_list_list:
    len_list: int = len(list)
    print(f'\nloading {len_list} objects\n')

    for count, item in enumerate(list, 1):
        loadingBar(count, len_list)
        sleep(0.2)


print('All objects loaded')