CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    password TEXT, 
    role TEXT
);

CREATE TABLE recipes (
    id SERIAL, 
    name TEXT, 
    type TEXT, 
    author_id INTEGER, 
    base_liquid TEXT, 
    grain TEXT, 
    protein TEXT, 
    ingredient_1 TEXT, 
    ingredient_2 TEXT, 
    sweetener TEXT,
    CONSTRAINT recipes_pk PRIMARY KEY (id),
    CONSTRAINT recipes_users_fk
        FOREIGN KEY(author_id)
            REFERENCES users(id)
);

CREATE TABLE favorites (
    id SERIAL, 
    user_id INTEGER, 
    recipe_id INTEGER, 
    CONSTRAINT favorites_pk PRIMARY KEY (id),
    CONSTRAINT favorites_users_fk
        FOREIGN KEY(user_id)
            REFERENCES users(id),
    CONSTRAINT favorites_recipes_fk
        FOREIGN KEY(recipe_id)
            REFERENCES recipes(id)
);

CREATE TABLE upvotes (
    id SERIAL, 
    user_id INTEGER, 
    recipe_id INTEGER, 
    stars INTEGER,
    CONSTRAINT upvotes_pk PRIMARY KEY (id),
    CONSTRAINT upvotes_users_fk
        FOREIGN KEY(user_id)
            REFERENCES users(id),
    CONSTRAINT upvotes_recipes_fk
        FOREIGN KEY(recipe_id)
            REFERENCES recipes(id)
);

CREATE TABLE comments (
    id SERIAL, 
    user_id INTEGER, 
    recipe_id INTEGER, 
    comment_text TEXT,
    CONSTRAINT comments_pk PRIMARY KEY (id),
    CONSTRAINT comments_users_fk
        FOREIGN KEY(user_id)
            REFERENCES users(id),
    CONSTRAINT comments_recipes_fk
        FOREIGN KEY(recipe_id)
            REFERENCES recipes(id)
);

CREATE TABLE recipe_of_the_week (
    id SERIAL, 
    recipe_id INTEGER, 
    date TEXT,
    CONSTRAINT recipe_of_the_week_pk PRIMARY KEY (id),
    CONSTRAINT recipe_of_the_week_recipes_fk
        FOREIGN KEY(recipe_id)
            REFERENCES recipes(id)
);