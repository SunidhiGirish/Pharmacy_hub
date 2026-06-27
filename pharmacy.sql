CREATE DATABASE pharmacy_hubs;
USE pharmacy_hubs;


CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE medicines (
    medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    stock INT DEFAULT 0,
    category_id INT,
    image_url VARCHAR(255),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
select * from users;




SELECT * FROM categories;

INSERT INTO categories (category_name)
VALUES ('General Medicines');

SELECT * FROM categories;
DESCRIBE categories;

INSERT INTO medicines
(name, description, price, stock, category_id, image_url)
VALUES
('Benadryl Syrup', 'Cough relief syrup', 120.00, 50, 1, 'images/benadryl.jpg'),
('Aspirin', 'Pain relief tablet', 60.00, 100, 1, 'images/aspirin.jpg'),
('Azithromycin 250mg', 'Antibiotic tablet', 180.00, 75, 1, 'images/azithromycin.jpg'),
('Cetirizine', 'Allergy relief tablet', 45.00, 120, 1, 'images/cetirizine.jpg'),
('Cofsils Syrup', 'Dry cough syrup', 110.00, 60, 1, 'images/cofsils.jpg'),
('Ibuprofen', 'Pain and inflammation relief', 75.00, 90, 1, 'images/ibuprofen.jpg'),
('Multivitamin', 'Daily health supplement', 250.00, 40, 1, 'images/multivitamin.jpg'),
('Omez 40', 'Acidity and gastric relief tablet', 140.00, 80, 1, 'images/omez40.jpg'),
('Paracetamol 500mg', 'Fever and pain relief tablet', 30.00, 150, 1, 'images/paracetamol.jpg'),
('Vitamin C 500mg', 'Immunity booster supplement', 95.00, 70, 1, 'images/vitaminc.jpg');

TRUNCATE TABLE medicines;
select * from medicines;

INSERT INTO medicines
(name, description, price, stock, category_id, image_url)
VALUES
('Benadryl Syrup', 'Cough relief syrup', 120.00, 50, 1, 'images/antihistamine.jpg'),
('Aspirin', 'Pain relief tablet', 60.00, 100, 1, 'images/aspirin.jpg'),
('Azithromycin 250mg', 'Antibiotic tablet', 180.00, 75, 1, 'images/azithromycin.jpg'),
('Cetirizine', 'Allergy relief tablet', 45.00, 120, 1, 'images/coldmedicine.jpg'),
('Cofsils Syrup', 'Dry cough syrup', 110.00, 60, 1, 'images/coughsyrup.jpg'),
('Ibuprofen', 'Pain and inflammation relief tablet', 75.00, 90, 1, 'images/ibuprofen.jpg'),
('Multivitamin', 'Daily health supplement', 250.00, 40, 1, 'images/multivitamins.jpg'),
('Omez 40', 'Acidity and gastric relief tablet', 140.00, 80, 1, 'images/omeprazole.jpg'),
('Paracetamol 500mg', 'Fever and pain relief tablet', 30.00, 150, 1, 'images/paracetamol.jpg'),
('Vitamin C 500mg', 'Immunity booster supplement', 95.00, 70, 1, 'images/vitaminc.jpg');



DESCRIBE medicines;