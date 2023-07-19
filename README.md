# FootBot
## An automated bot that performs the role of a goalkeeper in mini-football

**The bot works in general using computer vision (OpenCV + mss libraries), and mouse movement emulation.**

**[Video](https://www.youtube.com/watch?v=akwmVh6k5aY&ab_channel=KroSheChKa) how `FootBot_fast` works**

https://user-images.githubusercontent.com/104899233/232225652-76f9716a-ed4e-47fb-81b8-358fb6ec9a55.mp4

- If you want `maximum performance` of the bot launch `FootBot_fast`, if you want to **observe the process** and **modify the values** for a while launch `FootBot`

### So the idea is

The [game](https://vk.com/app8013553) is built on the principle of ping-pong, where you have to hit the ball and hit all the bricks from above. Miss - lose.

*The game is constructed in such a way, that from the PC version the control of the brick that kicks the ball is done by just moving the cursor. (The brick follows the cursor)*

**1. Get the most possible coordinates of the ball. And VERY quickly, because with each new level the ball accelerates faster and faster.**

>So I had to use the `mss library`, because it is faster than the libraries I know, such as PIL, pyautogui.

 >More screenshots per second == more fps == the chance of missing the ball is reducing

**2. Set the cursor on these coordinates, but the y coordinate is `stable`. There is no need to change it.**

>Actually, I did a confidence threshold to calm down a cursor a little bit while a ball is away, but it had a bad influence on detecting the ball. Even with a little threshold.

some features and thats it.

----
### Total optimization

**I made as much effort to optimize the bot as possible. The next stage of optimization goes beyond Python to `C++`**

I implemented some optimization features:
- I made a small optimization, by `limiting the cursor area`. Why is this necessary? In a game there can be a case where the ball hits the corner of the soccer field, and the cursor, not keeping up with the ball (about this later), pinches it in the corner. The ball comes out of such a position with the least resistance - **in the goal**. Therefore, the `cursor is limited` so that it does not jam the ball, but also would not let the ball into the goal at any angle.

```python
win32api.ClipCursor((width start,height start,width end,height end))
```
- A new optimization [feature](https://github.com/KroSheChKa/FootBot/commit/92d9ba6f254b7bf6952f8debc7283942045523f6) has been added. The reason for creating it was the fact that the ball could kind of "slide" off the edge of the brick and hit the goal. Since the brick should ideally only travel along the goal to kick the ball (or maybe it's all over the field). I came up with a solution:
```python
x = round((x_old - goal_center) * 0.7) + goal_center
```
>Shrink the entire visible field for the bot to the size of the goal. Multiply the difference between the center of the goal and the X coordinate of the ball by `coefficient` and add to the center of the goal. In my case, the coefficient is 0.7.

    Now the bot hardly ever faces the problem that the ball is ahead of him.
    
----
### A technical problem with the ~~bot~~ game

There was a whole paragraph here, which dealt with the problem with the bot. But they've already been fixed, and the rest are left in the game itself. The game doesn't have time to `process the inputs`, I think. It turns out that the game counts defeat when I actually kicked the ball. Also there are some in-game cases that highly accelerated ball might just go through the wall and cause a loss :(

----

## How to run

This bot has an enormous attachment to `certain coordinates` on the screen and to the screen resolution itself. Actually in the new commit on 13.07.2023 I added a solution that should help.

All you have to to is:

- Install [python](https://www.python.org/downloads/) together with `IDLE` on your computer **(you should run the code via IDLE!)**
- Clone this project by this command somewhere on your computer:
> **Make sure you have downloaded [git](https://git-scm.com/downloads)!**
```
git clone https://github.com/KroSheChKa/FootBot.git
```
- Open cmd in the created folder or press RButton in the folder and click "`Git Bash Here`" and paste that:
```
pip install -r requirements.txt
```

**Particular case:** *If you have a monitor 3440x1440, then simply place the window with the game exactly half the screen on the left, set the **window scale 150%** and run it.*

In other cases to run this code on your computer you will have to `change values` depending on the resolution of your monitor, such as:
```python 
# Football field (game area)
field = {'left': 747,
         'top': 990,
         'width': 462,
         'height': 200}
```
![image](https://github.com/KroSheChKa/FootBot/assets/104899233/c6a186a9-f941-494f-a93a-da001182656c)
> The corners of the rectangle are the `coordinates of your screen` relative to the left edge of the screen and the top edge of the screen
```python
# Limiting the cursor movement area btw soccer goalposts
from_left, cursor_area = 870, 214
...
from_top = 1160
```
![image](https://github.com/KroSheChKa/FootBot/assets/104899233/35daa60c-fd5e-4a60-be77-3563bc3d968c)
> Limit cursor area to make bot more effective

You can also play with the ball detection threshold to make the detection valid
```python
ball_threshold = 0.251
```

- It is necessary to have an account in a popular CIS social network [VK.com](https://vk.com)
  
- Then go into the [Game](https://vk.com/app6657931)
  
- Make sure the game window is on the top. You will have a moment to remove the `IDLE Shell` from game area.

And that's it.
>I hope my detailed comments in the code will help you

----

>There are some in-game bugs and the bot may lose due to it

*Any suggestions? You found a bug?*

-> Leave a comment in [Discussions](https://github.com/KroSheChKa/BasketBot/discussions)
