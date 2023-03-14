INSERT INTO teams (name)
VALUES ('Engineering'),
       ('Marketing');

INSERT INTO users (first_name, last_name, password, email, team_id)
VALUES ('Guest', 'User', '1234', 'guest@email.com', 1),
       ('Clare', 'Cho', '1234', 'claire@email.com', 1),
       ('Peter', 'Williams', '1234', 'peter@email.com', 1),
       ('Emma', 'Smith', '1234', 'emma@email.com', 1),
       ('John', 'Doe', '1234', 'john@email.com', 2),
       ('Susan', 'Watson', '1234', 'susan@email.com', 2);

INSERT INTO tasks (category, description, status, due_date, assignee_id, user_id)
VALUES ('Private', 'Develop a python app','To do', '2023-12-31', 1, 1),
       ('Private', 'Research new software programs', 'Done', '2023-06-05', 1, 1),
       ('Public', 'Design MERN project', 'To do', '2023-03-16', 2, 3),
       ('Public', 'Debug test', 'In progress', '2023-03-01', 1, 3);