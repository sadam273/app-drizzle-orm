import { Router, Request, Response } from "express";
import { db } from "../db";
import { movies } from "../db/schema";
import { eq } from "drizzle-orm";

const router = Router();

// GET semua movie
router.get("/", async (req: Request, res: Response) => {
  const allMovies = await db.select().from(movies);
  res.json(allMovies);
});

// PUT update movie
router.put("/:id", async (req: Request, res: Response) => {
  const { movieName, movieDescription, directorId } = req.body;
  const updated = await db
    .update(movies)
    .set({ movieName, movieDescription, directorId })
    .where(eq(movies.movieId, Number(req.params.id)))
    .returning();
  res.json(updated[0]);
});

export default router;
