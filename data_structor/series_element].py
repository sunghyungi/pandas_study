import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)
print()

print("sr[0] = {}".format(sr[0]))
print("sr['이름'] = {}\n".format(sr['이름']))

print("sr[[1, 2]]\n".format(sr[[1, 2]]))
print("sr[['생년월일', '성별']]\n{}\n".format(sr[['생년월일', '성별']]))

print("sr[1: 2]\n{}".format(sr[1: 2]))
print("sr['생년월일': '성별']\n{}".format(sr['생년월일': '성별']))
