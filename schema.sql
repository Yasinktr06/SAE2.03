USE gestion_notes;

-- Création de la table 'etudiant'
CREATE TABLE etudiant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_etudiant VARCHAR(50) UNIQUE NOT NULL,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    groupe VARCHAR(50),
    photo VARCHAR(255),
    email VARCHAR(150)
);

-- Création de la table 'ue'
CREATE TABLE ue (
    code VARCHAR(20) PRIMARY KEY,
    nom VARCHAR(200),
    semestre VARCHAR(20),
    credit_ects INT
);

-- Création de la table 'ressource'
CREATE TABLE ressource (
    code VARCHAR(50) PRIMARY KEY,
    nom VARCHAR(200),
    descriptif TEXT,
    coefficient FLOAT,
    ue_code VARCHAR(20),
    FOREIGN KEY (ue_code) REFERENCES ue(code) ON DELETE CASCADE
);

-- Création de la table 'enseignant'
CREATE TABLE enseignant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100)
);

-- Création de la table 'examen'
CREATE TABLE examen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(200),
    date DATE,
    coefficient FLOAT
);

-- Création de la table 'note' (relation entre examen et étudiant)
CREATE TABLE note (
    examen_id INT,
    etudiant_id INT,
    note FLOAT,
    appreciation TEXT,
    PRIMARY KEY (examen_id, etudiant_id),
    FOREIGN KEY (examen_id) REFERENCES examen(id) ON DELETE CASCADE,
    FOREIGN KEY (etudiant_id) REFERENCES etudiant(id) ON DELETE CASCADE
);

-- Insertion de données exemple

-- Étudiants
INSERT INTO etudiant (numero_etudiant, nom, prenom, groupe, email) 
VALUES 
('E12345', 'Dupont', 'Pierre', 'G1', 'pierre.dupont@email.com'),
('E12346', 'Durand', 'Marie', 'G2', 'marie.durand@email.com');

-- UE
INSERT INTO ue (code, nom, semestre, credit_ects)
VALUES 
('UE101', 'Informatique', 'Semestre 1', 6),
('UE102', 'Mathématiques', 'Semestre 1', 5);

-- Ressources
INSERT INTO ressource (code, nom, descriptif, coefficient, ue_code)
VALUES 
('R101', 'Livres', 'Livres de cours pour UE101', 1.5, 'UE101'),
('R102', 'Tutoriels', 'Tutoriels pour UE102', 1.0, 'UE102');

-- Enseignants
INSERT INTO enseignant (nom, prenom)
VALUES 
('Lemoine', 'Jean'),
('Martin', 'Claire');

-- Examens
INSERT INTO examen (titre, date, coefficient)
VALUES 
('Examen Informatique', '2025-06-10', 2.0),
('Examen Mathématiques', '2025-06-15', 1.5);

-- Notes
INSERT INTO note (examen_id, etudiant_id, note, appreciation)
VALUES 
(1, 1, 15, 'Bon travail'),
(2, 2, 12, 'A améliorer');
