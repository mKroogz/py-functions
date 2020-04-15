def run(*kids):
    for kid in kids:
        print(f"{kid} ran around the playground")
def swing(*kids):
    for kid in kids:
        print(f"{kid} was swinging until the sun went down")
def slide(*kids):
    for kid in kids:
        print(f"{kid} went down the slide")
def hide_and_seek(*kids):
    for kid in kids:
        print(f"{kid} went to hide")

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Courtney", "Kevin")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")