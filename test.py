import enchant
d = enchant.Dict("en_US")

print(d.check("Hello"))

print(d.check("helo"))

print(d.suggest("helo how are you"))