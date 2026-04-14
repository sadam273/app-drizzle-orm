import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  scenarios: {
    spike_test: {
      executor: "ramping-vus",
      startVUs: 0,
      stages: [
        { duration: "5s", target: 50 },
        { duration: "10s", target: 50 },
        { duration: "5s", target: 0 },
      ],
    },
  },
};

export default function () {
  const res = http.get("http://localhost:3000/movies");

  check(res, {
    "status is 200": (r) => r.status === 200,
  });

  sleep(0.5);
}
