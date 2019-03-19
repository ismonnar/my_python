s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"

res = [i for i in s.lower().split() if not i.startswith('м')]
print(' '.join(res))
