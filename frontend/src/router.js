import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "@/components/LandingPage.vue";
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import User from "@/components/User.vue";
import Scheduler from "@/components/Scheduler.vue";

<<<<<<< HEAD
function isLoggedIn() {
    return !!localStorage.getItem('isUserLoggedIn');
}

=======
>>>>>>> f1abda14fb93aa4355ff7e93eb5da528410905cb
const routes = [{
    path: "/",
    name: "LandingPage",
    component: LandingPage,
},
{
    path: "/login",
    name: "Login",
    component: Login,
<<<<<<< HEAD
    beforeEnter: (to, from, next) => {
        if (isLoggedIn()) {
            next('/user'); // Redirect to the user page or another appropriate route
        } else {
            next(); // Proceed to login page
        }
    }
=======
>>>>>>> f1abda14fb93aa4355ff7e93eb5da528410905cb
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
<<<<<<< HEAD
    beforeEnter: (to, from, next) => {
        if (isLoggedIn()) {
            next();
        } else {
            next('/login');
        }
    }
=======
>>>>>>> f1abda14fb93aa4355ff7e93eb5da528410905cb
},
{
    path: "/schedule",
    name: "Scheduler",
    component: Scheduler,
    beforeEnter: (to, from, next) => {
<<<<<<< HEAD
        if (isLoggedIn()) {
            next();
        } else {
            next('/login');
=======
        if (true) {
            next();
        } else {
            next('/user');
>>>>>>> f1abda14fb93aa4355ff7e93eb5da528410905cb
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