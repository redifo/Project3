| Feature                    | Expected Outcome                                                  | Testing Performed                                  | Result                                  | Pass/Fail |
|----------------------------|-------------------------------------------------------------------|----------------------------------------------------|-----------------------------------------|-----------|
| Game Initialization        | Game initializes with a welcome message and name prompt           | Started the game                                   | Welcome message and name prompt appear  | Pass      |
| Player Name Validation     | Reject names under 3 characters and prompt for re-entry           | Entered various name lengths                       | Incorrect names rejected, correct prompt | Pass      |
| Difficulty Selection       | Allows selection of difficulty and sets guess limit               | Selected each difficulty level                     | Correct guess limit set for each level   | Pass      |
| Word Guessing              | Accepts valid 5-letter words and provides feedback                 | Entered various valid and invalid words            | Valid words accepted, feedback provided  | Pass      |
| Guess Limit Functionality  | Game ends after reaching max guesses for difficulty               | Guessed until reaching the limit                   | Game ended after max guesses             | Pass      |
| High Score Functionality   | Records and displays high scores correctly                        | Completed games and checked high score list        | High scores recorded and displayed       | Pass      |
| Game Restart               | Option to play again or return to main menu after game ends       | Selected options after game completion             | Correct navigation after game            | Pass      |
| Input Error Handling       | Display error for invalid inputs and allows correction            | Entered invalid inputs and corrected               | Error displayed, correction allowed      | Pass      |
| Data Persistence           | Scores and words persist across sessions                          | Restarted game, checked scores and word list       | Data persisted correctly                 | Pass      |
| User Interface Consistency | UI elements consistent and responsive throughout gameplay         | Interacted with various UI elements                | UI consistent and responsive             | Pass      |


Initial results from pep8 checker:
21: W605 invalid escape sequence '\ '
21: W605 invalid escape sequence '\ '
22: W605 invalid escape sequence '\ '
22: W605 invalid escape sequence '\ '
22: W605 invalid escape sequence '\ '
22: W605 invalid escape sequence '\ '
22: W605 invalid escape sequence '\ '
23: W605 invalid escape sequence '\ '
24: W605 invalid escape sequence '\_'
24: W605 invalid escape sequence '\_'
24: W605 invalid escape sequence '\_'
24: W605 invalid escape sequence '\_'
24: W605 invalid escape sequence '\_'
84: E501 line too long (88 > 79 characters)
86: W291 trailing whitespace
88: W291 trailing whitespace
90: W293 blank line contains whitespace
95: E501 line too long (94 > 79 characters)
95: W291 trailing whitespace
96: W293 blank line contains whitespace
99: E231 missing whitespace after ','
99: E231 missing whitespace after ','
99: E501 line too long (112 > 79 characters)
99: E231 missing whitespace after ','
100: E501 line too long (139 > 79 characters)
105: E501 line too long (121 > 79 characters)
110: E501 line too long (81 > 79 characters)
113: E501 line too long (97 > 79 characters)
115: E225 missing whitespace around operator
118: E225 missing whitespace around operator
119: E225 missing whitespace around operator
124: W293 blank line contains whitespace
126: E303 too many blank lines (2)
128: W291 trailing whitespace
135: W293 blank line contains whitespace
138: W293 blank line contains whitespace
145: W293 blank line contains whitespace
146: W293 blank line contains whitespace
147: E303 too many blank lines (2)
149: W291 trailing whitespace
156: E501 line too long (139 > 79 characters)
158: W293 blank line contains whitespace
166: E501 line too long (127 > 79 characters)
167: E501 line too long (116 > 79 characters)
168: E501 line too long (144 > 79 characters)
169: E501 line too long (122 > 79 characters)
170: E501 line too long (188 > 79 characters)
171: E501 line too long (110 > 79 characters)
188: E501 line too long (112 > 79 characters)
191: E501 line too long (113 > 79 characters)
194: E501 line too long (111 > 79 characters)
208: W293 blank line contains whitespace
213: E501 line too long (97 > 79 characters)
216: E261 at least two spaces before inline comment
216: E262 inline comment should start with '# '
221: E225 missing whitespace around operator
229: E501 line too long (106 > 79 characters)
230: W293 blank line contains whitespace
231: W293 blank line contains whitespace
232: E303 too many blank lines (2)
238: W293 blank line contains whitespace
242: E501 line too long (126 > 79 characters)
253: W293 blank line contains whitespace
254: E302 expected 2 blank lines, found 1
262: W291 trailing whitespace
263: E501 line too long (184 > 79 characters)
269: W293 blank line contains whitespace
270: E302 expected 2 blank lines, found 1
274: E265 block comment should start with '# '
276: E265 block comment should start with '# '
276: E501 line too long (83 > 79 characters)
277: E225 missing whitespace around operator
279: W293 blank line contains whitespace
282: E225 missing whitespace around operator
283: W293 blank line contains whitespace
284: E225 missing whitespace around operator
284: E261 at least two spaces before inline comment
287: W293 blank line contains whitespace
292: W293 blank line contains whitespace
297: W293 blank line contains whitespace
302: E305 expected 2 blank lines after class or function definition, found 1
303: W292 no newline at end of file