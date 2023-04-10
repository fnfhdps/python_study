import _pickle

# with open('profile.pickle', 'rb') as profile_file:
#     print(_pickle.load(profile_file))
# #close 필요 없음

# with open('study.txt', 'w', encoding='utf-8') as study_file:
#     study_file.write('파이썬을 열심히 공부하고 있어요')

with open('study.txt', 'r', encoding='utf-8') as study_file:
    print(study_file.read())