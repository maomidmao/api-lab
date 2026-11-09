import pytest


# Valid boundary values are saved; invalid updates leave the rating unchanged.
@pytest.mark.parametrize(
    "stars, expected_status, expected_saved_stars",
    [
        (0, 400, 3),
        (1, 200, 1),
        (5, 200, 5),
        (6, 400, 3),
    ],
)
def test_update_stars_boundaries(
    api, auth, rating, stars, expected_status, expected_saved_stars
):
    path = f"/api/ratings/{rating['id']}"

    # Try to update the rating.
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status

    # Read it back to see what was actually saved.
    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json()["stars"] == expected_saved_stars