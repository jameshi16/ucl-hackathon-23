import { createApp } from 'vue'
import { createPinia } from "pinia";
import App from './App.vue'
import router from './router'
import VueCryptojs from 'vue-cryptojs'

import UserGreeting from './components/UserGreeting.vue'

import "./assets/main.scss";

const app = createApp(App);
const pinia = createPinia();

app.use(router);
app.use(pinia);
app.use(VueCryptojs);

app.component('UserGreeting', UserGreeting);

app.mount("#app");
