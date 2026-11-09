# Another user cannot read a rating, and the owner's rating stays unchanged.
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.get(path, headers=other_auth)
    print("Other user read status:", res.status_code)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user cannot change a rating, and the owner's rating stays unchanged.
def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.put(path, json={"stars": 4}, headers=other_auth)
    print("Other user update status:", res.status_code)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user cannot delete a rating, and the owner can still read it.
def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.delete(path, headers=other_auth)
    print("Other user delete status:", res.status_code)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating
