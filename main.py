import turtle
import time
import scoreboard
import snake
import food

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        score.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
