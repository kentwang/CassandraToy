CREATE KEYSPACE movies;
CREATE TABLE movies ( distribution text, votes varint, rank float, title text PRIMARY KEY );
CREATE TABLE movies ( distribution text, votes varint, rank float, title text, PRIMARY KEY (title, rank, votes));
CREATE INDEX ON movies(rank);


CREATE TABLE literature ( MOVI text PRIMARY KEY, NOVLAuthor text, NOVLTitle text, BOOKAuthor text, BOOKTitle text, ADPTAuthor text, ADPTTitle text);
