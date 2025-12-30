For now let's have all the key elements of the gameplay working and then we'll get to polishing it and adding extra features.

# Features
  - Moving entities
  - Class for levels (rename current `Level` class to GameField or sth like that)

# Refactors
  - Polymorphic stuff in fields could be nicer (like everything could inherit the \_\_str\_\_ method)
  - I don't like how level cells are represented and it would be cool to access them like `cells.x.y` rather than `cells[y][x]`
  - Use Surface.scroll instead of pos.update to move stuff?
