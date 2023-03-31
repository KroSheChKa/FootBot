# FootBot
## An automated bot that performs the role of a goalkeeper in mini-football

**The bot works in general using computer vision (OpenCV + mss libraries), and mouse movement emulation.**

The [game](https://vk.com/app8013553) is built on the principle of ping-pong, where you have to hit the ball and hit all the bricks from above. Miss - lose.

*The game is constructed in such a way that from the PC version the control of the brick that kicks the ball is done by just moving the cursor. (The brick follows the cursor)*

### So the idea is

**1. Get the most possible coordinates of the ball. And VERY quickly, because with each new level the ball accelerates faster and faster.**

>So I had to use the mss library, because it is faster than the libraries I know, such as PIL, pyautogui.

 >More screenshots per second == more fps == the chance of missing the ball is reducing

**2. Set the cursor on these coordinates, but the y coordinate is stable. There is no need to change it.**

>Actually, I did a confidence threshold to calm down a cursor a little bit while a ball is away, but it had a bad influence on detecting the ball. Even with a little threshold.

and thats it.

----
### A small optimization

I made a small optimization, by limiting the cursor area. Why is this necessary? In a game there can be a case where the ball hits the corner of the soccer field, and the cursor, not keeping up with the ball (about this later), pinches it in the corner. The ball comes out of such a position with the least resistance - in the goal. Therefore, the cursor is limited so that it does not jam the ball, but also would not let the ball into the goal at any angle.

```python
win32api.ClipCursor((width start,height start,width end,height end))
```
----
### A technical problem with the bot

    As I mentioned earlier, more fps means less chance of missing the ball.

**Even though the mss library does this at a rate of approximately 25 frames, there are cases where the cursor does not keep up with the ball. Let's look at the loop in details**

1. Screenshot of the selected area (and the area is deliberately not large, to have more fps)

2. Running through the original picture of the ball looking for the highest match

3. Moving the cursor to the central coordinates (y does not change, it is not necessary)

*That's it. This is the most simplified variant of the bot, but even so he manages to not keep up with the ball at high speeds.*

>Yes, there are small inaccuracies in determining the center of the ball, but they are at the level of inaccuracy and do not lead to this problem.

**I have two guesses. Either you need MORE fps(1), or the time it takes to send coordinate data is too long to keep up with the speed of the ball(2).**

1. Gotta find something faster than mss. Or rewrite it in C++, but OpenCV library is already written in C and I work with win32 library that is quiet close to OS and hardware.

2. So in one frame the ball is at (x, y) coordinates, and when the cursor movement function has already received and is processing the data, the ball has already moved to (x + n, y + m). Where n and m can already be quite an impressive number so that the cursor does not keep up with the ball and misses the goal.

        It is like we are following the shadow of the ball
    **We need to take the coordinates in the 2 neighboring frames and calculate the estimated next movement to expect the ball faster when it has not yet appeared there.**

    *But in this case we lose calculation time.*

----

## How to run

As I said in my previous bot project [here](https://github.com/KroSheChKa/BasketBot/blob/main/README.md#how-to-use) that there is a huge attachment to certain coordinates on the screen. I use a 3440x1440 monitor and place the game window in a certain place. Based on this it should be understood that it's close to impossible to know the exact situation of the user to run the bot with one button :(

**So in the case of self-launching, the user should configure everything manually for his working surroundings.**

----

>Also there are some in-game bugs and the bot may lose due to it

*Any suggestions? You found a bug?*

-> Leave a comment

**I WILL ADD A VIDEO HOW THE BOT WORKS. ALSO TO MY PREVIOUS BOT**