import { pgTable, serial, varchar, integer, date } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  userId: serial("user_id").primaryKey(),
  userName: varchar("user_name", { length: 255 }).notNull(),
  noId: varchar("no_id", { length: 100 }).notNull(),
});

export const directors = pgTable("directors", {
  directorId: serial("director_id").primaryKey(),
  directorName: varchar("director_name", { length: 255 }).notNull(),
  bornDt: date("born_dt"),
});

export const movies = pgTable("movies", {
  movieId: serial("movie_id").primaryKey(),
  directorId: integer("director_id")
    .notNull()
    .references(() => directors.directorId),
  movieDescription: varchar("movie_description", { length: 500 }),
  movieName: varchar("movie_name", { length: 255 }).notNull(),
});

export const loans = pgTable("loans", {
  loanId: serial("loan_id").primaryKey(),
  movieId: integer("movie_id")
    .notNull()
    .references(() => movies.movieId),
  userId: integer("user_id")
    .notNull()
    .references(() => users.userId),
  loanDate: date("loan_date").notNull(),
  returnDate: date("return_date"),
});
