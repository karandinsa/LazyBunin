from tkinter import *

window_caption = "Понималка"
show_text = """ Что-то сообщить сотруднику,
 подождать 60 секунд и закрыть окно. 
 Если текст не влезает в окошко, изменить window_geomery.
"""
delay_for_close = 60
window_geometry = "400x150"

root = Tk()
root.title(window_caption)
root.geometry(window_geometry)
exit_button = Button(root, text="Поняла!", command=root.destroy)
tt = Label(root, text=show_text)
tt.pack()
exit_button.pack(pady=20)
root.after(delay_for_close*1000, lambda:root.destroy())
root.call('wm', 'attributes', '.', '-topmost', True)
root.mainloop()
