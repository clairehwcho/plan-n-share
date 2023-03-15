INSERT INTO teams (name)
VALUES ('Engineering'),
       ('Marketing'),
       ('Sales');

INSERT INTO users (first_name, last_name, password, email, team_id)
VALUES ('Claire', 'Cho', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'guest@email.com', 1),
       ('Scott', 'Hall', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'scott@email.com', 1),
       ('Peter', 'Williams', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'peter@email.com', 1),
       ('Emma', 'Smith', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'emma@email.com', 1),
       ('John', 'Doe', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'john@email.com', 1),
       ('Susan', 'Watson', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'susan@email.com', 1);

INSERT INTO tasks (category, description, status, due_date, assignee_id, user_id)
VALUES ('Private', 'Develop a python app','To do', '2023-12-31', 1, 1),
       ('Private', 'Research new software programs', 'Done', '2023-06-05', 1, 1),
       ('Public', 'Design MERN project', 'To do', '2023-03-16', 2, 3),
       ('Public', 'Debug test', 'In progress', '2023-03-01', 1, 3);