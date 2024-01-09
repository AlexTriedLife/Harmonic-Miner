import random
import tkinter as tk
import numpy as np
import playsound as psnd

root = tk.Tk()
screen = tk.Canvas(root, width=800, height=600, bg="white")
screen.pack()

notes = np.array(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])

noteSounds = {
    "C": "D:\Projects\Python\Harmonic Miner\Audio\C.mp3",
    "C#": "D:\Projects\Python\Harmonic Miner\Audio\C.mp3",
    "D": "D:\Projects\Python\Harmonic Miner\Audio\C.mp3",
    "D#": "D:\Projects\Python\Harmonic Miner\Audio\C.mp3",
}


def playSound(bpm, note):
    for i in range(50):

        if note == "C":
            psnd.playsound(noteSounds["C"])
        print("Sound Played")
        root.after(bpm, playSound)
        i += 1


class Game:
    is_running = False

    enemies = np.array([])

    def __init__(self, is_running):
        self.isRunning = is_running


class Entity:
    def __init__(self, name, pos_X, pos_Y, health_points, sprite, note):
        self.name = name
        self.posX = pos_X
        self.posY = pos_Y
        self.health_points = health_points
        self.sprite = sprite
        self.note = note

    def printInfo(self):
        print(f"X pos: {self.posX} Y pos: {self.posY} note: {self.note}")


class Player(Entity):

    def __init__(self, name, pos_X, pos_Y, health_points, sprite, note):
        super().__init__(name, pos_X, pos_Y, health_points, sprite, note)


class Enemy(Entity):

    def __init__(self, name, pos_X, pos_Y, health_points, sprite, note):
        super().__init__(name, pos_X, pos_Y, health_points, sprite, note)
        Game.enemies = np.append(Game.enemies, name)

    def setPos(self):
        self.posX = random.randint(200, 300)
        self.posY = random.randint(100, 400)

    def setNote(self):
        self.note = random.choice(notes)


en = Enemy("Quarter", None, None, 50, None, None)
en.setNote()
en.setPos()
en.printInfo()

print(Game.enemies)
screen.create_oval(en.posX, en.posY, en.posX + 50, en.posY + 50, fill="green")
screen.update()

playSound(120, "C")
root.mainloop()
