from time import sleep

ingredients = ["4 cups of raspberries", "1 cup sugar", "3/4 cup flour", "1 egg"]

def recipe(items):
    for i in items:
        print("- " + i)
        sleep(1)


for i in ingredients:
    print(i)
    sleep(1)   

print(" ")
recipe(ingredients)