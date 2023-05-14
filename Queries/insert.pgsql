INSERT INTO "Role" VALUES
    ('52fcf505afe14a2e9a08f84f46065af1', 'Администратор'),
    ('5f555aa487984b85837234107d126caf', 'Врач');

--password: admin -> pbkdf2:sha256:600000$UnJIwurI8k0q1xkP$78d23a95d8e77562c0fe033540ff5fe33dcfa9372202d2da0818c6eef4b74c21
--password: doc -> pbkdf2:sha256:600000$gEWfFJMz9gGbtHo2$71f42cfd762bcd86cf2fd93e1d57c060525f00076507460a51b55ca32438eb22

INSERT INTO "Employee" VALUES
    ('725e59ad3e10496ba82b77460dbc4a7b', 'Вячеслав', 'Лампочкин', 'Васильевич', 'admin', 'pbkdf2:sha256:600000$UnJIwurI8k0q1xkP$78d23a95d8e77562c0fe033540ff5fe33dcfa9372202d2da0818c6eef4b74c21', '52fcf505afe14a2e9a08f84f46065af1'),
    ('a9a020a7002c49e9b2bc2d6ac3b7cf23', 'Дмитрий', 'Казанцев', 'Андреевич', 'doc', 'pbkdf2:sha256:600000$gEWfFJMz9gGbtHo2$71f42cfd762bcd86cf2fd93e1d57c060525f00076507460a51b55ca32438eb22', '5f555aa487984b85837234107d126caf');

INSERT INTO "Patient"(name, surname, midname, doctorguid) VALUES
    ('Анна', 'Викторовна', 'Скрижаль', 'a9a020a7002c49e9b2bc2d6ac3b7cf23');

