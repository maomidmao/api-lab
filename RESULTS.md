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
- Step A4, status codes when the other user reads, changes and deletes: Read: 404; update: 400; delete: 400.
## Part B
1. API tests can find failures in communication between the client and the real server, and problems in how the server code works with stored data. A unit test with stubs does not exercise those real connections. Unit tests are still useful because they can test one piece of logic quickly and independently, including cases that are hard to reproduce on a live server.

2. Each test creates a user with a new name so its ratings belong to that user and do not interfere with other students' data or tests. The public token can refer to shared data. In Project 2, I would create and use my group's own test data in the shop or hotel, and only change or delete data that our tests created.

3. A session keeps cookies between requests. QuickPizza's load balancer uses the cookie to direct requests to the same server, where the new user was created. Without a session, a later request may reach a different server. In my three runs without a session, user creation succeeded but login returned 401 each time; a different server is a likely explanation, although the output alone does not prove which server handled each request.

4. Excluding all three tools revealed the defect. A 500 response with an empty body indicates a server error and gives the calling app no useful explanation. A 400 with a message tells the app that the request cannot be satisfied. The test remains marked xfail so the defect stays visible; strict=True flags it if the expected behavior starts working.

5. Base choice coverage needs 9 cases: one base case plus 2, 3, 1, and 2 non-base blocks for C1, C2, C3, and C4: 1 + 2 + 3 + 1 + 2 = 9. All combinations would need 3 × 4 × 2 × 3 = 72 cases.

6. The other user's read returned 404, update returned 400, and delete returned 400. I would expect each request to be refused with a 4xx status, such as 403 Forbidden or 404 Not Found. A 404 can avoid revealing whether a rating exists. The 400 responses are less specific than 403 or 404, but the lab accepts any 4xx response, so these results alone do not establish a defect. The owner's follow-up reads showed the rating was unchanged.

7. A GET request to /api/ratings with the made-up token `0000000000000000` returned 200 and a JSON list of ratings. Accepting an arbitrary token as authentication is a security defect if access is meant to require a valid login. On a real system, a stranger might use this weakness to read data they are not authorized to see. I only tested reading; this result does not show whether the token can change data.

8. An API test can directly check status codes and JSON fields, including error responses. A web-page test can check what a person sees and interacts with, such as whether an error message is visible and a button works in the browser.
