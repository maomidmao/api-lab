# api-lab

## Input domain model: create a rating

`POST /api/ratings` takes a pizza ID and stars in the request body, and an authorization token in the header. The base choices represent a normal valid request.

| Characteristic | Blocks | Values in the tests |
| --- | --- | --- |
| C1: Value of stars | Below 1; 1 to 5 (base); above 5 | `0`, `3`, `6` |
| C2: Type of stars | Whole number (base); decimal; text; missing | `3`, `3.5`, `"3"`, no `stars` field |
| C3: Pizza | Exists (base); does not exist | A new pizza; `999999999` |
| C4: Token | User's own (base); none; wrong length | Token from `auth`; no header; `token short` |
