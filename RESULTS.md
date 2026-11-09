# API lab results
## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Hot Marinara
- Step 0.12, results of the three runs without a session (optional): All three failed. User creation returned 201, but login returned 401 instead of the expected 200.
- Step 0.16, blocks of "how many of the three tools are excluded": 0, 1, 2, or 3 tools.
## Defect report
- Title: Excluding all pizza tools causes a server error.
- Request: POST /api/pizza with `{"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}`.
- Expected result: 400 Bad Request with a JSON error message.
- Actual result: 500 Internal Server Error with an empty body.
- Severity: Medium, because this request fails but other requests can still work.
## Part A
- Step A4, status codes when the other user reads, changes and deletes:
## Part B
1.
2.
3.
4.
5.
6.
7.
8.
