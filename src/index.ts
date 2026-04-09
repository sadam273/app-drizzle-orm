import "dotenv/config";
import express from "express";
import movieRouter from "./routes/movies";
import loanRouter from "./routes/loans";

const app = express();
app.use(express.json()); //middleware yang convert request body jadi JSON

app.use("/movies", movieRouter);
app.use("/loans", loanRouter);

app.listen(3000, () => {
  //ngetest apakah dah jalan kalo di run
  console.log("Server running on port 3000");
});
