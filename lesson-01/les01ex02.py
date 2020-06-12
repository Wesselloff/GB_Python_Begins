print('Введите число секунд: ')
num = int(input())
hours = num // (60 * 60)
minutes = (num - hours * 60 * 60) // 60
seconds = num - hours * 60 * 60 - minutes * 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
