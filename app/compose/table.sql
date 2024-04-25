-- public."comments" definition

-- Drop table

-- DROP TABLE public."comments";

CREATE TABLE public."comments" (
	id serial4 NOT NULL,
	date_comment timestamp NOT NULL,
	email varchar(120) NOT NULL,
	"comment" varchar(120) NOT NULL,
	content_id int4 NOT NULL,
	CONSTRAINT comments_pkey PRIMARY KEY (id)
);