import json

types = []
before, after = [], []
f = open('rules_qw/rules_question_words_v11.txt')
for r in f.readlines():
  v = r.split('->')[0]
  if v not in before:
    before.append(r.split('->')[0])
    after.append(r.split('->')[1][:-1])
f.close()
after[-1] = after[-1]+'gì'

def dau_cau(s):
  return s[0].upper()+s[1:]

def apply_rules(question):
  for j, k in enumerate(before):
        ok = 0
        if k in question:
          question = question.replace(k, after[j])[:-1]+'?'
        if dau_cau(k) in question:
          question = question.replace(dau_cau(k), dau_cau(after[j]))[:-1]+'?'
  return question