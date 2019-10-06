class Door(object):
    
    def __init__(self, name, width, height, color):
        self.name = name
        self.width = width
        self.height = height
        self.color = color
        self.status = 'closed'
        
    def open(self):
        print('Opening the {} door'.format(self.name))
        self.status = 'opened'
        
    def close(self):
        print('Closing the {} door'.format(self.name))
        self.status = 'closed'
        
    def get_status(self):
        print('Door {} has status {}'.format(self.name, self.status))
        
    def get_color(self):
        print(self.color)
        
classroom_door = Door('209', 70, 190, 'brown')
university_door = Door('univercity', 160, 190, 'white')
print(type(classroom_door))
classroom_door.open()
classroom_door.get_status()
classroom_door.close()
classroom_door.get_status()
university_door.get_status()
classroom_door.get_color()
print(classroom_door.__dict__)
