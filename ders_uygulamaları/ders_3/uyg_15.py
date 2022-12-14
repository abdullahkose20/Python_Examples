# -----------------TURTLE--------------------------------------------

import turtle  # Turtle kütüphanesi dahil edildi

"""----------------------------------------------------------------------"""

tosbaga = turtle.Turtle()  # tosbaga adında bir bir model oluşturuldu

tosbaga.forward(50)  # modeli 50 birim ileri doğru hareket ettirir

tosbaga.backward(40)  # modeli 40 birim geriye doğru hareket ettirir

tosbaga.right(90)  # modeli 90 derece sağa doğru döndürür

tosbaga.left(45)  # modeli 45 derece sola doğru döndürür

tosbaga.color("blue", "red") # model renk ayarlaması: ilk renk çizilen çizgi rengi , ikici renk modelin rengi

tosbaga.goto(90, 90) # modeli belirli kordinatlara taşıma (x,y) !!! sayfa ortası (0,0) noktasıdır

tosbaga.circle(30)  # model yarıçapı 30 olan daire çizer

tosbaga.penup()  # modelin kalemini kaldırır ve model çizim yapmaz

tosbaga.pendown()  # modelin kalemini indirir ve model çizim yapar

tosbaga.fillcolor("blue") # çizilen şeklin kapalı olması durumunda dolgu rengini mavi yapar

tosbaga.begin_fill()  # şeklin çizilmesinden önce dolguyu başlatır

tosbaga.end_fill()  # şeklin çizildikten sonra dolguyu kapatır

tosbaga.speed(20)  # modelin hızını 20 yapar

tosbaga.shape("turtle") # kullanılan modelin şeklini değiştirme ("arrow", "turtle", "circle", "square", "triangle", "classic")

"""----------------------------------------------------------------------"""

pencere = turtle.Screen()  # pencere adında bir arayüz oluşturma

pencere.mainloop()  # arayüzün kapatma tuşuna basılmaz ise sürekli açık tutar

pencere.bgcolor("green")  # arayüzün arka plan rengini yeşil yapar

pencere.title("ABDULLAH KÖSE")  # arayüz başlık adını değiştirme

pencere.textinput("ayarlar", "adınıgir:") 

pencere.setup(width=100,height=100) #arayüz boyutları oluşturma 100x100 lük arayüz oluşturma

"""----------------------------------------------------------------------"""


"""
# örnek 1 // basit şekiller oluşturma

import turtle

# turtle nesnesini oluşturun
my_turtle = turtle.Turtle()

# Daire çizmek için kodunuzu buraya yazın
my_turtle.circle(50)

# Çokgen çizmek için kodunuzu buraya yazın
for i in range(6):
    my_turtle.forward(100)
    my_turtle.right(60)

# Kare deseni oluşturmak için kodunuzu buraya yazın
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Çember deseni oluşturmak için kodunuzu buraya yazın
for i in range(360):
    my_turtle.forward(1)
    my_turtle.right(1)

# Yıldız deseni oluşturmak için kodunuzu buraya yazın
for i in range(5):
    my_turtle.forward(100)
    my_turtle.right(144)


"""

"""
# örnek 2 // turtle ile büyüyen daireler çizimi

import turtle
loadWindow = turtle.Screen()
turtle.speed(10)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()

"""

"""
# örnek 3 // turtle ile rengarenk büyüyen altıgen

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

"""

"""
# örnek 4 //

"""

"""
# örnek 5 // türk bayrağı oluşturma

import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.title("ABDULLAH KÖSE")         # Başlık
w.setup(width=100,height=100)   # Pencere Boyutu
w.bgcolor("red")                # Arka Plan Kırmızı Yap

# İlk daire
t.up()
t.goto(-100,-100)               # Fare imleci lokasyonu
t.color('white')                # Beyaz renk
t.begin_fill()                  # Beyaz rengi doldur
t.circle(120)                   # Çapı
t.end_fill()

# Hilal yapabilmek için ikinci daire
t.goto(-70,-80)                 # Fare imleci lokasyonu
t.color('red')                  # Kırmızı renk
t.begin_fill()                  # Kırmızı rengi doldur
t.circle(100)                   # Çapı
t.end_fill()                    # Dolguyu Bitir

# Yıldız için hazırlık
t.goto(0,35)
t.fillcolor("white")
t.begin_fill()

# Yıldız için tekrar eden üçgen çizimi
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

t.goto(-130,-190)
t.color("white")
t.write("NCT MUCİT ATÖLYESİ", font=("Verdana", 17,"bold"))

# Fare imleci ekranda durup görüntüyü bozmasın diye uzaklaştırıyoruz :)
t.goto(-999,-0)

# Ekrana tıklayınca programın kapanmasını sağlar.
w.exitonclick()

"""

"""
# örnek 6 // yılan oyunu yapımı

import turtle
import time
import random
 
delay = 0.1
score = 0
high_score = 0
 
 
# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)
 
# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))
 
 
# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
 
def goright():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
 
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
 
segments = []
 
 
# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
 
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
 
wn.mainloop()

"""