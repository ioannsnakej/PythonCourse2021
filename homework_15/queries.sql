CREATE TABLE users
(
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) UNIQUE,
    email VARCHAR(80) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE posts
(
    id INT NOT NULL AUTO_INCREMENT,
    body TEXT DEFAULT '',
    user_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT INTO users (username, email)
VALUES
    ('Ivan', 'ivan@example.com'),
    ('Sofia', 'sofia@example.com');

INSERT INTO posts (body, user_id)
VALUES
    ('Привет', 1),
    ('Привет', 2),
    ('Кодекс обновлен', 1);

SELECT * FROM users;
SELECT * FROM posts;
