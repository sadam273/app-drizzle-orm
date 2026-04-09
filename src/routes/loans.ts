import { Router, Request, Response } from "express";
import { db } from "../db";
import { loans, movies } from "../db/schema";
import { count, eq } from "drizzle-orm";

const router = Router();

router.get("/group-by-movie", async (req: Request, res: Response) => {
  const result = await db
    .select({
      movieId: movies.movieId,
      movieName: movies.movieName,
      totalLoan: count(loans.loanId),
    })
    .from(loans)
    .innerJoin(movies, eq(loans.movieId, movies.movieId))
    .groupBy(movies.movieId, movies.movieName);

  res.json(result);
});

router.get("/:id", async (req: Request, res: Response) => {
  const loan = await db
    .select()
    .from(loans)
    .where(eq(loans.loanId, Number(req.params.id)));
  res.json(loan[0]);
});

router.post("/", async (req: Request, res: Response) => {
  const { movieId, userId, loanDate, returnDate } = req.body;
  const newLoan = await db
    .insert(loans)
    .values({ movieId, userId, loanDate, returnDate })
    .returning();
  res.json(newLoan[0]);
});

// DELETE loan
router.delete("/:id", async (req: Request, res: Response) => {
  await db.delete(loans).where(eq(loans.loanId, Number(req.params.id)));
  res.json({ message: "Loan deleted" });
});

export default router;
