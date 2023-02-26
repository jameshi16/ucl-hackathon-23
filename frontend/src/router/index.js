import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import { useAuthStore } from "../stores/auth";
import Search from "../views/Search.vue";
import Topic from "../views/Topic.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: Login,
        },
        {
            path: "/search",
            name: "search",
            component: Search,
        },
        {
            path: "/topic",
            name: "topic",
            component: Topic
        },
    ],
});

router.beforeEach((to, from) => {
    if (to.name !== "home" && useAuthStore().logged_in === null) return "/";
});

export default router;
