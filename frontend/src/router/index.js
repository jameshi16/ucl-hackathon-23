import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
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
        }
    ],
});

export default router;
