import uuid


# A username that is already taken cannot be used again.
def test_duplicate_username_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}

    # Create the first user.
    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    # Try to create another user with the same name.
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}


# A user cannot log in with the wrong password.
def test_wrong_password_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}

    # Create the user with the correct password.
    res = api.post("/api/users", json=user)
    assert res.status_code == 201

    # Try to log in with a different password.
    wrong_user = {"username": name, "password": "Wrong-Password"}
    res = api.post("/api/users/token/login", json=wrong_user)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# A user cannot be created with an empty username.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}

    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}