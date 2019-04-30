-- Kevin Macario 17369
-- LABORATORIO 12

-- Ejercicio 1
CREATE USER operador PASSWORD '123456';
GRANT CONNECT ON DATABASE laboratorio12 TO operador;

-- Ejercicio 2
CREATE USER gerente PASSWORD '123456';
GRANT CONNECT ON DATABASE laboratorio12 TO gerente;

-- Ejercicio 3
CREATE USER administrador PASSWORD '123456';
GRANT CONNECT ON DATABASE laboratorio12 TO administrador;

-- Ejercicio 4
GRANT ALL PRIVILEGES ON DATABASE laboratorio12 TO administrador WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO administrador WITH GRANT OPTION; 

-- Ejercicio 5
GRANT SELECT ON ALL TABLES IN SCHEMA public TO operador;

-- Ejercicio 6
GRANT SELECT,INSERT ON ALL TABLES IN SCHEMA public TO gerente;

-- Ejercicio 7
GRANT CREATE ON DATABASE laboratorio12 TO gerente;

-- Ejercicio 8
REVOKE REFERENCES,TRIGGER ON ALL TABLES IN SCHEMA public FROM operador;
