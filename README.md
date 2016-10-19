# 12_image_resize

###Prerequisites:

Run in console `pip install -r requirements.txt` to install 3rd party modules.

---

Simple command line image resizer. Acceptable format is JPG or PNG.

Script takes one required and several optional parameters:

- `original_path` - can be short (name of image in same folder) or full (`C:/my_folder/img.jpg`);
- `--width` - int;
- `--height` - int;
- `--scale` - float;
- `--output` - place where to save image. If not given - will save in the same folder of input image.

```
!Note that: if `--scale` is given you cannot add `--height` or `--width`.
```


> Вытащи работу с изображением из ifmain в отдельную функцию.
Вытащил, молодец. Вот только стало хуже. load_image, внезапно, выводит что-то в консоль?! Да еще прерывает работу программы?!!
Реорганизуй код еще раз. Только в этот раз подумай как сделать правильно.

> def resize_image(image, **params):
Как мне теперь выяснить что подавать на вход функции без вычитывания её кода? Не делай так.

