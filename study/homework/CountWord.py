text = """Love makes the world go around.
Love to us human is what water to fish.Love shines the most beautiful light of humanity,we born in
it,we live by it.Too often we take it as granted,but we should know love is a priceless gift we should
cherish.But how to cherish the love?I have heard a saying :the quickest way to receive love is to give it;
the fastest way to lose love is to hold it too tightly the best way to keep love is to give it wings.
It is important for us to learn to love as the first class in our life.Only when you know how to love than
you will be a real man in this world.Love brings us warmth in the fearful coldness,love brings us bright
when life gets hard and dark.Love brings us confidence toward life when we are tired out and want to
give up.
Love deserves all the admiring words,and love is even beyond the life and death.That is what love is
all about in my eyes."""

# 统计
text_list = text.replace('\r', ' ').replace('\n', ' ').replace('-', '').replace(
    '.', ' ').replace(',', ' ').replace('?', ' ').replace(':', ' ').replace('"', ' ').split(' ')
# print(text_list)
text_list = [t.strip().lower() for t in text_list if t.strip() != '']
text_dict = dict()
for word in text_list:
    if word not in text_dict:
        text_dict[word] = 1
    else:
        text_dict[word] += 1
# print(text_dict)
text_freq = []
for k in text_dict:
    text_freq.append((k, text_dict[k]))
# print(text_freq)

# 排序
text_freq.sort(key=lambda x: x[1], reverse=True)
max_print = 5
times = 0
for t in text_freq:
    print("%8s : %2d" % t)
    times += 1
    if times > max_print:
        break
