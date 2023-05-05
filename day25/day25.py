# Challenge #1
import csv
with open("weather_data.csv") as data:
    data_file = csv.reader(data)
    temperatures = []
    for row in data_file:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


# Challenge #2
import pandas
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
print(f"Average temperature: {data['temp'].mean():.2f}")
print(f"Maximum temperature: {data['temp'].max()}")
highest_temp_row = data[data.temp == data.temp.max()]
print(highest_temp_row)
monday = data[data.day == "Monday"]
print(int(monday.temp))


# Challenge #3
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamon = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
gray = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
white = squirrel_data[squirrel_data["Primary Fur Color"] == "White"]
black = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
print(len(black))

data_dact = {
    "Fur Color": ["cinnamon", "gray", "white", "black"],
    "Count": [len(cinnamon), len(gray), len(white), len(black)]
}

df = pandas.DataFrame(data_dact)
df.to_csv("squirrel_count.csv")


# Challenge #4
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x = data["x"].to_list()
y = data["y"].to_list()

answers = []

while len(answers) < len(states):
    answer_state = screen.textinput(title=f"{len(answers)}/{len(states)} states correct",prompt="What's another state name?")
    if answer_state == "exit":
        diff = list(set(states) - set(answers))
        print(diff)
        break

    if answer_state.title() in states:
        if answer_state.title() not in answers:
            answers.append(answer_state.title())
        index = states.index(answer_state.title())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x[index]), int(y[index]))
        t.write(answer_state)

screen.exitonclick()