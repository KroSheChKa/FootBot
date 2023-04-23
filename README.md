# FootBot
## An automated bot that performs the role of a goalkeeper in mini-football

**The bot works in general using computer vision (OpenCV + mss libraries), and mouse movement emulation.**

**[Video](https://www.youtube.com/watch?v=akwmVh6k5aY&ab_channel=KroSheChKa) how FootBot ("fast" branch) works**

https://user-images.githubusercontent.com/104899233/232225652-76f9716a-ed4e-47fb-81b8-358fb6ec9a55.mp4

- If you want maximum performance of the bot, go to the **[fast](https://github.com/KroSheChKa/FootBot/tree/fast)** branch, if you want to observe the process for a while, go to the **[main](https://github.com/KroSheChKa/FootBot)**

### So the idea is

The [game](https://vk.com/app8013553) is built on the principle of ping-pong, where you have to hit the ball and hit all the bricks from above. Miss - lose.

*The game is constructed in such a way that from the PC version the control of the brick that kicks the ball is done by just moving the cursor. (The brick follows the cursor)*

**1. Get the most possible coordinates of the ball. And VERY quickly, because with each new level the ball accelerates faster and faster.**

>So I had to use the mss library, because it is faster than the libraries I know, such as PIL, pyautogui.

 >More screenshots per second == more fps == the chance of missing the ball is reducing

**2. Set the cursor on these coordinates, but the y coordinate is stable. There is no need to change it.**

>Actually, I did a confidence threshold to calm down a cursor a little bit while a ball is away, but it had a bad influence on detecting the ball. Even with a little threshold.

and thats it.

----
### Total optimization

**I made as much effort to optimize the bot as possible. The next stage of optimization goes beyond Python to C++**

I implemented some optimization features:
- I made a small optimization, by limiting the cursor area. Why is this necessary? In a game there can be a case where the ball hits the corner of the soccer field, and the cursor, not keeping up with the ball (about this later), pinches it in the corner. The ball comes out of such a position with the least resistance - in the goal. Therefore, the cursor is limited so that it does not jam the ball, but also would not let the ball into the goal at any angle.

```python
win32api.ClipCursor((width start,height start,width end,height end))
```
- A new optimization [feature](https://github.com/KroSheChKa/FootBot/commit/92d9ba6f254b7bf6952f8debc7283942045523f6) has been added. The reason for creating it was the fact that the ball could kind of "slide" off the edge of the brick and hit the goal. Since the brick should ideally only travel along the goal to kick the ball (or maybe it's all over the field), I came up with a solution:
```python
x = round((x_old - goal_center) * 0.7) + goal_center
```
>Shrink the entire visible field for the bot to the size of the goal. Multiply the difference between the center of the goal and the X coordinate of the ball by coefficient and add to the center of the goal. In my case, the coefficient is 0.7.

    Now the bot hardly ever faces the problem that the ball is ahead of him.
    
----
### A technical problem with the ~~bot~~ game

There was a whole paragraph here, which dealt with the problem with the bot. But they've already been fixed, and the rest are left to the game itself. The game doesn't have time to process the inputs, I think. It turns out that the game counts defeat when I actually kicked the ball

----

## How to run

As I said in my previous bot project [here](https://github.com/KroSheChKa/BasketBot/blob/main/README.md#how-to-use) that there is a huge attachment to certain coordinates on the screen. I use a 3440x1440 monitor and place the game window in a certain place. Based on this it should be understood that it's close to impossible to know the exact situation of the user to run the bot with one button :(

**So in the case of self-launching, the user should configure everything manually for his working surroundings ([help](https://github.com/KroSheChKa/BasketBot/blob/main/README.md#how-to-use)).**

----

>Also there are some in-game bugs and the bot may lose due to it

*Any suggestions? You found a bug?*

-> Leave a comment
