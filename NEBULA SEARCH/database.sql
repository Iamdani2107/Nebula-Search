CREATE DATABASE buscador;
USE buscador;

CREATE TABLE articulos (
    id INT  PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL
);

INSERT INTO articulos (titulo, contenido) VALUES
('Artículo 1', 'Este es el contenido del artículo 1'),
('Artículo 2', 'Este es el contenido del artículo 2'),
('Artículo 3', 'Este es el contenido del artículo 3');
