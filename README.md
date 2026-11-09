# api-lab

## Input domain model: create a rating

`POST /api/ratings` takes a pizza ID and stars in the request body, and an authorization token in the header. The base choices represent a normal valid request.

| Characteristic | Block | Example value | Test |
| --- | --- | --- | --- |
| C1: Value of stars | Below 1 | `0` | `test_stars_out_of_range` |
| C1: Value of stars | 1 to 5 (base) | `3` | `test_base_choice_is_saved` |
| C1: Value of stars | Above 5 | `6` | `test_stars_out_of_range` |
| C2: Type of stars | Whole number (base) | `3` | `test_base_choice_is_saved` |
| C2: Type of stars | Decimal | `3.5` | `test_invalid_stars_type_is_refused` |
| C2: Type of stars | Text | `"3"` | `test_invalid_stars_type_is_refused` |
| C2: Type of stars | Missing | No `stars` field | `test_missing_stars_is_refused` |
| C3: Pizza | Exists (base) | A new pizza | `test_base_choice_is_saved` |
| C3: Pizza | Does not exist | `999999999` | `test_nonexistent_pizza_is_refused` |
| C4: Token | User's own (base) | Token from `auth` | `test_base_choice_is_saved` |
| C4: Token | None | No header | `test_missing_token_is_refused` |
| C4: Token | Wrong length | `token short` | `test_short_token_is_refused` |
