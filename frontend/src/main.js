import { createApp } from 'vue';
import { createPinia } from "pinia";
import App from './App.vue';
import router from './router';
import VueCryptojs from 'vue-cryptojs';
import axios from 'axios';
import VueAxios from 'vue-axios';

import UserGreeting from './components/UserGreeting.vue';

import "./assets/main.scss";

const app = createApp(App);
const pinia = createPinia();

app.use(router);
app.use(pinia);
app.use(VueCryptojs);
app.use(VueAxios, axios);
app.config.globalProperties.$backendUrl = "http://127.0.0.1:5000/"
app.config.globalProperties.$apiChoice = "mockapi"

app.component('UserGreeting', UserGreeting);

app.mount("#app");
