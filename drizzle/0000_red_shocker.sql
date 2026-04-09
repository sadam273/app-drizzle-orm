CREATE TABLE "directors" (
	"director_id" serial PRIMARY KEY NOT NULL,
	"director_name" varchar(255) NOT NULL,
	"born_dt" date
);
--> statement-breakpoint
CREATE TABLE "loans" (
	"loan_id" serial PRIMARY KEY NOT NULL,
	"movie_id" integer NOT NULL,
	"user_id" integer NOT NULL,
	"loan_date" date NOT NULL,
	"return_date" date
);
--> statement-breakpoint
CREATE TABLE "movies" (
	"movie_id" serial PRIMARY KEY NOT NULL,
	"director_id" integer NOT NULL,
	"movie_description" varchar(500),
	"movie_name" varchar(255) NOT NULL
);
--> statement-breakpoint
CREATE TABLE "users" (
	"user_id" serial PRIMARY KEY NOT NULL,
	"user_name" varchar(255) NOT NULL,
	"no_id" varchar(100) NOT NULL
);
--> statement-breakpoint
ALTER TABLE "loans" ADD CONSTRAINT "loans_movie_id_movies_movie_id_fk" FOREIGN KEY ("movie_id") REFERENCES "public"."movies"("movie_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "loans" ADD CONSTRAINT "loans_user_id_users_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("user_id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "movies" ADD CONSTRAINT "movies_director_id_directors_director_id_fk" FOREIGN KEY ("director_id") REFERENCES "public"."directors"("director_id") ON DELETE no action ON UPDATE no action;