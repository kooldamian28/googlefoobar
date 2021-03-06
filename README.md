# googlefoobar
Google Foobar Challenge Solutions(foobar.withgoogle.com)

This repo is also available at <a href="kooldamian28.github.io/googlefoobarr">https://kooldamian28.github.io/googlefoobar</a>. You can bookmark <a href="https://kooldamian28.github.io/googlefoobar">this page</a> for easy access.

Here are all the Google Foobar challenges that I had completed.

Thank you!

1.Braille Translation
=

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and - since you'll be promoting efficiency at the same time - increase your chances of a promotion.

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and ""read"" the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order: 1 4 2 5 3 6

So given the plain text word ""code"", you get the Braille dots:

11 10 11 10 00 01 01 01 00 10 00 00

where 1 represents a bump and 0 represents no bump. Put together, ""code"" becomes the output string ""100100101010100110100010"".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

Languages
To provide a Python solution, edit solution.py To provide a Java solution, edit Solution.java

Test cases
Your code should pass the following test cases. Note that it may also be run against hidden test cases not shown here.

-- Python cases -- Input: solution.solution("code") Output: 100100101010100110100010

Input: solution.solution("Braille") Output: 000001110000111010100000010100111000111000100010

Input: solution.solution("The quick brown fox jumps over the lazy dog") Output: 000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

-- Java cases -- Input: Solution.solution("code") Output: 100100101010100110100010

Input: Solution.solution("Braille") Output: 000001110000111010100000010100111000111000100010

Input: Solution.solution("The quick brown fox jumps over the lazy dog") Output: 000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

To download the solution:
<a href="https://cdn.jsdelivr.net/gh/kooldamian28/googlefoobar/brailletranslation/solution.py">https://cdn.jsdelivr.net/gh/kooldamian28/googlefoobar/brailletranslation/solution.py</a>

2.Prison Labor Dodgers
=
Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up. You've been given the task of fixing them, but after you wrote up new shifts, you realized that some prisoners had been transferred to a different block and aren't available for their assigned shifts. And manually sorting through each shift list to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!

Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, write a function solution(x, y) that compares the lists and returns the additional ID.

For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function solution(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't. Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function solution(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.

In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99, and one of the lists will contain an additional unique integer which should be returned by the function.  The same n non-unique integers will be present on both lists, but they might appear in a different order, like in the examples above. Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.

Languages:

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases:

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([13, 5, 6, 2, 5], [5, 2, 5, 13])
Output:
    6

Input:
solution.solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])
Output:
    -4

-- Java cases --
Input:
Solution.solution({13, 5, 6, 2, 5}, {5, 2, 5, 13})
Output:
    6

Input:
Solution.solution({14, 27, 1, 4, 2, 50, 3, 1}, {2, 4, -4, 3, 1, 1, 14, 27, 50})
Output:
    -4

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

Submitting solution...

You survived a week in Commander Lambda's organization, and you even managed to get yourself promoted. Hooray! Henchmen still don't have the kind of security access you'll need to take down Commander Lambda, though, so you'd better keep working. Chop chop!

Submission: SUCCESSFUL. Completed in: 5 mins, 1 secs.

To download the solution: <a href="https://cdn.jsdelivr.net/gh/kooldamian28/googlefoobar/prisonlabordodgers/solution.py">https://cdn.jsdelivr.net/gh/kooldamian28/googlefoobar/prisonlabordodgers/solution.py</a>

3.Gearing Up for Destruction
=
As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple - just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

Languages:

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases:

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({4, 17, 50})
Output:
    -1,-1

Input:
Solution.solution({4, 30, 50})
Output:
    12,1

-- Python cases --
Input:
solution.solution([4, 30, 50])
Output:
    12,1

Input:
solution.solution([4, 17, 50])
Output:
    -1,-1

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

Submitting solution...
Submission: SUCCESSFUL. Completed in: 15 mins, 4 secs.

To download the solution: <a href="https://cdn.jsdelivr.net/gh/kooldamian28/googlefoobar/gearingupfordestruction/solution.py">https://cdn.jsdelivr.net/gh/kooldamian28/googlefoobar/gearingupfordestruction/solution.py</a>

Solar Doomsday
==============
Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor core with solar arrays, and she's tasked you with setting up the solar panels. 
Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into three 1x1 square solar panels.
Write a function answer(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, answer(12) would return [9, 1, 1, 1].

To download the solution: <a href="https://cdn.jsdelivr.net/gh/kooldamian28/googlefoobar/solardoomsday/solution.py">https://cdn.jsdelivr.net/gh/kooldamian28/googlefoobar/solardoomsday/solution.py</a>

Note:
=
If you're here still, you can trigger the Google Foobar by searching for "c++ move semantics" and going to Page 2 of results, then reloading 2-8 times, don't reload fast because it takes 4-5 seconds for the animation to appear.
If it doesn't work search for, in order, "mutex lock" and "arraylist java", in both the searches go to second page of search results and reload 2 times, then again search for "c++ move semantics" and go to the second page of search results, then wait for 3-4 seconds, if it doesn't appear, reload 2-8 times each at a interval of 4 seconds.
If it still doesn't work, this guide may be outdated because I'm writing it at 01/08/2020 at 3:07 PM (IST).
Thank you! (and pray for me and I will too!)

This work is licensed under the <a href="https://www.gnu.org/licenses/agpl-3.0.html">GNU Affero General Public License v3.0</a>
