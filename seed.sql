-- Directors
INSERT INTO directors (director_name, born_dt) VALUES
('Christopher Nolan', '1970-07-30'),
('Steven Spielberg', '1946-12-18'),
('Martin Scorsese', '1942-11-17'),
('Quentin Tarantino', '1963-03-27'),
('James Cameron', '1954-08-16');
-- Users
INSERT INTO users (user_name, no_id) VALUES
('Budi Santoso', 'ID001'),
('Siti Rahayu', 'ID002'),
('Ahmad Fauzi', 'ID003'),
('Dewi Lestari', 'ID004'),
('Rizky Pratama', 'ID005');
-- Movies
INSERT INTO movies (director_id, movie_name, movie_description) VALUES
(1, 'Inception', 'A thief who enters the dreams of others to steal secrets'),
(1, 'Interstellar', 'A team of explorers travel through a wormhole in space'),
(2, 'Jurassic Park', 'A theme park with cloned dinosaurs goes wrong'),
(3, 'The Departed', 'An undercover cop and a mole in the police try to identify each other'),
(4, 'Pulp Fiction', 'The lives of two mob hitmen intertwine in a series of stories');
-- Loans
INSERT INTO loans (movie_id, user_id, loan_date, return_date) VALUES
(1, 1, '2024-01-01', '2024-01-07'),
(2, 2, '2024-01-05', '2024-01-12'),
(3, 3, '2024-01-10', NULL),
(4, 4, '2024-01-15', '2024-01-20'),
(5, 5, '2024-01-20', NULL);