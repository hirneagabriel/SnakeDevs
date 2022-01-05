drop table if exists user;
drop table if exists post;
drop table if exists temperature;
drop table if exists rgb;
drop table if exists timer;
drop table if exists holiday;
drop table if exists stock;

create table user (
  id integer primary key autoincrement,
  username text unique not null,
  password text not null
);

create table post (
  id integer primary key autoincrement,
  author_id integer not null,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

create table temperature (
  id integer primary key autoincrement,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  value REAL NOT NULL
);

create table rgb (
    id integer primary key autoincrement,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    red REAL NOT NULL,
    green REAL NOT NULL,
    blue REAL NOT NULL
);

create table timer (
  id integer primary key autoincrement,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  is_closed BOOL NOT NULL DEFAULT TRUE,
  time REAL NOT NULL
);

create table holiday (
  id integer primary key autoincrement,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  is_away BOOL NOT NULL DEFAULT FALSE,
  days INTEGER NOT NULL
);

create table stock (
  id integer primary key autoincrement,
  product_name varchar(64) not null,
  quantity numeric(5) not null,
  product_expiration_date TIMESTAMP NOT NULL,
  shelf_number NUMERIC(5) NOT NULL
);