def fora(x):
    a = x

    def dentro():
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())