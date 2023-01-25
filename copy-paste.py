'''
The challenge is to analyse these strings for any instances of [CTRL+C] and [CTRL+V]. When [CTRL+C] is encountered, 
the contents of the string before it should be 'copied' to a clipboard. Upon any instance of [CTRL+V] in the string, 
this clipboard should be pasted in its place. If [CTRL+V] is encountered before any corresponding [CTRL+C] then 
it should simply paste nothing.

Rewards:
:five:  Points are awarded for a working algorithm as described above
:three:  Further points are awarded for supporting [CTRL+X], which should remove the preceding text before copying it to the clipboard
:two:  Further points are awarded for validating your solution with a collection of unit tests
Example:
For this example input:
challenge("the first[CTRL+C] Coding Challenge was [CTRL+V] string manipulation task")
Your solution might output:
"the first Coding Challenge was the first string manipulation task"
Submission:
When you have a solution, submit a link to your source code repo using the /submit command here on Slack. Please include any code and data required in order to test your solution easily. Submission closes 1st February, 17:00
Good luck good luck good luck good luck (edited)

output:
"the big red fox jumps over the big red lazy dog.",
"the tall oak tree towers over the lush green meadow.",
"the sun shines down on the sun shines down the busy the sun shines down on the sun shines down.",
"[CTRL+V]the tall oak tree towers over the lush green meadow.",
"a majestic lion[CTRL+C] searches for [CTRL+V] in the tall grass.",
"the shimmering star[CTRL+X]Twinkling in the dark, [CTRL+V] shines bright.",
"[CTRL+X]a fluffy white cloud drifts [CTRL+V][CTRL+C] across the sky, [CTRL+V]",

'''

str_lst=[
  "the big red[CTRL+C] fox jumps over [CTRL+V] lazy dog.",
  "[CTRL+V]the tall oak tree towers over the lush green meadow.",
  "the sun shines down[CTRL+C] on [CTRL+V][CTRL+C] the busy [CTRL+V].",
  "[CTRL+V]the tall oak tree towers over the lush green meadow.",
  "a majestic lion[CTRL+C] searches for [CTRL+V] in the tall grass.",
  "the shimmering star[CTRL+X]Twinkling in the dark, [CTRL+V] shines bright.",
  "[CTRL+X]a fluffy white cloud drifts [CTRL+V][CTRL+C] across the sky, [CTRL+V]",
]



for k in str_lst:
    if '[CTRL+C]' not in k:
        post_text = k.replace('[CTRL+V]','')
    else:
        pre_text = k.split('[CTRL+C]')[0]
        if pre_text!='':
            post_text = k.replace('[CTRL+V]',pre_text).replace('[CTRL+C]','')
        else:
            post_text = k.replace('[CTRL+V]','')
    print(post_text)
            