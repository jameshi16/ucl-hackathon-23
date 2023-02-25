import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCryptojs from 'vue-cryptojs'

import UserGreeting from './components/UserGreeting.vue'

import './assets/main.css'

const app = createApp(App)

app.use(router)
app.use(VueCryptojs)

app.component('UserGreeting', UserGreeting);

app.mount('#app')
