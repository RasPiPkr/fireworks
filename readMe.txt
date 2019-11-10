If you want to stop / quit at any time press "q" to quit scipt. I have not included personal pictures I used but
have included an example picture. All pictures used don't get destroyed as they are only loaded and
a temporary picture (current.png) is created and that's what exploded, BOOM!.

Check through the code and adjust accordingly how many fireworks, screen size etc.

*** HOW TO USE ***
For licensing reasons I have not included any sounds but you can get some free sounds to use
online very easily by searching, downloading and saving into this folder with appropiate filenames.

If no sounds are found it will run but in silent mode.

WOOSHING SOUNDS:
The script also looks for sounds named with Woosh.wav in the title so save your variations with the
filename ending with "Woosh.wav" (example: firework2Woosh.wav).

BANGING SOUNDS:
The script looks for sounds named with Bang.wav in the title so save your variations with the
filename ending with "Bang.wav" (example: big1Bang.wav).

PICTURES:
The script also looks for pictures named with 100.png in the title so save your variations with the
filename ending with "100.png" (example: 21stBirthday100.png). Pictures used are better if they have
no border, if that's the case then crop the picture or edit it so unwanted parts are transparent.

SET PICTURE DISPLAY / FINALE
You can have a set order by adding the filename in the list finale and set the order in the
kaBoom function and make sure your stopDisplay variable amount matches your display / finale amount.
Rounded pictures will be best but I'll leave that up to you.

This was designed by myself to take pictures in the current folder and show them in the
firework display but for using on a Raspberry Pi I would suggest resizing your picture to
100x100 as I did to improve the animation. This python script does resize the pictures in the
code but as it reloads the picture per firework its a little easier on the Pi. If your using
another device then you could try bigger pictures.

The pictures I've included are 100 pixels in width by 100 pixels in height circles and are
transparent outside of the circle.