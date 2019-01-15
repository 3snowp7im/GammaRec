# GammaRec

GammaRec is a video capture recording and preview utility. The main use case
is recording a feed from a capture device while compositing the source into
a stream layout using some other screen capture or streaming software such
as [OBS](https://obsproject.com).

![GammaRec Window](data/window.png)

GammaRec is written in Python and relies heavily on Gtk and Gstreamer. You
may need to install some prerequisites depending on your distribution:

```shell
$ sudo apt-get install gstreamer1.0-gtk3 python3 python3-pip
```

To get GammaRec, clone this repo using `git` and install using `pip3`:

```shell
$ git clone https://github.com/3snowp7im/GammaRec
$ cd GammaRec
$ pip3 install .
```

To run GammaRec, just launch the desktop entry, or run from command line:

```shell
$ gammarec
```
## Wayland

GammaRec supports Wayland via its fallback element, `gtksink`, however,
performance takes a hit. I recommend running on top of the Wayland X11
client instead:

```shell
GDK_DISPLAY=x11 gammarec
```
