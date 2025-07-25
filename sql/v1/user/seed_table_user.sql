INSERT INTO user (display_name, first_name, last_name, date_of_birth) SELECT display_name, first_name, last_name, date_of_birth FROM seed_user;
DROP TABLE seed_user;

INSERT INTO user (display_name, first_name, last_name, date_of_birth) VALUES (
	"the_one_and_only_john",
	"John",
	"Smith",
	"1990-02-15"
);

INSERT INTO user (display_name, first_name, last_name, date_of_birth) VALUES (
	"not_tarzan",
	"Jane",
	"Smith",
	"1991-03-10"
);