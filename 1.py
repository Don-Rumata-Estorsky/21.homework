"""
есть главный класс и он может присваивать поля,
 через конструктор, и есть младший потомок класс, он с числовым полем, через полиморфизм
"""

class ClassClassov:
  def __init__(self, text):
    self.text = text

  def set_text(self, new_text=""):
    self.text = new_text

  def get_text(self):
    return self.text

class lilClass(ClassClassov):
  def __init__(self, text, number):
    super().__init__(text)  
    self.number = number

  def set_number(self, new_number):
    self.number = new_number

  def get_number(self):
    return self.number

classclassov= ClassClassov("привет")
print("")
print("Текст главного: " + classclassov.get_text())

classclassov.set_text("пока")
print("Текст главного: " + classclassov.get_text())
print("")

lilclass = lilClass("Здасьте", "111")
print("Текст малого класса: " + lilclass.get_text())
print("Число малого класса: " + lilclass.get_number())
print("")

lilclass.set_text("Досвидания")
lilclass.set_number("222")
print("Текст малого класса после изменения: " + lilclass.get_text())
print("Число малого класса после изменения: " + lilclass.get_number())
print("")