-- Create seed data for users with null team_id as there are no teams created yet.
INSERT INTO users (first_name, last_name, password, email, team_id)
VALUES ('Claire', 'Cho', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'guest@gmail.com', NULL),
       ('Scott', 'Hall', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'scott@gmail.com', NULL),
       ('Peter', 'Williams', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'peter@gmail.com', NULL),
       ('Emma', 'Smith', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'emma@gmail.com', NULL),
       ('John', 'Doe', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'john@gmail.com', NULL),
       ('Susan', 'Watson', '$2b$12$3nwZp4NEMRNxLGy3gQBNMO4KVig/VCRAxVhjVMIvZ.wVD1Hxttzp.', 'susan@gmail.com', NULL);

-- Create seed data for teams and assign user_id of team creator to each team.
INSERT INTO teams (name, user_id)
VALUES ('Engineering', 1),
       ('Marketing', 2),
       ('Sales', 3);

-- Update users' team id.
UPDATE users SET team_id = 1 WHERE id = 1 OR id = 4 OR id = 5;
UPDATE users SET team_id = 2 WHERE id = 2;
UPDATE users SET team_id = 3 WHERE id = 3;

-- Create seed data for tasks.
INSERT INTO tasks (category, description, status, due_date, user_id, team_id)
VALUES ('Private', 'Develop a python app','To do', '2023-12-31', 1, 1),
       ('Public', 'Research new software programs', 'Done', '2023-06-05', 1, 1),
       ('Public', 'Design MERN project', 'To do', '2023-03-16', 3, 1),
       ('Public', 'Debug test', 'In progress', '2023-03-01', 3, 1),
       ('Private', 'Finish online python tutorials', 'To do', '2023-08-09', 1, 1);