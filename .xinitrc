
xset +fp $HOME/.fonts
xset fp rehash
xrdb -merge $HOME/.Xresources

#wallpaper desktop
$HOME/.fehbg &

#status bar panel
$HOME/.bin/statusbar &

#window X11 dwm suckless
exec dwm
