# pip install pyscreenshot
import pyscreenshot as pys

screenshot = pys.grab()
screenshot.save("scrnshot.png")
screenshot.show()
