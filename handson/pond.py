# stones, ground, pond, person

class Pond:
    def generate_ripple(stone):
        pass

class Person:
    def throw(self, stone):
        stone.velocity = 20
        stone.angle = 45
        return stone

    def pick(self, stones):
        return random.choice(stones);

class Stone:
    size = 10
    color = "black"
    velocity = 0
    def hit(self):
        pass

# Process of making a composite object is called composition
class Ground: # Composite Object
    stones = [Stone() for i in range(25)]
    pond = Pond()
    person = Person()

ground = Ground()
picked_stone = ground.person.pick(ground.stones)
thrown_stone = ground.person.throw(picked_stone)
ground.pond.generate_ripple(thrown_stone)
