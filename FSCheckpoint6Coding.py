class Usuario:
  
  def __init__(self, name, password):
    self.name = name
    self.password = password


mike = Usuario("Mike Tyson", "123456")

print(f"name: {mike.name}; password: {mike.password}")

