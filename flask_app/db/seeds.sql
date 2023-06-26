-- Create seed data for users with no team_id assigned yet as there are no teams created yet.
INSERT INTO users (first_name, last_name, password, email, team_id)
VALUES ('Claire', 'Cho', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'guest@gmail.com', NULL),
       ('Scott', 'Hall', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'scott@gmail.com', NULL),
       ('Peter', 'Williams', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'peter@gmail.com', NULL),
       ('Emma', 'Smith', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'emma@gmail.com', NULL),
       ('John', 'Doe', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'john@gmail.com', NULL),
       ('Susan', 'Watson', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'susan@gmail.com', NULL);

-- Create seed data for teams and assign users to each team
INSERT INTO teams (name, user_id)
VALUES ('Engineering', 1),
       ('Marketing', 1),
       ('Sales', 2);

-- Assign team
UPDATE users SET team_id = 1 WHERE id = 1;

INSERT INTO team_user (team_id, user_id)
VALUES (1, 1),
       (1, 2),
       (1, 3),
       (1, 4),
       (1, 5),
       (2, 1),
       (2, 6);

INSERT INTO tasks (category, description, status, due_date, assignee_id, user_id, team_id)
VALUES ('Private', 'Develop a python app','To do', '2023-12-31', 1, 1, 1),
       ('Private', 'Research new software programs', 'Done', '2023-06-05', 1, 1, 1),
       ('Public', 'Design MERN project', 'To do', '2023-03-16', 2, 3, 1),
       ('Public', 'Debug test', 'In progress', '2023-03-01', 1, 3, 1);