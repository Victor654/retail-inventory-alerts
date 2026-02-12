import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const requestCode = (phone_number) => {
  return api.post("/auth/request-code", { phone_number });
};