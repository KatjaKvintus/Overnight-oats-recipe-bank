CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    password TEXT, 
    role TEXT
);

CREATE TABLE favorites (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER, 
    recipe_id INTEGER
);

CREATE TABLE upvotes (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER, 
    recipe_id INTEGER, 
    stars INTEGER
);

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    type TEXT, 
    author_id TEXT, 
    base_liquid TEXT, 
    grain TEXT, 
    protein TEXT, 
    ingredient_1 TEXT, 
    ingredient_2 TEXT, 
    sweetener TEXT
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER, 
    recipe_id INTEGER, 
    comment_text TEXT
);

CREATE TABLE recipe_of_the_week (
    id SERIAL PRIMARY KEY, 
    recipe_id INTEGER, 
    date TEXT
);
