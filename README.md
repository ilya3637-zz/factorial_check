url = https://qa-test.emcd.io/

| Test id | Description               | Input                                                           | Output                                                                  | Category | Importance | Last result | Comment                                                                                                                   |
|---------|---------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------|----------|------------|-------------|---------------------------------------------------------------------------------------------------------------------------|
| 1       | Check 0                   | 0                                                               | 1                                                                       | API      | Blocker    | OK          |                                                                                                                           |
| 2       | Check 1                   | 1                                                               | 1                                                                       | API      | Blocker    | OK          |                                                                                                                           |
| 3       | Check 9                   | 9                                                               | 362880                                                                  | API      | Blocker    | OK          |                                                                                                                           |
| 4       | Check 2147483647          | 2147483647                                                      | Inf                                                                     | API      | Medium     | Failed      | This value is included in int. Need either change the description, or return infinity, overflow, too large a number, etc. |
| 5       | Check -1                  | -1                                                              | invalid value                                                           | API      | Medium     | Failed      | This value is included in int, but not valid for factorial. Need to show user info about "-" value.                       |
| 6       | Check 0.2                 | 0.2                                                             | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 7       | Check 0,2                 | 0,2                                                             | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 8       | Check %s                  | %s                                                              | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 9       | Check %d                  | %d                                                              | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 10      | Check 00                  | 00                                                              | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 11      | Check empty string        | ""                                                              | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 12      | Check space               | " "                                                             | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 13      | Check \[1-9]              | \[1-9]                                                          | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 14      | Check text                | test                                                            | invalid value                                                           | API      | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 15      | Check input field         | find it, click on it, insert value ("12"), check entered value  | value is correct = 123                                                  | UI       | Blocker    | OK          |                                                                                                                           |
| 16      | Check button              | after test 15: enter same value in input field and press button | button pressed, "The factorial of 12 is: 479001600" showed under button | UI       | Blocker    | OK          |                                                                                                                           |
| 17      | Check result field not ok | after test 15: enter "test" in input field and press button     | button pressed, "invalid value/input" showed under button               | UI       | Medium     | Failed      | This value is not valid. Need to show user info about it.                                                                 |
| 18      | Check recalculate         | after test 15: enter "3" in input field and press button        | button pressed, "The factorial of 3 is: 6" showed under button          | UI       | Blocker    | OK          |                                                                                                                           |
| 19      | Check text in button      | read text from button                                           | text = "Calculate!"                                                     | UI       | Critical   | OK          |                                                                                                                           |
| 20      | Check text in input       | read text from input                                            | text = "Enter an integer"                                               | UI       | Medium     | OK          |                                                                                                                           |
