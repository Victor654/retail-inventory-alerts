import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";

const routes = [
  { path: "/login", component: LoginView },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});