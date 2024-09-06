INSERT INTO users (username, passowrd, role, description) 
VALUES 
('john_doe', 'password123', 'admin', 'Administrator of the system'),
('jane_smith', 'jane@456', 'editor', 'Editor responsible for content'),
('michael_brown', 'mike!789', 'viewer', 'Viewer with read-only access'),
('alice_jones', 'alice#987', 'moderator', 'Moderator who manages comments'),
('chris_evans', 'chris@123', 'guest', 'Guest user with limited access');

SELECT * FROM users;