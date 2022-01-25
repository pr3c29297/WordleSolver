Preparation:
1. Install Python https://www.python.org/downloads/
2. Download or clone the repo
3. Run the Solver by going to Command Line (Window) / Terminal (Mac), type: "cd " and the file path of the downloaded files
4. Type: "python3 Solver.py"

Run:
1. Guess a word on Wordle, get the initial result
2. Enter the correct guess, means incorrect character (gray / yellow), input the correct character (green) in capital letter
3. Enter the guess with characters that incorrect order, mean incorrect character or character that are correct (gray / green), input the character that appears but not in correct order with capital letters (yellow)
4. Enter all the incorrect character (gray)
5. The Solver will return you the list of possible answer based on the guess you made. Repeat to step 1 until you win!

Known limitation:
- Does not support the answer ends with plural form
- Some of the suggested answer may not be a valid word in Wordle, since it is not common
