import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "@/components/LandingPage.vue";
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import User from "@/components/User.vue";
import Scheduler from "@/components/Scheduler.vue";

const routes = [{
    path: "/",
    name: "LandingPage",
    component: LandingPage,
},
{
    path: "/login",
    name: "Login",
    component: Login,
},
{
    path: "/register",
    name: "Register",
    component: Register,
},
{
    path: "/user",
    name: "User",
    component: User,
},
{
    path: "/schedule",
    name: "Scheduler",
    component: Scheduler,
    beforeEnter: (to, from, next) => {
        if (true) {
            next();
        } else {
            next('/user');
        }
    }
}
];

const router = createRouter({
    history: createWebHistory(),
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition;
        }
        if (to.hash) {
            return { el: to.hash, behavior: "smooth" };
        }
        return { top: 0, behavior: "smooth" };
    },
    routes,
});

export default router;