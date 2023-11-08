1. 
numbers = [4,0,5,13,54,43]
max_value = max(numbers, key=lambda x: x)
print(max_value)

2. 
num = lambda x: x % 2 == 0
print(num(4))
print(num(7))

3. 
words = ["Google", "Samsung", "Game", "Tiktok", "Telegram"]
min_num = 6

filtered = filter(lambda x: len(x) > min_num, words)
result = list(filtered)
print(result)

4. 
with open("home.txt","r") as txt:
    content = txt.read()
    print(content)

5. 
with open('output.txt','w') as txt:
    txt.write("Hello")