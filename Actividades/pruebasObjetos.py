class Student:

    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def set_marks(self, marks):
        self._marks = marks
    def get_marks(self):
        return self._marks
    
    def display(self):
        print('Name:', self.get_name())
        print('Marks:', self.get_marks())

