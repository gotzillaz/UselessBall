from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty

class UselessBall(Widget):
    vx = NumericProperty(1)
    vy = NumericProperty(1)

    def velo(self,xx,yy):
        self.vx = xx
        self.vy = yy

    def move(self):
        self.x += self.vx
        self.y += self.vy

class UselessJoy(Widget):
    nx = NumericProperty()
    ny = NumericProperty()

    def on_touch_down(self,touch):
        pass

class UselessGame(Widget):
    ball = ObjectProperty(None)
    #joy = ObjectProperty()
    
    def update(self,dt):
        self.bounce_ball(self.ball)

    def bounce_ball(self,ball):
        if ball.y < 0:
            ball.y = 0
        elif ball.y > self.height-ball.height:
            ball.y = self.height-ball.height
        if ball.x < 0:
            ball.x = 0
        elif ball.x > self.width-ball.width:
            ball.x = self.width-ball.width

class UselessApp(App):
    def build(self):
        game = UselessGame()
        Clock.schedule_interval(game.update , 1.0/60)
        return game

if __name__ == '__main__':
    UselessApp().run()
